export function modifyConfig(config: Config): Config {
    config.models.push({
      options: {
        title: "My Custom LLM",
        model: "gemma-7b-it",
      },
      streamCompletion: async function* (
        prompt: string,
        options: CompletionOptions,
        fetch,
      ) {
        try {
          const response = await fetch('http://12.34.56.78:8000/v1/chat/completions', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              model: 'gemma-7b-it',
              messages: [
                {
                  role: 'user',
                  content: prompt,
                },
              ],
              max_tokens: 50,
            }),
          });
   
          if (!response.ok) {
            const errorText = await response.text();
            console.error('Error response from server:', errorText);
            throw new Error(`HTTP ${response.status} ${response.statusText} from ${response.url}`);
          }
   
          const text = await response.text();
          console.log('API Response Text:', text); // Log the response text
   
          const parsedData = JSON.parse(text);
          console.log('Parsed API Response:', parsedData); // Log the parsed response
   
          // Yield the content of the first choice
          if (parsedData.choices && parsedData.choices.length > 0) {
            yield parsedData.choices[0].message.content;
          } else {
            yield 'No completion available.';
          }
        } catch (error) {
          console.error('Error in streamCompletion:', error);
          yield 'An error occurred while fetching the completion.';
        }
      },
    });
    return config;
  }