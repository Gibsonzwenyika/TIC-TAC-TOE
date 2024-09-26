def ConstBoard(board):
  print("Current state of the board :\n\n");
  for i in range (0 ,9):
    if (i>0) and (i%3==0):
      print("\n");
    if(board[i] == 0):
      print("_ ", end = " ");
    if (board[i] == 1):
      print("O ", end =" ");
    if (board[i] == -1):
      print("X " , end = " ");
  print("\n\n");

def User1Turn(board):
  pos = input("Enter X's position from [ 1, 2, 3, ..., 9]");
  pos = int(pos);
  if (board[pos - 1]!= 0):
    print("Wrong move");
    User1Turn(board);
  else:
   board[pos - 1]= -1;

def User2Turn(board):
  pos = input("Enter O's position from [ 1, 2, 3, ..., 9]");
  pos = int(pos);
  if (board[pos - 1]!= 0):
    print("Wrong move");
    exit(0);
  else:
   board[pos - 1]= 1;

def AnalyzeBoard(board):
  cd = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],[2, 4, 6], [0, 4, 8]];
  for i in range (0,8):
    if(board[cd[i][0]] !=0 and
     board[cd[i][0]] == board[cd[i][1]] and
     board[cd[i][1]] == board[cd[i][2]]):
     return board[cd[i][0]];

  return 0;

def CompTurn(board):
 pos = -1;
 value = -2;
 for i in range (0, 9):
  if(board[i]==0):
    board[i]=1;
    score = -MinMax(board, -1);
    board[i]= 0;
    if(score>value):
      value = score;
      pos = i;
 board[pos] =1;

def MinMax(board, player):
  x= AnalyzeBoard(board);
  if(x != 0):
    return x*player;
  pos = -1;
  value = -2;
  for i in range (0, 9):
   if(board[i]==0):
    board[i]=player;
    score = -MinMax(board, player*-1);
    board[i]= 0;
    if(score>value):
      value = score;
      pos = i;
  if(pos == -1):
   return 0;
  return value;




def main():
  choice = input("Enter 1(for single player) , 2 (for multiplayer)");
  choice = int(choice);
  board = [0, 0, 0, 0, 0, 0, 0, 0, 0];
  if (choice == 1):
    print("Computer :O vs you: X");
    player = input("Enter 1 to play first, 2 second");
    player = int(player);
    for i in range (0,9):
     if (AnalyzeBoard(board) != 0):
       break;
     if ((i + player) % 2 == 1):
      ConstBoard(board);
      User1Turn(board);
     else:
      ConstBoard(board);
      print("\n\n");
      CompTurn(board);

  else:
    print("player 1: X vs player 2: O");
    for i in range (0,9):
     if (AnalyzeBoard(board) != 0):
       break;
     if (i  % 2 == 0):
      ConstBoard(board);
      print("\n\n");
      User1Turn(board);
     else:
      ConstBoard(board);
      print("\n\n");
      User2Turn(board);
  x = AnalyzeBoard(board);
  if (x == 0):
   ConstBoard(board);
   print("Dreaw !!!");
  if (x == 1):
   ConstBoard(board);
   print("player O wins !!!");
  if (x == -1):
   ConstBoard(board);
   print("player X wins !!!");


main();