def printBoard(board):
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################
print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': '
   ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    if(board['top-L'] =='X' &&board['mid-L'] =='X' && board['low-L']
      print('X is the winner')
    if(board['top-L'] =='X' &&board['top-M'] =='X' && board['top-R']
      print('X is the winner')
    if(board['top-L'] =='X' &&board['mid-M'] =='X' && board['low-R'] 
      print('X is the winner')
    if(board['mid-L'] =='X' &&board['mid-M'] =='X' && board['mid-R'] 
      print('X is the winner')
    if(board['low-L'] =='X' &&board['low-M'] =='X' && board['low-R'] 
      print('X is the winner')
    if(board['low-L'] =='X' &&board['mid-M'] =='X' && board['top-R']   
      print('X is the winner')
    if(board['top-R'] =='X' &&board['mid-R'] =='X' && board['low-R'] 
      print('X is the winner')
    if(board['top-M'] =='X' &&board['mid-M'] =='X' && board['low-M']
      print('X is the winner')
    
    if(board['top-L'] =='O' &&board['mid-L'] =='O' && board['low-L']
      print('O is the winner')
    if(board['top-L'] =='O' &&board['top-M'] =='O' && board['top-R']
      print('O is the winner')
    if(board['top-L'] =='O' &&board['mid-M'] =='O' && board['low-R'] 
      print('O is the winner')
    if(board['mid-L'] =='O' &&board['mid-M'] =='O' && board['mid-R'] 
      print('O is the winner')
    if(board['low-L'] =='O' &&board['low-M'] =='O' && board['low-R'] 
      print('O is the winner')
    if(board['low-L'] =='O' &&board['mid-M'] =='O' && board['top-R']   
      print('O is the winner')
    if(board['top-R'] =='O' &&board['mid-R'] =='O' && board['low-R'] 
      print('O is the winner')
    if(board['top-M'] =='O' &&board['mid-M'] =='O' && board['low-M']
      print('O is the winner')

def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer
    for i in range(9):
        printBoard(board)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        board[move] = turn
        if( checkWinner(board, 'X') ):
            print('X wins!')
            break
        elif ( checkWinner(board, 'O') ):
            print('O wins!')
            break
    
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board)
    
