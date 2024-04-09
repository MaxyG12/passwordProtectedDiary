from replit import db
import datetime
import random

print("Private Diary")
print()

def add():
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[timestamp] = entry

def view():
  keys = db.keys()
  entryList = list(keys)
  entryList.sort(reverse=True)
  for key in entryList:
      entry = db[key]
      if 'password' in entry:
          del entry['password']
      if 'salt' in entry:
          del entry['salt']

      print(f"{key}: {entry}")
      print()
      next_action = input("Next or exit? > ")
      if next_action.lower() == "exit":
          break

            
def createUser():
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  while True: 
    salt = random.randint(1000,9999)
    newPassword = f"{password}{salt}"
    newPassword = hash(newPassword)
    db[username] = {"password": newPassword, "salt": salt}
    break

def login():
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  salt = db[username]["salt"]
  oldPassword = f"{password}{salt}"
  oldPassword = hash(oldPassword)
  if oldPassword == db[username]["password"]:
    print("\nLogin successful")
    diary()
  else:
    print("\nLogin failed, try again")
    login()
    
def diary():
  while True:
    print()
    print("1: Add")
    print("2: View")
    print("3: Exit")
    print()
    menu = input("> ")
    if menu == "1":
      add()
    elif menu == "2":
      view()
    elif menu == "3":
      break
    else:
      print("Invalid input")

while True:
  print()
  print("1. Add User")
  print("2. Login")
  print("3. Exit")
  choice = input("Enter your choice: ")
  if choice == "1":
    createUser()

  elif choice == "2": 
    login()
  else: 
    print("Goodbye")