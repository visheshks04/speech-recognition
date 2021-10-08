import requests
import json


class CaptionFetcher:

    def __init__(self, url):
        # https://www.youtube.com/api/timedtext?v=HtSuA80QTyo&asr_langs=de%2Cen%2Ces%2Cfr%2Cid%2Cit%2Cja%2Cko%2Cnl%2Cpt%2Cru%2Ctr%2Cvi&caps=asr&exp=xftt%2Cxctw&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1631187357&sparams=ip%2Cipbits%2Cexpire%2Cv%2Casr_langs%2Ccaps%2Cexp%2Cxoaf&signature=8D60161D31A8301B3B8524EFD3F22E5D4E66957A.2BF728B067CB1EA262D8FCF9E898F109FBE0A69B&key=yt8&lang=en&fmt=json3&xorb=2&xobt=3&xovt=3

        self.url = url


    def fetch(self, save_location):

        captions_json = requests.get(self.url)
        self._clean_data(captions_json.text)
        with open(save_location, "w") as file:
            file.write(captions_json.text)

    def _clean_data(self, save_location):

        with open(save_location, 'r') as f:
            data = json.load(f)

        for event in data['events']:
            sentence = event['segs'][0]['utf8']
            sentence = sentence.replace('\n', ' ')
            sentence = self._remove_caps(sentence)
            sentence = self._remove_special_chars(sentence)
            event['segs'][0]['utf8'] = sentence

        with open(save_location, 'w') as f:
            json.dump(data, f)


    def _remove_caps(string):
        string = string.split()
        for word in string:
            if(word.isupper()):
                string.remove(word)
        string = " ".join(string)
        return string

    def _remove_special_chars(string):

        removables = ['.', ',', ';', '"', '\'', ':', '<', '>', '?', '/', '\\', '[', ']', '{', '}', '-', '_', '+', '=', '(', ')', '!', '@', '#', '$', '%', '^', '&', '*', '~', '`']
    
        string = list(string)

        for ch in string:
            if ch in removables:
                string.remove(ch)

        string = "".join(string)	