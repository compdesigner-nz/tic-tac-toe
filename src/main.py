import gamerunner as gr
import os

def main():
        print("Welcome to Tic-Tac-Toe!")
        print("Please enter the players' names \n \n")
        print("--------------------------")
        player_1 = input("Player 1\n\n")
        print("--------------------------")
        player_2 = input("Player 2\n\n")
        print("Thanks! \n\nHow many games do you want to play?")
        game_count_valid = False
        while game_count_valid == False:
                game_count = input("Please enter a number of games greater than 0 \n\n")
                if(int(game_count) > 0):
                        game_count_valid = True
        print("Thanks! Enjoy your game!")
        os.system('cls')
        runner = gr.GameRunner(player_1,player_2, int(game_count))
        runner.run()

if(__name__ == "__main__"):
        main()