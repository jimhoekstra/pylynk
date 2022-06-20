import requests
import json
import os


LYNK_HOST_URL = 'https://www.lynkdataplatform.com'


class DataType:

    def __init__(self, id, relations={}):
        self.id = id
        self.relations = {
            k.removeprefix('https://').split('/', maxsplit=1)[1]: 
            v.removeprefix('https://').split('/', maxsplit=1)[1] 
                for k, v in relations.items()
        }

    def print_relations(self):
        print(json.dumps(self.relations, indent=4))

    def __getitem__(self, key):
        return self.relations[key]

    @classmethod
    def all(cls):
        url = LYNK_HOST_URL + '/r/t/' + cls.data_type
        response = requests.get(url, headers={'Authorization': 'Token ' + os.environ['LYNK_API_TOKEN']})
        response.raise_for_status()
        json_response = response.json()
        return [cls(k, v) for k, v in json_response.items()]

    @classmethod
    def new(cls, id, dataset):
        url = LYNK_HOST_URL + '/r/t/' + cls.data_type
        data = {'id': id, 'dataset': dataset}
        response = requests.post(url, headers={'Authorization': 'Token ' + os.environ['LYNK_API_TOKEN']}, data=json.dumps(data))
        response.raise_for_status()
        json_response = response.json()
        return cls(json_response['id'])
    
    def __str__(self):
        return '<' + self.__class__.__name__ + ': ' + self.id + '>'
