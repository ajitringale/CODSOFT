import random

def gameWin(comp, you):
    if comp == you:
        print("Match Tie")
    elif (comp=='s' and you=='r'):
        print("Congratulations, You Win... Rock beats Scissors") 
    elif(comp=='r' and you=='p'):
        print("Congratulations, You Win... Paper beats Rock")
    elif(comp=='p' and you=='s'):
        print("Congratulations, You Win... Scissors beat Paper")
    else:
        print("You Loss!!!")
   
print("Computer Turn : Rock(r) Paper(p) Scissors(s)")  
randNo = random.randint(1, 3)
if randNo==1:
    comp = 'r'
elif randNo==2:
    comp = 'p'
elif randNo==3:
    comp = 's'
    
you = input("Your Turn : Rock(r) Paper(p) Scissors(s) => ")
gameWin(comp, you)

print(f"Computer Choose {comp}")

