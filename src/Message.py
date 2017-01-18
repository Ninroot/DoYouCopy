class Message:
    def __init__(self):
        self.id = None
        self.author = None
        self.content = None
        self.delay = None

    def __init__(self, dico):
        try:
            self.author = str(dico['author'])  # why not message.author ?
        except Exception:
            self.author = '?'
        try:
            self.responses = dico['responses']  # why not message.author ?
        except Exception:
            self.responses = None
        try:
            self.content = dico['content']
        except Exception:
            self.content = '???'
        self.id = None
        self.delay = None