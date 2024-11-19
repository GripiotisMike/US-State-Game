# US State Game

This is a fun and interactive game where the player attempts to name all 50 U.S. states. As each state is correctly guessed, its name is displayed on a map. Any missed states are saved to a separate CSV file for future study.

## Project Overview

In this project, you will be using Python's turtle graphics library to create an interactive map of the United States. The game asks players to guess U.S. states, and once the player guesses a state correctly, its name is written on the map. At the end of the game, any missed states are saved to a CSV file called states_to_learn.csv, which can be used to review the missed states later.


## Requirements

- Python 3.x
- pandas library
- turtle graphics library (comes with Python by default)

  ## How to play

1. Run the Game: Execute the main.py script. This will open a new window displaying the U.S. map.

2. Guess the States: You will be prompted to guess the name of a U.S. state. Type the name of a state (e.g., "California"). If the state is correct and has not been guessed yet, it will appear on the map at its correct location.

3. Exit the Game: If you want to stop the game before guessing all the states, type "Exit" in the prompt. This will save the list of missed states in a CSV file called states_to_learn.csv.

4. Winning the Game: The game continues until all 50 states are guessed correctly. Once completed, the game ends and you can start over or review the states you missed.

## How It Works
- The map of the United States is shown using a blank state map (blank_states_img.gif).
- The list of states is stored in 50_states.csv with their x and y coordinates.
- The player types in the name of a state, and if it matches a state in the list and hasn't been guessed before, its name is written on the map at the correct coordinates.
- When the player types "Exit", the program creates a CSV file (states_to_learn.csv) containing the names of states the player missed, which can be reviewed later.
