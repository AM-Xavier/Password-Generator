from interface import *
import string
import random
from time import sleep

def checkInterger(interger):
    while True:
        try:
            interger = int(input(interger))
        except (ValueError, TypeError):
            print("\033[0;31;47mERROR! Enter only intergers!\033[m")
            continue
        else:
            return interger

def get_password():
    p_quantity = checkInterger('How many passwords: ')
    p_size = checkInterger('How many characters: ')
    
    return p_quantity, p_size

def password_gen(p_quantity, p_size):
    header('Generating your password.')
    header('Please, wait a moment.')
    sleep(3)
    
    possibilities = string.ascii_letters + string.punctuation + string.digits

    passwords = [] 
    
    for _ in range(0, p_quantity):
        password = ''
        for _ in range(0, p_size):
            password += random.choice(possibilities)
        passwords.append(password)
        
    for pword in passwords:
        print(pword)
    
    sleep(1)