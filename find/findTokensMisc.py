import json

def locateTokens(getJson):
    data = {
        'attempted': False
    }

    if getJson:
        return json.dumps(data)
    else:
        return data