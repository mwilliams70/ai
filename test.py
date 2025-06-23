# from colorama import Fore
# from selenium import webdriver
# from selenium.webdriver.common.by import By

import openai
import os


def main():
    openai.api_key = "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"
    response = openai.completions.create(
        model="gpt-4o",
        prompt=[
            {"role":"system", "content": "You are a helpful assistant"}
        ]
    )
    print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()


