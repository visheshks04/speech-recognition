from scipy.io import wavfile
import json
import librosa

class AudioChopper:

    def __init__(self, wav_location, save_location, time_stamps_location):
        self.location = wav_location
        self.save_location = save_location
        self.time_stamps_location = time_stamps_location

    def chop(self):

        with open(self.time_stamps_location, 'r') as f:
            data = json.load(f)

        aud = librosa.load(self.location)
        
        for event in data['events']:
            start_index = event['tStartMs'] * 1e-3 * aud[1]
            end_index = (event['tStartMs'] + event['dDurationMs']) * 1e-3 * aud[1]

            start_index, end_index = int(start_index), int(end_index)

            chopped_sample = aud[0][start_index:end_index]
            wavfile.write(str(self.save_location)+'{}.wav'.format(event['tStartMs']), aud[1], chopped_sample)
