class ConversationManager:
    def __init__(self):
        self.context = {}

    def start_conversation(self):
        self.context = {}

    def end_conversation(self):
        self.context = {}

    def remember_context(self, key, value):
        self.context[key] = value

    def get_context(self):
        return self.context

    def clear_context(self):
        self.context = {}
