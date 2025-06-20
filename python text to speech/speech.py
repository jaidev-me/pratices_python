import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

user = input("\nWhat's your name dear: ")
print(f"\nHello {user}")
speaker.Speak(f"Hello {user}")

names = []

while True:
 name = input("\nEnter a name whome you want to give shoutout: ")
 names.append(name)
 choice = input(f'''\nName of {name} was added to shoutout list\n\n\nType (1) if you want to add more names\nType anything if you want to give shoutouts\n''')
 try:
  if (int(choice) == 1):
   pass
 except:
  for name in names:
   print(f"\nA big Shoutout to {name}")
   speaker.Speak(f"A big shoutout to {name}")
  choice = input(f"\nShoutouts done!\n\nType zero (0) for EXIT\nType anything to continue\n")
  try:
   if int(choice) == 0:
    break
  except:
   names.clear()
print(f"\nHave a nice day {user}")   
speaker.Speak(f"Have a nice day {user}, See you later!") 