from random import randint
import json

useragents = []

with open('./useragent/useragents.json') as f:
    useragents = json.loads(f.read())

def getRandomUseragent():
    useragent = useragents[randint(0, len(useragents)-1)]
    if 100 * float(useragent['percent'].replace('%', '')) > 100/2:
        return useragent['useragent']
    else:
        return getRandomUseragent()