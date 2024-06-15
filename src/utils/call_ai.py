import json

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.gpt_tem import GPT_Template
from utils.gemini_tem import Gemini_Template

def call_aied(quest):
    prompt = f"""
{quest}

json 格式:
{{
    "輸出": ""
}}
"""
    try:
        # res = GPT_Template(prompt)
        res = Gemini_Template(prompt)
        res = json.loads(res)["輸出"]
    except:
        res = "LLM 當掉囉! 請重新發問 >_<"

    return res
