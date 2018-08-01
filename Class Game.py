class RPSGame(object):
    def __init__(self, level, p1, p2):
        self.player2 = p2
        self.player1 = p1
        self.levels = level
        self.player1goals = 0
        self.player2goals = 0

    def turn(self):
        choice = input().split()
        player1choice = choice[0].upper()
        player2choice = choice[1].upper()
        self.set_goals(player1choice, player2choice)

    def play(self):
        for i in range(0, self.levels):
            self.turn()
        self.judge()

    def set_goals(self, player1choice, player2choice):
        if player1choice == "S":
            if player2choice == "K":
                # paper covers rock
                self.player2goals += 1
            elif player2choice == "Q":
                # rock crushes scissors
                self.player1goals += 1
        elif player1choice == "K":
            if player2choice == "S":
                # paper covers rock
                self.player1goals += 1
            elif player2choice == "Q":
                # scissors cuts paper
                self.player2goals += 1
        elif player1choice == "Q":
            if player2choice == "K":
                # scissors cuts paper
                self.player1goals += 1
            elif player2choice == "S":
                # rock crushes scissors
                self.player2goals += 1

    def judge(self):
        if self.player1goals > self.player2goals:
            self.victory_message(self.player1)
        elif self.player2goals > self.player1goals:
            self.victory_message(self.player2)
        else:
            print("Draw!")

    @staticmethod
    def victory_message(player):
        print("{} wins!".format(player))
    

pl1 = input()
pl2 = input()
Lev = int(input())
game = RPSGame(Lev, pl1, pl2)
game.play()