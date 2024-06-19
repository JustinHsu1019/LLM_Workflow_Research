import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.gpt_tem import GPT_Template
from utils.gemini_tem import Gemini_Template

def call_aied(chart, mess):
    prompt = f"""
以下在一段python流程偽代碼，用於處理發貨問題
{chart}

以下是客服員工和客戶的對話，請仔細分析，並以JSON格式輸出偽代碼流程中的過程變量及變量值，最後輸出流程中的返回值
{mess}
"""
    prompt_mer = f"""
以下在一段 流程 Mermaid code，用於處理發貨問題
{chart}

以下是客服員工和客戶的對話，請仔細分析，並以JSON格式輸出偽代碼流程中的過程變量及變量值，最後輸出流程中的返回值
{mess}
"""
    try:
        # res = GPT_Template(prompt)
        res = Gemini_Template(prompt)
    except:
        res = "LLM 當掉囉! 請重新發問 >_<"

    return res
