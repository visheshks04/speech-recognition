from numpy.core.defchararray import encode
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

label_encodes = {
                ' ': 0, 
                'a': 1,
                'b': 2,
                'c': 3,
                'd': 4,
                'e': 5,
                'f': 6,
                'g': 7,
                'h': 8,
                'i': 9,
                'j': 10,
                'k': 11,
                'l': 12,
                'm': 13,
                'n': 14,
                'o': 15,
                'p': 16,
                'q': 17,
                'r': 18,
                's': 19,
                't': 20,
                'u': 21,
                'v': 22,
                'w': 23,
                'x': 24,
                'y': 25,
                'z': 26
}

def get_encoded_sentence(sentence):
        '''
        Returns an encoded version of param sentence according to the label_encodes
        '''
        encoded = []
        for ch in list(sentence.lower()):
            encoded.append(label_encodes[ch])

        encoded = np.array(encoded)
        return encoded

def insert_spect_col(df):
    '''
    Inserts another column in df with encoded sentence
    '''
    encoded_sentences = pd.Series([])
    for sentence in df['sentence']:
        encode = get_encoded_sentence(sentence)
        encoded_sentences.append(pd.Series([encode]))

    new_df = pd.concat([df, encoded_sentences], axis = 1)
    new_cols = list(new_df.columns)
    new_cols[-1] = 'encoded_sentences'
    new_df.columns = new_cols
    return new_df