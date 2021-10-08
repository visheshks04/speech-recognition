import json

def create_jsons():
    data = []

    with open('data/captions_data.json', 'r') as f:
        captions_data = json.load(f)

    for event in captions_data['events']:
        sample = dict()
        sample["key"] = str(event['tStartMs']) + '.wav'
        sample["text"] = event['segs'][0]['utf8']
        data.append(sample)


    with open('data/dataset.json', 'w') as f:
        json.dump(data, f, indent=4)