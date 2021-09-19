import random
import string

print("hello, Welcome to random password generator")

length = int(input("\nEnter the length of the password you need : "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

#one method of generating password
i = 0
while i <= length:
    new = random.choice(all)
    print(new,end="")
    i += 1
print()
#another method
temp = random.sample(all, length)
#random.sample will never repeat the letter again

#output is in list so we use "".join()
password = "".join(temp)
print(password)

