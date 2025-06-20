import random

def win(comp_choice, user_choice):
    if (comp_choice == user_choice):
        return "It's a draw"
    elif (comp_choice == choices[0] and user_choice == choices[1]) or (comp_choice == choices[1] and user_choice == choices[2]) or  (comp_choice == choices[2] and user_choice == choices[0]):
        return 'Ohh! You lose'
    else:
        return 'Congrats You Won!'
        
choices = ['Gun', 'Snake', 'Water']
user_choice = input(f'What do you want to choose?\n1.{choices[0]} 2.{choices[1]} 3.{choices[2]}\n')
try: 
    if (1 > int(user_choice)) or (3 < int(user_choice)):
      exit("Please type a valid choice")
    else:
      user_choice = choices[int(user_choice) - 1]
except:
     user_choice = user_choice.capitalize()
     if (user_choice not in choices):
         exit("Please type a valid choice") 
     else:
         pass
     
comp_choice = random.choice(choices)

print(f"Your choice is {user_choice}")
print(f"My choice is {comp_choice}")
print('''
''', win(comp_choice, user_choice))