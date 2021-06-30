import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_mel_spect(path):
    y, sr = librosa.load(path)
    return librosa.feature.melspectrogram(y, sr)

def insert_spect_col(df):
    '''
    Inserts another column in df with corresponding Mel Spectograms
    '''
    spects = pd.Series([])
    for path in df['path']:
        path = 'clips/' + path
        spect = get_mel_spect(path)
        spects = spects.append(pd.Series([spect]), ignore_index = True)

    new_df = pd.concat([df, spects], axis = 1)
    new_cols = list(new_df.columns)
    new_cols[-1] = 'mel'
    new_df.columns = new_cols
    return new_df