import random
import secrets

def rand():
    return random.randint(0, 100)


def generate_password():
    return secrets.token_urlsafe(16)