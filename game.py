import random
import emoji
print('===========================\n')
print('Welcome to the game \n')
print('===========================\n')
print(emoji.emojize('1. Rock :raised_fist:'))
print(emoji.emojize('2. Paper :hand_with_fingers_splayed:'))
print(emoji.emojize('3. Scissor :victory_hand:'))

us = int(input('\nSelect a number : '))
pc = random.randint(1,3)

print ('\nYou chose: ', us)
print ('CPU chose: ', pc)

if us == pc:
    print("\nIt's a Tie")
elif us == 1 and pc == 2:
    print('\nCPU won!')
elif us == 1 and pc == 3:
    print('\nYou won!')
elif us == 2 and pc == 1:
    print('\nYou won!')
elif us == 2 and pc == 3:
    print('\nCPU won!')
elif us == 3 and pc == 1:
    print('\nCPU won!')
elif us == 3 and pc == 2:
    print('\nYou won!')
else:
  print('\nError, try again ')
