import requests
import os

scan ='y'

def determine(scan):
  while True:
    if scan == 'y':
      break
    elif scan == 'n':
      print("k. bye")
      exit(0)
    else:
      print("That's not vaild answer")
      print("Do you want to start over? y/n", end =" ")
      scan = input()

def repeat():
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLS you want to check. (separated by comma)")

  user = list(map(str,input().split(',')))

  for x in range(len(user)):
    user[x] = user[x].replace(" ","")
  return user

def result(user):
  try:
    for x in range(len(user)):
      tmp = requests.get(f"{user[x]}")
      if tmp.status_code == 200:
        print(f"{user[x]} is up!")
      
  except:
    print(f"{user[x]} is down!")
    requests.exceptions.ConnectionError
  return user

while scan != 'n':
  user = repeat()
  for x in range(len(user)):

    if ".com" not in user[x]:
      print(f"{user[x]} is not vaild URL.")
      print("Do you want to start over? y/n", end =" ")
      scan = input()
      determine(scan)
      
    elif "http://" not in user[x]:
      user[x] = "http://" + user[x]
      user[x] = user[x].lower()
      
  user = result(user)
  print("Do you want to start over? y/n", end =" ")
  scan = input()

  determine(scan)
  