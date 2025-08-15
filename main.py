from interface import *
from functions import *

header('PASSWORD GENERATOR')
header('Welcome.')

quantity, size = get_password()
password_gen(quantity, size)

header('Exiting...')