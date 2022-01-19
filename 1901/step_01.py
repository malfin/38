import random

str1 = '1234567890'
str2 = 'qwertyuiop'
str3 = str2.upper()
str4 = str1 + str2 + str3

ls = list(str4)

random.shuffle(ls)

psw = ''.join([random.choice(ls) for x in range(12)])

print('password random:', psw)
print('random.choice:', random.choice(ls))
