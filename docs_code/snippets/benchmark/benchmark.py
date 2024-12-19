import fire
from ollama import chat
from time import time
from tqdm import tqdm
import json
import subprocess


def benchmark_ollama(prompt, model="llama3.2:3b", runs=10, verbose=False):
    times = []
    for _ in range(runs):
        response = chat(model=model, messages=[{'role': 'user', 'content': prompt}])
        
        if verbose:
            print(f"Output :: {response.message.content}")


def benchmark_genie(prompt, model="llama3.2:3b", runs=10, verbose=False):
    prefix = r'<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n'
    suffix = r'<|eot_id|><|start_header_id|>assistant<|end_header_id|>'
    input = prefix + prompt + suffix

    command = [
    'genie-t2t-run.exe', 
    '-c', 'genie_config.json',
    '-p', input
    ]

    if verbose:
        cx = " ".join(command)
        print(f"Command :: {cx}")

    for _ in range(runs):
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
            # print("Command output:")

            if verbose:
                print(f"Output :: {result.stdout}")

                if result.stderr:
                    print(f"Stderr :: {result.stderr}")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
    


def main(prompt=None, model="llama3.2:3b",  runs=1, backend="cpu", verbose=False, dataset = "dataset.json"):

    if backend == "cpu":
        benchmark = benchmark_ollama
    elif backend == "npu":
        benchmark = benchmark_genie

    if prompt is not None:
        benchmark(prompt, model, runs, verbose=verbose)
        return

    with open(dataset,"r") as file:
        data = json.load(file)

        for i in tqdm(range(len(data))):
            if isinstance(data[i], str):
                benchmark(data[i], model, runs)
            else:
                benchmark(".".join(data[i]["turns"]), model, runs)


if __name__ == '__main__':
    init_time = time()
    fire.Fire(main)
    end_time = time()
    print(f"Total time :: {end_time - init_time:.4f} seconds")
