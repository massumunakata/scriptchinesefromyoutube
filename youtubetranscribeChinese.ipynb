#googleColabo
!pip install -U yt-dlp
!pip install -U git+https://github.com/openai/whisper.git
!apt install ffmpeg -y

import yt_dlp
import os
import whisper
model = whisper.load_model("small")

query = "" #@param {type:"string"}
youtube_urls_input =query
youtube_urls = youtube_urls_input.strip().split()

for i, url in enumerate(youtube_urls):
print(f"\n🎬 処理中の動画 {i+1}: {url}")

# ファイル名を動画ごとにユニークに
output_filename = f"audio_{i}.mp3"

# ダウンロード設定
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'downloaded_{i}.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': True
}

# 音声ダウンロード
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
        ydl.download([url])
    except Exception as e:
        print(f"⚠️ ダウンロード失敗: {e}")
        continue

# Whisperで文字起こし（中国語指定）
try:
    result = model.transcribe(f"/content/downloaded_{i}.mp3", language="zh")
    print("📝 認識されたテキスト:")
    print(result["text"])
except Exception as e:
    print(f"⚠️ 文字起こし失敗: {e}")