import random
import string
import random
import time

digits = '0123456789'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = None
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_random_number(length):
    digits = "0123456789"
    random_number = None
    random_number = int(''.join(random.choice(digits) for i in range(length)))
    return random_number

def get_random_email():
    return str(f"orechov18_{time.time()}@anypost.org")

def get_random_name():
    return str(f"orechov18_{time.time()}")

def get_random_password():
    password = ''
    for i in range(random.randrange(8, 16)):
        password += random.choice(digits + uppercase + lowercase + punctuation)
    return password