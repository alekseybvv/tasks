class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

class RockPaperScissors:
    @staticmethod
    def rps_game_winner(players):
        if len(players) != 2:
            raise WrongNumberOfPlayersError 

        player1, action1 = players[0]
        player2, action2 = players[1]

        valid_actions = ['R', 'P', 'S']
      
        if action1 not in valid_actions or action2 not in valid_actions:
            raise NoSuchStrategyError

        if action1 == action2:
            return f'{player1} {action1}'

        if (action1 == 'R' and action2 == 'S') or (action1 == 'S' and action2 == 'P') or (action1 == 'P' and action2 == 'R'):
            return f'{player1} {action1}'
        else:
            return f'{player2} {action2}'


try:
    result = RockPaperScissors.rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])
    print(result)
except Exception as e:
    print(e.__class__.__name__) 

try:
    result = RockPaperScissors.rps_game_winner([['player1', 'P'], ['player2', 'A']])
    print(result)
except Exception as e:
    print(e.__class__.__name__)  

try:
    result = RockPaperScissors.rps_game_winner([['player1', 'P'], ['player2', 'S']])
    print(result)
except Exception as e:
    print(e.__class__.__name__)

try:
    result = RockPaperScissors.rps_game_winner([['player1', 'P'], ['player2', 'P']])
    print(result)
except Exception as e:
    print(e.__class__.__name__)
