# 🤖 Discord 情緒分析機器人

本專案是一個使用 Python 建立的 Discord 聊天機器人，能夠即時分析用戶輸入文字的情緒（正面 / 中性 / 負面），並回覆信心度。情緒分析模型來自 Hugging Face 的 [`cardiffnlp/twitter-roberta-base-sentiment`](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)。

---

## 📌 功能簡介

- 使用 `!mood <句子>` 指令分析情緒。
- 採用 Hugging Face 的預訓練模型進行情緒分類。
- 回覆情緒判斷結果與信心度。
- 運作於 Discord 頻道，即時互動。

---

## 📄 文件說明

- `discord_mood_bot.py`：主程式碼，包含 Discord bot 初始化與情緒分析邏輯。
- `.env`（需自行建立）：環境變數配置檔，格式如下：

```env
DISCORD_TOKEN=你的 Discord Bot Token
HF_API_TOKEN=你的 Hugging Face API Token

