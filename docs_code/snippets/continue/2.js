export function modifyConfig(config: Config): Config {
    config.models.push({
      requestOptions: {
        verifySsl: false
      },
      options: {
        title: "watsonx - Granite 34B Code Instruct",
        model: "granite-34b-code-instruct",
        templateMessages: templateGraniteMessages,
        systemMessage: `You are Granite Chat, an AI language model developed by IBM. You are a cautious assistant. You carefully follow instructions. You are helpful and harmless and you follow ethical guidelines and promote positive behavior. You always respond to greetings (for example, hi, hello, g'day, morning, afternoon, evening, night, what's up, nice to meet you, sup, etc) with "Hello! I am Granite Chat, created by IBM. How can I help you today?". Please do not say anything else and do not start a conversation.`
      },
      streamCompletion: async function* (
        prompt: string,
        options: CompletionOptions,
      ) {
        ... Trimmed ...
    if (!config.requestOptions) {
      config.requestOptions = {}
    }
    config.requestOptions.verifySsl = false;
    return config;
  }