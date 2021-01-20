import string as s
from random import *
ch = s.ascii_letters + s.digits + s.punctuation
password = "".join(choice(ch)for c in range (randint(8,16)))
print(password)
