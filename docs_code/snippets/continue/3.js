import fs from 'fs';
import path from 'path';

export function modifyConfig(config: Config): Config {
  const logFile = path.join('/...', 'logfile.log');

  function log(message) {
    fs.appendFileSync(logFile, message + '\n');
  }

  config.models.push({
    options: {
      title: "Endpoint",
      model: "Model",
    },
    streamCompletion: async function* (prompt: string, options: CompletionOptions) {
      log("Prompt: " + prompt);

      try {
        const response = await fetch('http://localhost:8020/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ prompt: prompt })
        });

        if (!response.ok) {
          log(`HTTP error! status: ${response.status}`);
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let done = false;

        while (!done) {
          const { value, done: readerDone } = await reader.read();
          done = readerDone;
          if (value) {
            const decodedValue = decoder.decode(value);
            log("Value received: " + decodedValue);
            yield decodedValue;
          }
        }
      } catch (error) {
        log("Error during fetch: " + error);
        throw error;
      }
    },
  });

  log("Config modified");
  return config;
}