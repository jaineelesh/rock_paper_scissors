from resource import rps
from random import randint

choice = int(input('''
What do you choose:
0 - rock
1 - paper
2 - scrissors
'''))

computer = randint(0, 2)

# display:
print("Your choice")
print(rps[choice])

print("Computer's choice")
print(rps[computer])

if choice == computer:
    print("it is a draw")
elif (choice == 0 and computer == 1) or (choice == 1 and computer == 2) or (choice == 2 and computer == 0):
    print("Computer wins!!")
else:
    print("YOU WIN!!!")
