print('Game Begins 👾👾🎮🎮......')
player1= input('player 1 Name:')
player2 = input('player 2 Name:')
select1count =0
select2count =0

while True:
  
  select1 = input ("""                 Scissor
                  Paper
                  Rock
                  Your choice player1 :""")
  select2 = input("""                  Scissor
                    Paper
                    Rock
                    Your choice player 2:""")

  if select1=="Scissor"and select2=="Rock":
    print("player2 won!😍")
    select2count +=1
  elif select1=="Rock" and select2 == "Scissor":
    print("player 1 won!😉")
    select1count +=1
      
  elif select1 == "Scissor" and select2== "Scissor" :
   print("It is tie!")
  elif select1=="Rock" and select2== "Rock":
   print ("It is tie!")
  elif select1 == "Paper" and select2 == "Scissor":
    print("player2 won!😍")
    select2count +=1
    
  elif select1 == "Scissor"and select2 == "Paper":
    print("player1 won!😉")
    select1count +=1
  elif select1== "Paper" and select2== "Paper":
   print("It is tie!")
  elif select1=="Rock" and select2== "Paper":
   print("player2 won!😍")
   select2count +=1
  elif select1=="Paper" and select2=="Rock":
   print("player1 won!😉")
   select1count +=1
  print("Player 1 has",select1count ,"point.")
  print("Player 2 has",select2count ,"point.")
  if select1count ==3 or select2count==3:
    print("Great Game.")
    break
  else:
   continue