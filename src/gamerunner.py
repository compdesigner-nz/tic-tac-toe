import gametracker as gt
import re
import random
import os

class GameRunner:
        def __init__(self, player_1_name: str, player_2_name: str, best_of: int = 3) -> None:
                self.player_1 = player_1_name
                self.player_2 = player_2_name
                self.players = [self.player_1, self.player_2]
                self.games = [gt.Game() for i in range(best_of)]
                self.player_1_score = 0
                self.player_2_score = 0
                self.run()
        def run(self):
                for i, game in enumerate(self.games):
                        os.system('cls')
                        print(f"Game {i+1} of {len(self.games)}")
                        self.run_game(game)

        def run_game(self, game: gt.Game) -> None:
                """
                Method that runs a game

                Args:
                    game (gt.Game): The game to run               
                    """
                result = self.__alternate_players(game, random.randint(0,1))
                match result:
                        case 2:
                                print("The game has been drawn. Starting a new game.")
                                self.games.append(gt.Game())

        
        def __alternate_players(self, game: gt.Game, starter: int) -> int:
                """
                Method that alternates between the players, getting an input from the player and then displaying the choice

                Args:
                    game (gt.Game): The gam to alternate players for
                    starter (int): The starter player

                Returns:
                    int: The winning result
                """
                player_index = starter
                choice_character = False
                player = player = self.players[starter]
                while game.winner == None:
                        try:
                                choice = self.get_player_choice(player)
                                game.update_square(choice["vertical"],choice["horizontal"], choice_character)
                                os.system('cls')
                                win = game.check_for_winner()
                                game_value = game.print_game()
                                print(game_value)
                                print("\n\n ----------------------------------")
                                if(win == -1):
                                        choice_character = not(choice_character)
                                        if(player == self.player_1):
                                                player = self.player_2
                                        else:
                                                player = self.player_1
                                else:
                                        if(win != 2):
                                                self.congratulate_game_winner(player)
                                        input("Press enter to continue")
                                        return win
                        except:
                                print("Oops! That square is already taken! Try a different square :)\n\n")
                                print("-------------------\n")
                
        def get_player_choice(self, player_name) -> dict:
                """
                Method that gets the player's choice of square a text input from the console.

                Args:
                    player_name (str): The player whose turn it is

                Returns:
                    dict: A dictionary of the choice
                """
                print(f"{player_name}, please enter the square selection from below for your square of choice (see below for hints)")
                # print("0,0 - top left")
                # print("0,0 - top center")
                # print("0,2 - top right")
                # print("1,0 - middle left")
                # print("1,1 - middle center")
                # print("1,2 - middle right")
                # print("2,0 - bottom left")
                # print("2,1 - bottom center")
                # print("2,2 - bottom right")
                print("\n\n")

                #get the choice and validate it
                choice_valid = False
                while choice_valid == False:
                        choice = input("Please input your selection in the form of 'x,y':\n\n")
                        if(self.__validate_choice(choice) == True):
                                choice_valid = True
                vert, horizontal = choice.split(',')
                return {
                        "vertical":int(vert),
                        "horizontal": int(horizontal)
                }
        def __validate_choice(self, choice: str) -> bool:
                match_string = "[0-2],[0-2]"
                match = re.match(match_string, choice)
                if(match):
                        return True
                else: 
                        return False
        def congratulate_game_winner(self, player_name: str) -> None:
                print(f"Congratulations, {player_name}!")
                print("--------------------------")
                if(player_name == self.player_1):
                        self.player_1_score += 1
                else:
                        self.player_2_score += 1
                print(f"SCORE\n{self.player_1}:{self.player_1_score} - {self.player_2}:{self.player_2_score}")

        