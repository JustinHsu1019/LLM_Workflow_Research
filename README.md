# 流程圖呈現方式對 LLM 流程檢查的準確性探究

## 研究動機
對 LLM 的各種感官感興趣，先前 GPT-4o 釋出，讓 LLM 不只能讀文字 / 圖片，還具備了良好的聽覺感官。但根據我在業界的一些經驗，尤其是我在程曦（台灣客服外包龍頭公司）兼職軟體開發，主要做生成式 AI 相關應用的研究與開發的經驗而言，LLM 對於流程的處理仍然太過薄弱。自己用 LLM 嘗試過 SalesGPT 的做法，也有使用過 Google 釋出的 Agent Builder x DialogflowCX，所以我想利用這個想法做一個相關研究，研究如何讓 LLM 更好的處理複雜流程。探索要用什麼樣的流程輸入形式，才能確保 LLM 最好的了解流程內容，並遵守流程做出對應需求。

## 研究方法
我們有大量的客戶進線通話紀錄 (目前先模仿一份通話紀錄，再根據標準答案想呈現的流程做細微修改)，這些紀錄的通話主題主要為電商客服人員處理發貨/退貨。並有對應的發貨/退貨客服人員對答流程圖，我們要讓 LLM 檢查對話的客服人員是否依照流程進行。

具體操作為：
1. LLM 回復在哪裡的時候客服人員沒有照流程走，或是完全遵循流程。
2. 回復格式例如：4, 3.1, Pass，Pass 表示完全遵循流程，數字表示客服人員遵守到的流程節點。

### 五種流程圖比較
我們將比較五種不同的流程圖呈現方式給 LLM，觀察其回答的準確率：
1. 把流程圖換成虛擬碼 (例: if ... else if ... else) --> LLM 強大的生成/理解程式碼能力，對 if else 應有良好處理
2. 把流程圖轉成專門製圖的 Mermaid 語法 --> 經典的製圖語法，LLM 生成圖表多是使用此語法做轉換
3. 自然語言描述流程圖 (例: 首先，客服人員要 ...，然後要 ...，他這邊有可能可以選擇 ... 或是選擇 ...)
4. 使用可以識圖的 LLM (例: GPT-4o)，直接呈現流程圖片給 LLM
5. 將流程寫成 Excel 表 (第一層流程會在第一 Column，第二層流程會在第二 Column，一層流程可能會有分支，所以在不同 row 就是不同分支)

## 業界實際應用
1. 客服人員通話流程品質檢查
2. 智能流程機器人可以更好的依照流程對話

## 聯絡方式
如有任何問題，歡迎聯絡：
- 電子郵件: [justin.hsu.1019@gmail.com](mailto:justin.hsu.1019@gmail.com)
- LinkedIn: [https://linkedin.com/in/justinhsu101999](https://www.linkedin.com/in/justinhsu101999)

## License
This repository is licensed under the [MIT License](https://github.com/JustinHsu1019/LLM_Workflow_Research/blob/main/LICENSE).
