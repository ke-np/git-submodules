import random
import re
import secrets

def rand():
    return random.randint(0, 100)


def generate_password():
    return secrets.token_urlsafe(16)


def sanitize_string(string):
    return re.sub(r'\s{2,}', ' ', string.strip())