import os
from pytube import YouTube

urls = []

while Ture:
    url = input("유튜브 URL을 복사하세요. ('y'를 입력하면 다운로드 됩니다.): ")
    if url.lower() == 'y':
        break
    elif url.lower() == 'Y':
        break
    elif url.lower() == 'ㅛ':
        break
    urls.append(url)

for url in urls:
    try:
        yt = YouTube(url)
        filePath = yt.streams.filter(only_audio=True).first().download()
        mp3FilePath = filePath.replace('mp4', 'mp3')
        os.rename(filePath, mp3FilePath)
        print(f"Downloaded: {mp3FilePath}")
    except Exception as e:
        print(f"Error downloading video from {url}: {e}")