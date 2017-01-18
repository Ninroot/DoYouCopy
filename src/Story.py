import json
import random
import re

from pprint import pprint
from urllib.request import urlopen

import time
import sys

from src.Message import Message


class Story:
    def __init__(self, path=''):
        self.path = path
        self.choice = None
        self.location_id = 0

    # http://stackoverflow.com/questions/7160737/python-how-to-validate-a-url-in-python-malformed-or-not
    def isUrl(self):
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if regex.match(self.path):
            return True
        return False

    def evaluate(self, responses):
        while True:
            self.choice = input('> ')
            try:
                self.choice = int(self.choice)
                reponse_id = responses[self.choice]['id']
            except Exception:  #  TODO better with ValueError
                print("This response does not actually exist, please select a correct response.")
                continue
            break
        self.location_id = reponse_id

    # Return the response id corresponding of the evaluation
    def getNextId(self, responses):
        while True:
            try:
                id = responses[self.choice]['id']
                print(id)
            except Exception:
                print("This message does not actually exist")
                continue
            break
        return id

    def print_slowly(self, string, slow_coef=0):
        for letter in string:
            print('{}'.format(letter), end='')
            sys.stdout.flush()
            time.sleep(slow_coef)

    def start(self):
        if self.isUrl():
            file = urlopen(self.path)
        else:
            file = open(self.path, 'r')

        story = json.load(file)
        # pprint(message)
        while True:
            try:
                message = Message(story['messages'][self.location_id])
            except Exception:
                print('This message does not exist')
            print('<{}> '.format(message.author), end='')
            print('{}'.format(message.content))
            x = 0;
            for response in message.responses:
                print(str(x) + ': ' + response['content'])
                x += 1
            self.evaluate(message.responses)