import random

def anonymize_data(data):
    anonymized_data = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=len(data)))
    return anonymized_data