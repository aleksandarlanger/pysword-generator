import random
import string

password = []
nums = int(input("How many numbers do you want to have?: "))
password.extend(random.choices(string.digits, k=nums))

uletter = int(input("How many upper letters do you want to have: "))
password.extend(random.choices(string.ascii_uppercase, k=uletter))

loletter = int(input("How many lower letters do you want to have?: "))
password.extend(random.choices(string.ascii_lowercase, k=loletter))
#
symb = int(input("How many symbols do you want to have?: "))
password.extend(random.choices(string.punctuation, k=symb))
#
random.shuffle(password)

secured_pass = ""

for c in password:
    secured_pass += c

print(f"Your password is: {secured_pass}")
