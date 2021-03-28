def winner(choice1, choice2):
        print("Choose Rock Paper or Scissors:")
        player1 = choice1
        player2 = choice2
    
        if (player1 == 'rock' and player2 == 'scissors'):
            return "Player 1 wins."
 
        elif (player1 == 'rock' and player2 == 'rock'):
            return "It's a draw!"
 
        elif (player1 == 'scissors' and player2 == 'paper'):
            return "Player 1 wins."
 
        elif (player2 == 'scissors' and player2 == 'scissors'):
            return "It's a draw!"
 
        elif (player1 == 'paper' and player2 == 'paper'):
            return "It's a draw!"
 
        elif (player1 == 'paper' and player2 == 'scissors'):
            return "Player 2 wins." 
 
        elif (player1 == 'rock'and player2 == 'paper'):
           return "Player 2 wins." 
 
        elif (player1 == 'paper' and player2 == 'rock'):
            return "Player 1 wins."
 
        elif (player1 == 'scissors' and player2 == 'rock'):
            return "Player 2 wins."
            
