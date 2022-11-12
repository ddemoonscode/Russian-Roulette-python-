#imports
import random, os

#menu
def menu():
    print('Enter to shoot')

print()
menu()
option = input('')
print()

while option !=0:
    #number generating & Testing
    if random.randint(1, 6) == 1:
        print('YOU ARE DEAD')
        print('==========')
        print()
        #if dead -> Exit
        exit()

    else:
        print('YOU ARE LUCKY')
        print('==========')

    #stop loop
    print()
    menu()
    option = input('')
    print()