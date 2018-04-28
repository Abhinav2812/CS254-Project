from copy import deepcopy
from random import choice
import matplotlib.pyplot as plt


class Board():
    def __init__(self, rows=9, cols=6, no_of_players=2):
        self.rows = rows
        self.cols = cols
        self.no_of_players = no_of_players
        self.turn = 1
        self.player_colors = ['r','r','g','b']
        # player starts with index 1
        self.player_orbs_count = [0] * (no_of_players + 1)
        self.no_of_turns = [0] * (no_of_players + 1)
        onestate = {'player': 0, 'mass': 0}
        self.state = [[deepcopy(onestate) for i in range(cols)]
                      for i in range(rows)]

    def __getitem__(self, pos):
        return self.state[pos[0]][pos[1]]

    def __setitem__(self, pos, value):
        self.state[pos[0]][pos[1]] = value

    def __str__(self):
        s = ""
        for i in range(self.rows):
            for j in range(self.cols):
                s += str((self[(i, j)]['player'], self[(i, j)]['mass'])) + " "
            s += '\n'
        return s

    def hash(self):
        return str(self)

    def neighbours(self, pos):
        ans = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                pos2 = (pos[0] + i, pos[1] + j)
                if (pos2 == pos or (i != 0 and j != 0) or
                        not self.valid_pos(pos2)):
                    continue
                ans.append(pos2)
        return ans

    def game_over(self, player):
        if (self.player_orbs_count[player] == 0 and
                self.no_of_turns[player] != 0):
            return True
        else:
            return False

    def get_next_player(self):
        self.turn = 1 if self.turn == self.no_of_players else self.turn + 1
        while self.game_over(self.turn):
            self.turn = 1 if self.turn == self.no_of_players else self.turn + 1

    def critical(self, pos):
        critical_mass = 1
        if pos in [(0, 0), (self.rows - 1, 0), (0, self.cols - 1),
                   (self.rows - 1, self.cols - 1)]:
            critical_mass = 2
        elif pos[0] in [0, self.rows - 1] or pos[1] in [0, self.cols - 1]:
            critical_mass = 3
        else:
            critical_mass = 4
        return critical_mass

    def valid_pos(self, pos, player_check=False):
        if (pos[0] < 0 or pos[0] >= self.rows or
                pos[1] < 0 or pos[1] >= self.cols):
            return False
        if (player_check and self[pos]['player'] != 0 and
                self[pos]['player'] != self.turn):
            return False
        return True

    def move(self, pos, mid_states=True):
        if not self.valid_pos(pos, player_check=True):
            yield False
        else:
            self.no_of_turns[self.turn] += 1
            self.player_orbs_count[self.turn] += 1
            self[pos]['player'] = self.turn
            self[pos]['mass'] += 1
            if self[pos]['mass'] >= self.critical(pos):
                delim = -1
                unstable = [pos, delim]
                while len(unstable):
                    if self.game_complete():
                        unstable = []
                        continue
                    top = unstable.pop()
                    if top == delim:
                        if len(unstable):
                            unstable.insert(0, delim)
                        if mid_states:
                            yield(self)
                        continue
                    self[top]['player'] = self.turn
                    self[top]['mass'] -= self.critical(top)
                    if self[top]['mass'] == 0:
                        self[top]['player'] = 0
                    for i in self.neighbours(top):
                        old_player = self[i]['player']
                        if old_player != self.turn:
                            self.player_orbs_count[old_player] -= (
                                self[i]['mass'])
                            self.player_orbs_count[self.turn] += (
                                self[i]['mass'])
                            self[i]['player'] = self.turn
                        self[i]['mass'] += 1
                        if self[i]['mass'] >= self.critical(i):
                            if i not in unstable:
                                unstable.insert(0, i)
            else:
                if mid_states:
                    yield self
            if not mid_states:
                yield True
            self.get_next_player()

    def play(self, pos, mid_states=True):
        if mid_states:
            return self.move(pos, mid_states)
        else:
            temp = [x for x in self.move(pos, False)]
            return temp[0]

    def game_complete(self):
        still_playing = []
        for i in range(1, self.no_of_players + 1):
            if not (self.player_orbs_count[i] == 0 and
                    self.no_of_turns[i] != 0):
                still_playing.append(i)
        if len(still_playing) != 1:
            return False
        else:
            return still_playing[0]

    def valid_moves(self):
        moves = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self[(i, j)]['player'] in [0, self.turn]:
                    moves.append((i, j))
        return moves

    def verify_game_over(self):
        for i in range(1, self.no_of_players + 1):
            if (self.game_complete() == i and self.game_over(i)):
                return False
            elif (self.game_complete() != i and not self.game_over(i)):
                return False
        return True
    def drawOneCircle(self,xa,ya,ra,ca,x,y,color='r'):
        x+=0.5
        y+=0.5
        xa.append(x)
        ya.append(y)
        ra.append(300)
        ca.append(color)

    def drawTwoCircle(self,xa,ya,ra,ca,x,y,color='r'):
        x+=0.5
        y+=0.5
        x-=.2
        xa.append(x)
        ya.append(y)
        ra.append(300)
        ca.append(color)
        x+=.4
        xa.append(x)
        ya.append(y)
        ra.append(300)
        ca.append(color)

    def drawThreeCircle(self,xa,ya,ra,ca,x,y,color='r'):
        x+=0.5
        y+=0.5
        x-=.2
        y-=.2
        xa.append(x)
        ya.append(y)
        ra.append(300)
        ca.append(color)
        x+=.4
        xa.append(x)
        ya.append(y)
        ra.append(300)
        ca.append(color)
        x-=.2
        y+=.4
        xa.append(x)
        ya.append(y)
        ra.append(300)
        ca.append(color)

    
    def drawGraphical(self, image_name):
        x = []
        y = []
        r = []
        c = []
        i,j = 0,0
        for row in self.state:
            j = 0
            for cell in row:
                if cell['mass'] == 1:
                    self.drawOneCircle(x,y,r,c,i,j,self.player_colors[cell['player']])
                elif cell['mass'] == 2:
                    self.drawTwoCircle(x,y,r,c,i,j,self.player_colors[cell['player']])
                elif cell['mass'] == 3:
                    self.drawThreeCircle(x,y,r,c,i,j,self.player_colors[cell['player']])
                j+=1
            i+=1
        plt.scatter(x,y,s=r,c=c)
        plt.gca().set_xlim([0,self.rows])
        plt.gca().set_ylim([0,self.cols])
        plt.grid()
        plt.savefig(image_name)
        plt.clf()



def test():
    rows, cols = 9, 6
    no_of_games = 100
    no_of_players = 10
    no_of_moves_avg = 0
    wins = [0] * (no_of_players + 1)
    for _ in range(no_of_games):
        board = Board(rows=rows, cols=cols, no_of_players=no_of_players)
        while not board.game_complete():
            for i in range(no_of_players):
                pos = choice(board.valid_moves())
                board.play(pos, mid_states=False)
                if board.game_complete():
                    break
        wins[board.game_complete()] += 1
        no_of_moves_avg += sum(board.no_of_turns)
        assert(board.verify_game_over())
    no_of_moves_avg //= no_of_games
    for i in range(1, no_of_players + 1):
        print("Player " + str(i) + ": " + str(wins[i]))
    print("Average No of Moves:" + str(no_of_moves_avg))


if __name__ == '__main__':
    test()
