from memory_retention import MemoryRetention

memory = MemoryRetention()

# Example usage
user_id = '123'
interaction1 = 'Hello, how can I help you?'
interaction2 = 'I would like to know the weather for tomorrow.'

memory.remember_interaction(user_id, interaction1)
memory.remember_interaction(user_id, interaction2)

user_interactions = memory.get_user_interactions(user_id)

for interaction in user_interactions:
    print(interaction)