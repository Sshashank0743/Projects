import random

print("Welcome to the password generator!")

chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?,./<>;:[]{}|"

num = int(input("How many passwords would you like to generate? "))

length = int(input("How long would you like your passwords to be? "))

print("\nHere are your passwords: ")

for pwd in range(num):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

