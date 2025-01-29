from yt_dlp import YoutubeDL

def download_tiktok_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Insira o link do TikTok: ")
    download_tiktok_video(video_url)