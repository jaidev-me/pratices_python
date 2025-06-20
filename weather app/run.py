from Weather import *

while True:
    try:
        choice = input(
            '''
                  *********Weather App**********

              =======> Type (1) to Enter your city
              =======> Type (2) for automatic detection
              =======> Type (0) to exit
              =======> Enter your choice: ''')
        try:
            choice = int(choice)
            if choice > 2 or choice < 0:
                print("\n   (>_<) Invalid choice")
            else:
                pass
            if choice == 0:
                break
            elif choice == 1:
                weather(City())
            else:
                weather(ip())
        except:
            print("\n   (>_<) Invalid choice. Type only integers")

    except:
        pass
print("\n    (ง •_•)ง Thanks for choosing our weather app\n")
