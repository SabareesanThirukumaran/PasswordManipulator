#importing os + time
import os, time

#timing commands
sleep = ["..."]

#Username input
username = str(input('What is your Username ?: '))
for i in sleep:
  print(i)
time.sleep(0.5)
os.system("clear")

#Password input
password = str(input('What is your Password ?: '))
for i in sleep:
  print(i)
time.sleep(0.5)
os.system("clear")

#password manipulation
password_length = len(password)
hidden_password = password_length * "*"

#last statement
print(f"Hi {username}, your password {hidden_password} is {password_length} letters long.")