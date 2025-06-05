import discord
import requests
import os

# ==== TOKEN設定 ====
from dotenv import load_dotenv

load_dotenv()  # 讀取 .env 檔案
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

# === Discord Bot 初始化 ===
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

# === Hugging face API ====
HF_API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
# analyze
def decode_label(label):
    mapping = {
        "LABEL_0": "負面",
        "LABEL_1": "中性",
        "LABEL_2": "正面"
    }
    return mapping.get(label, label)

def analyze_emotion_hf(text):
    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}"
    }
    payload = {"inputs": text}
    try:
        response = requests.post(HF_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, dict) and "error" in result:
            return f"❗ API 回傳錯誤：{result['error']}"

        best = max(result[0], key=lambda x: x['score'])
        label = decode_label(best['label'])
        score = best['score']
        return f"情緒判斷：{label}（信心度：{score:.2f}）"

    except Exception as e:
        return f"❗ 發生錯誤：{str(e)}"


@bot.event
async def on_ready():
    print(f"✅ Bot 已上線：{bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user_input = message.content.strip()
    if user_input.startswith("!mood "):
        text = user_input[len("!mood "):]
        await message.channel.send("🔍 分析中，請稍候...")
        analysis = analyze_emotion_hf(text)
        await message.channel.send(f"🧠 分析結果：\n{analysis}")

bot.run(DISCORD_TOKEN)
