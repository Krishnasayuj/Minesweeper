#d=dim_size, n=num_bombs
import random,re
class Board:
    def __init__ (self, d, n):
        self.d=d
        self.n=n
        self.board=self.makeboard()
        self.assign_values_to_board()
        self.dug=set()
    


    def makeboard(self):
        board=[[None for _ in range(self.d)] for _ in range(self.d)]
        bombs_planted=0
        while bombs_planted < self.n:
            loc=random.randint(0, self.d**2 - 1)
            row=loc//self.d
            col=loc%self.d
            if board[row][col]=='*':
                continue
            board[row][col]='*'
            bombs_planted+=1
        print(board)
        return board
    
    def assign_values_to_board(self):
        for r in range(self.d):
            for c in range(self.d):
                if self.board[r][c]=='*':
                    continue
                self.board[r][c]=self.get_num_neighboring_bombs(r,c)
    
    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs=0
        for r in range(max(0, row-1), min(self.d -1, row+1)+1):
            for c in range(max(0, col-1), min(self.d -1, col+1)+1):
                if r==row and c==col:
                    continue
                if self.board[r][c]=='*':
                    num_neighboring_bombs+=1

        return num_neighboring_bombs
    
    def dig(self, row, col):

        self.dug.add((row, col))
        if self.board[row][col]=='*':
            return False
        elif self.board[row][col]>0:
            return True
        for r in range(max(0, row-1), min(self.d -1, row+1)+1):
            for c in range(max(0, col-1), min(self.d -1, col+1)+1):
                if (r,c) in self.dug:
                    continue
                self.dig(r, c)

        return True
    
    def __str__(self):
        visible_board=[[None for _ in range(self.d)] for _ in range(self.d)]
        for row in range(self.d):
            for col in range(self.d):
                if(row,col) in self.dug:
                    visible_board[row][col]=str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.d):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key = len)))

        # print the csv strings
        indices = [i for i in range(self.d)]
        indices_row = '  '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.d)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
                   

        




def play(d=10, n=10):
    board=Board(d,n)
    safe=True

    while len(board.dug)<board.d**2 -n:
        print(board)
        #u=re.split(',(\\s)*', input("Where do you wanna dig> ROw: COL:"))
        #row, col = int(u[0]), int(u[-1])
        row=int(input("Row where u want to dig?"))
        col=int(input("column where u want to dig?"))
        if row<0 or row>=board.d or col<0 or col>=d:
            print("Try a valid location")
            continue
        safe=board.dig(row,col)
        if not safe:
            break
    if safe:
        print("HEYYO! You did it!")
    else:
        print("GAME OVER ")
        board.dug=[(r,c) for r in range(board.d) for c in range(board.d)]
        print(board)

if __name__ == '__main__':
    play()

