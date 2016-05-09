# Adversarial Search
**Adversarial search assignment**

Assignment description is [here](ai-t1b.pdf)!  
Requires [Pygame](http://www.pygame.org/news.html) :snake:  
Tested with [Python](https://www.python.org/) 2.7.9  
Check out this [Python](http://learnpython.org/) tutorial!

## Getting Started
- [Download this project](https://github.com/pucrs-ai-cs/adversarial-search/archive/master.zip)
- Install Python 2.7 and Pygame with [Super Install](super-install.sh) on Linux, you may be asked to accept, press **Y**

    ```
    bash super-install.sh
    ```

### Source:
The following are the files required to build your [Tic-tac-toe](http://en.wikipedia.org/wiki/Tic-tac-toe) player. Minimax and Alpha-Beta are the incomplete ones.

- [common.py](common.py) with constants and board methods
- [interface.py](interface.py) with drawing calls
- [tictactoe.py](tictactoe.py) contains the game logic
- [player_human.py](player_human.py) asks human for help
- [player_random.py](player_random.py) picks any clear cell
- [player_minimax.py](player_minimax.py) uses [minimax](http://en.wikipedia.org/wiki/Minimax) algorithm :exclamation:
- [player_alphabeta.py](player_alphabeta.py) uses [alpha-beta pruning](http://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning), this one is a bonus :exclamation:
- [test_tictactoe.py](test_tictactoe.py) contains the tests

### Execution

Player :large_blue_circle: is the first to play, followed by :x:, but your players can behave differently from each other using different arguments:

| Argument | Player Type |
| -------- | ------------- |
|   :zero: | Human :restroom:  |
|   :one:  | Random :interrobang: |
|   :two:  | Minimax :arrow_down_small::arrow_up_small: |
|   :three:| Alpha-Beta :rocket: |

- Execute interface with default players
```
python interface.py [playerO playerX]
```
- Execute terminal with default players
```
python tictactoe.py [playerO playerX]
```
- Execute tests
```
python test_tictactoe.py
```

### Questions

Questions are in the [readme.txt](readme.txt) to be sent together with the code.

### Player Interface

Players require a minimal interface to play the game. They receive their index (O or X) in the initialization, you do not need to worry about this as common.py already defined ```O``` and ```X``` as constants for you. Just remember to use ```self.index``` to compare with the other cells in the board to see how you are going. The hard part is to select the best cell in the board, ```get_next_move(self, board)``` is the method that must return a valid cell during the player turn. Cells must be an integer between 0 and 8. Let us take our friend Bob as an example. [Somebody](http://en.wikipedia.org/wiki/Alice_and_Bob) told him to start in the center, but he never got the rest of the message to understand how to continue the game:

```Python
from common import *

class Player_Bob:

    def __init__(self, index):
        self.index = index

    def get_next_move(self, board):
        return 4
```

The board is represented by a 1D list. If we consider Bob as the X player the board would be modified like this:

```Python
# 0 1 2
# 3 4 5
# 6 7 8

from common import *

player = Player_Bob(X)
board = [0,0,0,  0,0,0,  0,0,0]
move = player.get_next_move(board)
check_valid_move
board[move] = X
```

### Hints

- Use the method ```find_empty_cells(board)``` from common.py to help you see where is available to play.
- Do not try to mark several cells at once, the game provides a copy of the board for you to observe and only the position returned will make any difference.
- Start with a **successor** method that generates ([yields?](http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python)) different scenarios for you.
- Take a look at our [random player](player_random.py) or the [questions](readme.txt) if you get stuck.
- Python creates a lot of **.pyc** files if not called with **-B** flag, ```python -B script.py arguments```
