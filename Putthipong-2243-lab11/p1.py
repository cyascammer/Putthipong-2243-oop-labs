#Putthipong Phukhansung 633040224-3
"""
Generate a strong password that contains at least one uppercase letter, one lowercase letter, one digit, one special character and the string length must be 9
"""
import random
import string


characters = string.ascii_letters + string.digits + string.punctuation
pwd1 = random.choice(string.ascii_uppercase)
pwd2 = random.choice(string.ascii_lowercase)
pwd3 = random.choice(string.digits)
pwd4 = random.choice(string.punctuation)
pwd = ''.join(pwd1 + pwd2 + pwd3 + pwd4)


password = ''.join((pwd) for i in range(1))
password1 = ''.join(random.choice(string.ascii_letters) for i in range(5))
print("Random password is: ", password + password1)