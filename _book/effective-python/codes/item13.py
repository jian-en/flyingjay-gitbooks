import json

def load_json_key(data, key):
    try:
        result_dict = json.loads(data)
    except ValueError as e:
        raise KeyError from e
    else:
        print('hello')
        return result_dict[key]

load_json_key('{"hell": "worl}', 'hello')
