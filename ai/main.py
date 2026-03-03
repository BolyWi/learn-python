import sys
import threading as thread
import time
from openai import OpenAI  

api_key = "sk-mR8hv32In0DqaIg83e60Dd2c97Ca42Fb8bD9Ac83A8059179"
api_base = "http://maas-api.cn-huabei-1.xf-yun.com/v1"
api_model_id = "xop3qwen1b7"

def unified_chat_test(model_id, messages, use_stream=False, extra_body={}):
    client = OpenAI(api_key=api_key, base_url=api_base)
    try:
        response = client.chat.completions.create(
            model=model_id,
            messages=messages,
            stream=use_stream,
            temperature=0.7,
            max_tokens=4096,
            extra_headers={"lora_id": "0"},  # 调用微调大模型时,对应替换为模型服务卡片上的resourceId
            stream_options={"include_usage": True},
            extra_body=extra_body
        )

        if use_stream:
            # 处理流式响应
            full_response = ""
            print("--- 流式输出 ---")
            for chunk in response:
                if hasattr(chunk.choices[0].delta, 'content') and chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    print(content, end="", flush=True)
                    full_response += content
            print("\n\n--- 完整响应 ---")
            print(full_response)
        else:
            # 处理非流式响应
            print("--- 非流式输出 ---")
            message = response.choices[0].message
            print(message.content)

    except Exception as e:
        print(f"请求出错: {e}")

if __name__ == "__main__":
    if sys.argv[1] != "":
        ask = sys.argv[1]
    else:
        ask = "你好，请介绍一下自己。"
    print(ask)
    thread.Thread(target=lambda: time.sleep(1) or print("正在请求中...")).start()
    plain_messages = [{"role": "user", "content": ask}]
    unified_chat_test(api_model_id, plain_messages, use_stream=False)
