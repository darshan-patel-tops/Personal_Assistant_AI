import os
import openai
from config import apikey
openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="hello",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)




'''
{
  "id": "cmpl-7UpOfvJ2ZPl0K2PRNcShHWuvI9awQ",
  "object": "text_completion",
  "created": 1687581765,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 167,
    "total_tokens": 167
  }
}
'''