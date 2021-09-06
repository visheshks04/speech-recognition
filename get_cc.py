import requests
import json

url = "https://www.youtube.com/api/timedtext?v=HtSuA80QTyo&asr_langs=de%2Cen%2Ces%2Cfr%2Cid%2Cit%2Cja%2Cko%2Cnl%2Cpt%2Cru%2Ctr%2Cvi&caps=asr&exp=xftt%2Cxctw&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1630915878&sparams=ip%2Cipbits%2Cexpire%2Cv%2Casr_langs%2Ccaps%2Cexp%2Cxoaf&signature=9D36F5E4A41A7687A02726A404C1EA398FAC1707.07C232BA6BC40389A83CDB47A624FC9006CDD028&key=yt8&lang=en&fmt=json3&xorb=2&xobt=3&xovt=3"

captions_json = requests.get(url)

with open("SpeechRecognition/data/captions_data.json", "w") as file:
    file.write(captions_json.text)

data = json.load(open("SpeechRecognition/data/captions_data.json", "r+"))
