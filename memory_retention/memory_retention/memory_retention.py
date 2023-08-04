class MemoryRetention:
    def __init__(self):
        self.memory = {}

    def remember_interaction(self, user_id, interaction):
        if user_id not in self.memory:
            self.memory[user_id] = []
        self.memory[user_id].append(interaction)

    def get_user_interactions(self, user_id):
        if user_id in self.memory:
            return self.memory[user_id]
        else:
            return []