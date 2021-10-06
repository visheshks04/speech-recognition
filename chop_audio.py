from scipy.io import wavfile
import json

class AudioChopper:

    def __init__(self, wav_location, save_location, time_stamps):
        self.location = wav_location
        self.save_location = save_location
        self.time_stamps_location = time_stamps_location



    def chop(self):
        with open('data/captions_data.json', 'r') as f:
            data = json.load(f)

        print(data)