import json

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.gpt_tem import GPT_Template
from utils.gemini_tem import Gemini_Template

def call_aied(chart, mess):
    prompt = f"""
【流程】：{chart}

【通話紀錄】：{mess}

請根據【流程】檢查【通話紀錄】中客服人員是否有依照【流程】來處理客戶的問題

輸出 JSON 格式：
{{
    "流程遵守": ""
}}

如果客服人員完全遵守流程來對話，請輸出 "流程遵守": "pass"
如果客服人員僅遵守到 3.1 步，請輸出 "流程遵守": "3.1"
如果客服人員一開始就沒有依照流程，請輸出 "流程遵守": "0"
"""
    try:
        # res = GPT_Template(prompt)
        res = Gemini_Template(prompt)
        res = json.loads(res)["輸出"]
    except:
        res = "LLM 當掉囉! 請重新發問 >_<"

    return res
