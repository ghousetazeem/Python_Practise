print('welcome to password generaor by sarfaraZ!')
import random
import  string
letters = string.ascii_letters
numbers = string.digits
spl_char = string.punctuation
num_letter = int(input("how many letters you want in your pass ? \n"))
num_symbols = int(input("how many symbol you want in your pass ? \n"))
num_numbers = int(input("how many numbers you want in your pass ? \n"))

password_list = []

for char in range(1,num_letter+1):
  password_list += random.choice(letters)

for char in range(1, num_symbols + 1):
  password_list += random.choice(spl_char)

for char in range(1,num_numbers+1):
  password_list+= random.choice(numbers)


random.shuffle(password_list)# it shuffle the pass
#print(password_list)
password = ''
for char in password_list :
    password+=char
print(f"your pass is {password}")
