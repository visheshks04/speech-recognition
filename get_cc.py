import requests
import json


class CaptionFetcher:

    removables = ['.', ',', ';', '"', '\'', ':', '<', '>', '?', '/', '\\', '[', ']', '{', '}', '-', '_', '+', '=', '(', ')', '!', '@', '#', '$', '%', '^', '&', '*', '~', '`']

    def __init__(self, url):
        # https://www.youtube.com/api/timedtext?v=HtSuA80QTyo&asr_langs=de%2Cen%2Ces%2Cfr%2Cid%2Cit%2Cja%2Cko%2Cnl%2Cpt%2Cru%2Ctr%2Cvi&caps=asr&exp=xftt%2Cxctw&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1631187357&sparams=ip%2Cipbits%2Cexpire%2Cv%2Casr_langs%2Ccaps%2Cexp%2Cxoaf&signature=8D60161D31A8301B3B8524EFD3F22E5D4E66957A.2BF728B067CB1EA262D8FCF9E898F109FBE0A69B&key=yt8&lang=en&fmt=json3&xorb=2&xobt=3&xovt=3

        self.url = url

    def fetch(self, save_location):

        captions_json = requests.get(self.url)
        self._clean_data(captions_json.text)
        with open(save_location, "w") as file:
            file.write(captions_json.text)

    def _clean_data(self, captions_dict):
        print(captions_dict)

    def _remove_caps(str):
        str = str.split()
        for word in str:
            if(word.isupper()):
                str.remove(word)
        str = " ".join(str)
        return str

    def remove_special_chars(self, save_location):
        pass