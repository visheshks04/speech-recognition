from pytube import YouTube
import librosa
from scipy.io import wavfile


class AudioFetcher:

    def __init__(self, url):
        # 'https://youtu.be/HtSuA80QTyo'
        self.url = url

    def fetch(self, save_location):
        self.location = save_location
        yt = YouTube(self.url)
        print(f'Downloading {yt.title}')
        audio = yt.streams.get_by_itag(251)
        audio.download(save_location)

    def convert_to_wav(self, save_location):
        aud = librosa.load(self.location)
        wavfile.write(save_location, aud[1], aud[0])
