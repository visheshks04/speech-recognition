import json

def create_jsons(captions_data_path, dataset_path):
    data = []

    with open(captions_data_path, 'r') as f:
        captions_data = json.load(f)

    for event in captions_data['events']:
        sample = dict()
        sample["key"] = str(event['tStartMs']) + '.wav'
        sample["text"] = event['segs'][0]['utf8']
        data.append(sample)


    with open(dataset_path, 'w') as f:
        json.dump(data, f, indent=4)
