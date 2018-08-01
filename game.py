player1=input()
player2=input()
levels=int(input())
player1goals=0
player2goals=0
for i in range(0,levels):
    choice=input().split()
    player1choice=choice[0].upper()
    player2choice=choice[1].upper()
    if player1choice==player2choice:
        continue
    if player1choice=="S":
        if player2choice=="K":
            player2goals+=1
        elif player2choice=="Q":
            player1goals+=1
    elif player1choice=="K":
        if player2choice=="S":
            player1goals+=1
        elif player2choice=="Q":
            player2goals+=1
    elif player1choice=="Q":
        if player2choice=="K":
            player1goals+=1 
        elif player2choice=="S":
            player2goals+=1
if player1goals>player2goals:
    print("{} wins!".format(player1))
elif player2goals>player1goals:
    print("{} wins!".format(player2))
else:
    print("Draw!")


