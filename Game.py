from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks=[]
left_stack=Stack("Left")
middle_stack=Stack("Middle")
right_stack=Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)


# Pre Setup for the Game

num_disks=0
while num_disks < 3:
  num_disks= int(input("\nHow many disks do you want to play with?\nThere should be atleast 3 disks\n"))

for x in range(num_disks,0,-1):
  left_stack.push(x)

num_optimal_moves= 2**num_disks - 1

print("\nThe fastest you can solve this game is is {0} moves".format(num_optimal_moves))


# Handling User Input

def get_input():
  choices = [ element.get_name()[0] for element in stacks]
  while True:
    for i in stacks:
      print("{name}: Enter {letter}".format(name=i.get_name(),letter=i.get_name()[0]))
    user_input=input("")
    if user_input in choices:
      for i in range(len(choices)):
        if user_input == choices[i]:
          return stacks[i]


# Game Logic

num_user_moves=0
while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for element in stacks:
    element.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack=get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack=get_input()
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again")
    elif to_stack.is_empty() or from_stack.peek()<to_stack.peek():
      disk=from_stack.pop()
      to_stack.push(disk)
      num_user_moves+=1
      break
    else:
      print("\n\nInvalid Move. Cannot move Larger Disk onto a Smaller Disk")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves,num_optimal_moves))
