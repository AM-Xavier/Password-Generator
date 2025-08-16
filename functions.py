from interface import *
import string
import random
from time import sleep
import os
import sys
import csv

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
    while True:
        p_quantity = checkInterger('How many passwords: ')
        p_size = checkInterger('How many characters: ')
    
        if (p_quantity == 0 or p_size == 0):
            print("\033[0;31;47mERROR! Enter a number greater than zero!\033[m")
            continue
        
        else:
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

def save(passwords):
    while True:
        saving = input('Would you like to save the generated password(s), inside of a CSV file?\b [Y]es or [N]o: ')
        
        if saving.lower().startswith  ('y'):
            line()
            print('Saving your passwords...')
            sleep(1)
            with open('passwords.csv', 'w', encoding='utf-8') as file:
                file.write('Password\n')
                for p in passwords:
                    file.write(p + '\n')
            print('Passwords saved in password.csv')
            
        else:
            print('Passwords were not saved.')
            break

def main():
    while True:
        generate = input('Do you wish to generate a password? [Y]es or [N]o: ')

        if generate.lower().startswith('y'):
            quantity, size = get_password()
            passwords = password_gen(quantity, size)
            line()
            save(passwords)
            sleep(1)
    
        if generate.lower().startswith('n'):
            sleep(1)
            header('Exiting...')
            sleep(2)
            break
    
        else:
            print("\033[0;31;47mERROR! Enter only [Y]es or [N]o!\033[m")
            continue