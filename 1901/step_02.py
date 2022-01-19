import random

psw = ''
for x in range(12):
    psw = psw + random.choice(list('1234567890qwertyuiopQWERTYUIOP'))
print(psw)
