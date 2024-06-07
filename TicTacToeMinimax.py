def minimax(board, player, isMaximizing):
  if player == "O":
    opponent = "X"
  else:
    opponent = "O" 
  # terminal evaluation  
  if check_win(board, player) :
    return 1
  if check_win(board, opponent) :
    return -1
  if board_full(board) :
    return 0

  if isMaximizing : # computer's turn (O)
    max_eval = float("-inf")
    for i in range(len(board)) :
      for j in range(len(board)) :
        if board[i][j] == " " :
          board[i][j] = player 
          eval = minimax(board, player, False)
          max_eval = max(eval, max_eval)
          board[i][j] = " " # undo the move
    return max_eval

  else : # human's turn (X)
    min_eval = float("inf")
    for i in range(len(board)) :
      for j in range(len(board)) :
        if board[i][j] == " " :
          board[i][j] = opponent 
          eval = minimax(board, player, True)
          min_eval = min(eval, min_eval)
          board[i][j] = " " # undo the move
    return min_eval


def check_win(board, player) :
  # rows/columns
  for i in range(len(board)) :
    if player == board[i][0]==board[i][1]==board[i][2] or\
     player == board[0][i]==board[1][i]==board[2][i] :
     return True
  # diagonals   
  if player == board[0][0]==board[1][1]==board[2][2] or\
   player == board[2][0]==board[1][1]==board[0][2] :
   return True
  return False


def board_full(board):
  return all(all(cell != " " for cell in row) for row in board) 


def computer_turn(board, player) :
  print("Computer's turn:")
  max_eval = float("-inf")
  best_move = (None, None)
  for i in range(len(board)) :
    for j in range(len(board)) :
      if board[i][j] == " " :
        board[i][j] = player 
        eval = minimax(board, player, False)
        board[i][j] = " "
        if eval > max_eval :
          max_eval = eval
          best_move = (i, j)      
  make_move(board, *best_move, player)      


def human_turn(board, player) :
  print("Human's turn:")
  while True :
    i = int(input("Enter the row (1-3) of your next move:"))-1
    j = int(input("Enter the column (1-3) of your next move:"))-1
    if not (0 <= i < 3 and 0 <= i < 3) :
      print("Invalid row/column value! Try again.")
    else:
      if make_move(board, i, j, player) :
        break
      else:
        print("Spot taken! Try another.")


def make_move(board, i, j, player) :
  if board[i][j] == " " :
    board[i][j] = player
    return True
  return False


def switch_turn(player) :
  new_player = "O" if player == "X" else "X"
  return new_player


def print_board(board):
  for row_index, row in enumerate(board):
    print("  | ".join(row))
    if row_index != 2:
      print("-" * 12)


def main() :
  board = [[" " for _ in range(3)] for _ in range(3)]
  current_player = "X"

  while True :
    print_board(board)

    if current_player == "X" :
      human_turn(board, current_player)
    else:
      computer_turn(board, current_player)
    # Check if game is over
    if check_win(board, current_player) :
      print_board(board)
      print(f"The {current_player} player wins!")
      break
    if board_full(board) :
      print_board(board)
      print("It's a tie!")
      break
    current_player = switch_turn(current_player)
      

if __name__ == "__main__" :
  main()