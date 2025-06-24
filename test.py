# from colorama import Fore
# from selenium import webdriver
# from selenium.webdriver.common.by import By

import openai
import os
import json

from google import genai

from google.genai.types import Tool, GenerateContentConfig, GoogleSearch
from pydantic import BaseModel


def main():
    # openai.api_key = "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"
    # response = openai.completions.create(
    #     model="gpt-4o",
    #     prompt=[
    #         {"role":"system", "content": "You are a helpful assistant"}
    #     ]
    # )
    # print(response['choices'][0]['message']['content'])
    class Shoe(BaseModel):
        shoe_name: str
        desc: str
    
    client = genai.Client(api_key="AIzaSyD5bI0i5MlVk-3pUpR2aAoDvHvkNfi6fWg")
    model_id="gemini-2.5-flash"

    url_context_tool = Tool(
        url_context = GoogleSearch
    )

    response = client.models.generate_content(
        model=model_id,
        contents="provide a one to two paragraph description of this https://www.dickssportinggoods.com/p/nike-mens-dunk-low-shoes-24nikmdnklwrtrvrkmns/24nikmdnklwrtrvrkmns?color=White%2FGym%20Red",
        config={
            "response_mime_type":"application/json",
            "response_schema": list[Shoe],
        },
    )
    result = json.loads(response.text)
    shoe = Shoe(**result[0])

    print("Shoe Name: ", shoe.shoe_name)
    print("Description: ", shoe.desc)

if __name__ == "__main__":
    main()








