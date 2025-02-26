
import pandas
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
passwordlist =[]
print("Welcome to the PyPassword Generator!")
n_l= int(input("How many letters would you like in your password?\n"))
n_s = int(input(f"How many symbols would you like?\n"))
numb = int(input(f"How many numbers would you like?\n"))
# x is for the letters
# y is for the symbols
# z is for the numbers

# number of letters
for x in range(1,n_l+1):
    x = random.choice(letters)
    passwordlist.append(x)
# number of symbols
for y in range(1,n_s+1):
    y = random.choice(symbols)
    passwordlist.append(y)
#number of numbers
for z in range(1,numb+1):
    z = random.choice(numbers)
    passwordlist.append(z)

# shuffle the password
random.shuffle(passwordlist)
password =''.join(passwordlist)
print(password)
save = input('Do you want to save the password?(y/n)')
if save == 'y':
    pandas.
