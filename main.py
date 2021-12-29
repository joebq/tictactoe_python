# turn related data into classes

from os import system

# clear function -> clears console
def clear():
 """ clear function clears the screen by call an OS function
  cls for Windows and clear for Linux"""
 system('clear')

# initialize_game funtion to set up the variables of the game
def initialize_game(name_player_one, name_player_two, symbols, player_one_symbol, player_two_symbol):
  """ initialize_game setups the initial values of the players, their symbols and checks if the values
  that were entered by the user are valid. This function is only called when the game starts or restarts """
  
  while player_one_symbol not in symbols:
    player_one_symbol = input("{0} choose your symobl: {1} or {2}: "
                          .format(name_player_one, symbols[0], symbols[1])).upper()
  if player_one_symbol == 'O':
    player_two_symbol = 'X'
  else:
    player_two_symbol = 'O'

  return (player_one_symbol, player_two_symbol)

# display tic tac toe board
def board_display(tic_tac_toe):
  """ board_display function prints out the tic tac toe board after each insert """

  print("\n")
  print("{:>12}".format(tic_tac_toe[0][0]), "{:>1}".format('|'), tic_tac_toe[0][1], "{:>2}".format('|'), tic_tac_toe[0][2])
  print("{:>12}".format('___'), '|', '_' * 2, '|', '_' * 3)
  print("{:>12}".format(tic_tac_toe[1][0]), "{:>1}".format('|'), tic_tac_toe[1][1], "{:>2}".format('|'), tic_tac_toe[1][2])
  print("{:>12}".format('___'), '|', '_' * 2, '|', '_' * 3)
  print("{:>12}".format(tic_tac_toe[2][0]), "{:>1}".format('|'), tic_tac_toe[2][1], "{:>2}".format('|'), tic_tac_toe[2][2])
  print("{:>12}".format('   '), '|', ' ' * 2, '|', ' ' * 3)
  print("\n")
  
def insert_position():
  """ insert_position function gets input from the user, checks if it is a legal input and returns the position
  to insert the symbol to the board """

  position = input("insert position between 1-9:")
  if position.isdigit() and 1 <= int(position) <=9:
    return int(position)
  else:
    insert_position()

def update_board(position):
  """ update_board function translates the position inserted by the user (1-9) to an index for the 
  2 x 2 tic_tac_toe board and retuns the position as a tuple to board_index_1 and board_index_2 """
  if position == 1:
    return (0,0)
  elif position == 2:
    return (0,1)
  elif position == 3:
    return (0,2)
  elif position == 4:
    return (1,0)
  elif position == 5:
    return (1,1)
  elif position == 6:
    return (1,2)
  elif position == 7:
    return (2,0)
  elif position == 8:
    return (2,1)
  elif position == 9:
    return (2,2)
    

def is_game_won(tic_tac_toe, symbol):
  """ is_game_won checks if any of the players got won, called twice after each players game 
  and alters the flow of the programme if the game has been won  """
  
  if (tic_tac_toe[0][0] ==  tic_tac_toe[0][1] == tic_tac_toe[0][2] == symbol or 
  tic_tac_toe[1][0] ==  tic_tac_toe[1][1] == tic_tac_toe[1][2] == symbol or 
  tic_tac_toe[2][0] ==  tic_tac_toe[2][1] == tic_tac_toe[2][2] == symbol or
  tic_tac_toe[0][0] ==  tic_tac_toe[1][0] == tic_tac_toe[2][0] == symbol or
  tic_tac_toe[0][1] ==  tic_tac_toe[1][1] == tic_tac_toe[2][1] == symbol or
  tic_tac_toe[0][2] ==  tic_tac_toe[1][2] == tic_tac_toe[2][2] == symbol or
  tic_tac_toe[0][0] ==  tic_tac_toe[1][1] == tic_tac_toe[2][2] == symbol or
  tic_tac_toe[0][2] ==  tic_tac_toe[1][1] == tic_tac_toe[2][0] == symbol ) :
   return True
  pass
  

def main():
  
  clear()
  #----- Variables ----#
  name_player_one = "Player One"
  name_player_two = "Player Two"

  play_game = 'Y'
  game_won = False

  player_one_symbol = ''
  player_two_symbol = ''

  board_index_1 = 0
  board_index_2 = 0
  

  tic_tac_toe = [[' ',' ', ' '], [' ',' ',' '], [' ',' ',' ']]
  symbols = ('O', 'X')
  #--------------------#

  print("Welcome to the tic tac toe game!")
  player_one_symbol, player_two_symbol = initialize_game(name_player_one, 
                                                        name_player_two, 
                                                        symbols, 
                                                        player_one_symbol, 
                                                        player_two_symbol
                                                        )

  # print(player_one_symbol, player_two_symbol)
  board_display(tic_tac_toe)
  
  while play_game == 'Y':
    number_of_play = 0
    while game_won != True and number_of_play != 8:
      print("player one turn")
      position = insert_position()
      number_of_play +=1
      board_index_1, board_index_2 = update_board(position)
      tic_tac_toe[board_index_1][board_index_2] = player_one_symbol
      board_display(tic_tac_toe)
      game_won = is_game_won(tic_tac_toe, player_one_symbol)
      if game_won:
        print("Player One Wins!\n")
        break


      print("player two turn")
      position = insert_position()
      number_of_play +=1
      board_index_1, board_index_2 = update_board(position)
      tic_tac_toe[board_index_1][board_index_2] = player_two_symbol
      board_display(tic_tac_toe)
      game_won = is_game_won(tic_tac_toe, player_two_symbol)
      if game_won:
        print("Player One Wins!\n")
        break
    play_game = (input("Want to play again? (Y/N): ")).upper()
  

if __name__ == '__main__':
  main()