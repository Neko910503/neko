import openai
import os
import secrets
import time
import string

while(1):
    # 生成一個隨機的字串，長度為48
    random_string = "sk-"
    alphabet = string.ascii_letters + string.digits
    random_string += ''.join(secrets.choice(alphabet) for i in range(48))

    #print(random_string)
    key = random_string
    # 載入 API 金鑰
    openai.api_key = key
    try:
        openai.Completion.create(
            engine="text-davinci-002",
            prompt="Hello, world!",
            max_tokens=5
        )
        print(f"金鑰 {key} 是有效的！")
        break
    except Exception as e:
        print(f"金鑰 {key} 是無效的：{str(e)}")
    time.sleep(0)