import openai
openai.api_key = "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"
completion = openai.ChatCompletion.create(
  model="ft:gpt-3.5-turbo-0613:samyok::89TdeWO9",
  messages = [{"role": "system", "content" : "Luna is a personal voice assistant that interacts with the user's browser. The goal is search for the definition of proficient"}, {"role": "user", "content": "[ { \"role\": \"combobox\", \"name\": \"Search Google or type a URL\" }, { \"role\": \"button\", \"name\": \"Search by voice\" }, { \"role\": \"button\", \"name\": \"Search by image\" }, { \"role\": \"link\", \"name\": \"Gmail\", \"description\": \"Gmail\", \"children\": [ [Object], [Object] ] }, { \"role\": \"link\", \"name\": \"Google Drive\", \"description\": \"Google Drive\", \"children\": [ [Object], [Object] ] }, { \"role\": \"button\", \"name\": \"Add shortcut\", \"description\": \"Add shortcut\" }, { \"role\": \"button\", \"name\": \"Customize Chrome\", \"description\": \"Customize this page\", \"pressed\": false } ]"}],
functions = [{"name": "click", "description": "Click on a given element on the page", "parameters": {"type": "object", "properties": {"role": {"type": "string", "description": "The role of the element to click on"}, "name": {"type": "string", "description": "The name of the element to click on"}}, "required": ["role", "name"]}}, {"name": "gotoPage", "description": "Go to a given page", "parameters": {"type": "object", "properties": {"url": {"type": "string", "description": "The URL of the page to go to"}}, "required": ["url"]}}]
)
print(completion)