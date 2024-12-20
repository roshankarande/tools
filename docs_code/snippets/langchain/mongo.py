import os

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage

from imagine.langchain import ImagineChat, ImagineEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient
from langchain_community.document_loaders import DirectoryLoader
from langchain.chains.retrieval_qa.base import RetrievalQA

# Full path to our books directory
books_dir = "/home/heyia/code/imagine-sdk-python/examples/langchain/rag/book"

# Full path to where we will create the vector store database
# store_name = "my_vector_db"
# db_dir = f"/path/to/{store_name}"

client = MongoClient("mongodb://admin:admin@url:28017/")
dbName = "rag"
collectionName = "embedd"
collection = client[dbName][collectionName]
       
loader = DirectoryLoader( books_dir, glob="./*.txt", show_progress=True)
data = loader.load()

embeddings_fn = ImagineEmbeddings()
vectorStore = MongoDBAtlasVectorSearch.from_documents(data, embeddings_fn, collection=collection )


def query_data(query):
    # Convert question to vector using OpenAI embeddings
    # Perform Atlas Vector Search using Langchain's vectorStore
    # similarity_search returns MongoDB documents most similar to the query    

    docs = vectorStore.similarity_search(query, K=1)
    as_output = docs[0].page_content
    model = ImagineChat(model="Llama-3-8B")
    retriever = vectorStore.as_retriever()
    qa = RetrievalQA.from_chain_type(model, chain_type="stuff", retriever=retriever)
    retriever_output = qa.run(query)
    
    return as_output, retriever_output


print(query_data("How can I learn more about LangChain?"))
