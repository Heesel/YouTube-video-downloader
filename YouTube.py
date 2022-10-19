from pytube import YouTube
from pytube.cli import on_progress

#param url: string -> The YouTube url
#param option: int -> The option to choose video or audio
#param path: string -> The chosen path where to save the file

def download_youtube(url, option, path):
    color = '\033[38;2;255;00;255m'
    reset_color = '\033[39m'

    yt = YouTube(url, on_progress_callback=on_progress)

    if option == 1:
        yt.streams.get_highest_resolution().download(path)
    elif option == 2:
        yt.streams.get_audio_only().download(path)
    elif option != 1 or option != 2:
        print('Invalid option' + reset_color)
        return

    print(f'\n' + color + 'Downloading: ', yt.title, '~ viewed', yt.views, 
    'times.')

    print(f'\nFinished downloading:  {yt.title}' + reset_color)

try:
    link = input("Enter the link of YouTube video you want to download:  ")
    path = input("Enter the path where you want to save the file: ")
    opt = int(input("Press 1 to download the video or 2 to download the audio: "))
    download_youtube(link, opt, path)
except Exception as e:
    print(e)






