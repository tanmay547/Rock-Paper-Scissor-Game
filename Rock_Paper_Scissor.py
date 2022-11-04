import random
l = ["Rock","Paper","Scissor"]

while True:
    ccount=0
    ucount=0
    uchoice = int(input('''

Game Start.....
1 Yes
2 No | Exit
'''
    ))

    if uchoice==1:
        for a in range(1,6):
            userinput=int(input('''
1 Rock
2 Paper
3 Scissor          
                '''))
            if userinput==1:
                uchoice="Rock"
            elif userinput==2:
                uchoice=="Paper"
            elif userinput==3:
                uchoice=="Scissor"
            cchoice=random.choice(l)
            if cchoice==uchoice:
                print("Comuter Vaule",cchoice)
                print("Your Choice",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif(uchoice=="Rock"and cchoice=="Scissor") or(uchoice=="Paper" and cchoice=="Rock") or (uchoice=="Scissor" and cchoice=="Paper "):
                print("Computer Value",cchoice)
                print(("Your Choice",uchoice))
                print("You Win")
                ucount=ucount+1
                ccount=ccount+1
            else:
                print("Comuter Vaule",cchoice)
                print("Your Choice",uchoice)
                print("Computer Win ")
                ccount=ccount+1



    else:
        break
