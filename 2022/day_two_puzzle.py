# utils.py
import utils

# File names
input_fname = "dayTwo_input.txt"
example_input_fname = "dayTwo_exampleInput.txt"

input_list = []
example_input_list = []

outcome_points = {"win": 6, "draw": 3, "lose": 0}
shape_points = {"rock": 1, "paper": 2, "scissors": 3}
shape_number = {"rock": 0, "paper": 1, "scissors": 2}
opp_shape_letter = {'A': "rock", 'B': "paper", 'C': "scissors"}
player_shape_letter = {'X': "rock", 'Y': "paper", 'Z': "scissors"}
player_outcome_letter = {'X': "lose", 'Y': "draw", 'Z': "win"}

rock_outcome_against_shape = {"win": "paper", "draw": "rock", "lose": "scissors"}
paper_outcome_against_shape = {"win": "scissors", "draw": "paper", "lose": "rock"}
scissors_outcome_against_shape = {"win": "rock", "draw": "scissors", "lose": "paper"}

def parse_files():
    utils.parse_file(example_input_fname, example_input_list)
    utils.parse_file(input_fname, input_list)

def choose_shape_for_outcome(opp_shape, desired_outcome):
    if opp_shape == "rock":
        return rock_outcome_against_shape[desired_outcome];
    elif opp_shape == "paper":
        return paper_outcome_against_shape[desired_outcome];
    elif opp_shape == "scissors":
        return scissors_outcome_against_shape[desired_outcome];

def points_for_outcome(opp_shape, player_shape):
    player = shape_number[player_shape]
    opp = shape_number[opp_shape]
    
    if (player + 1) % 3 == opp:
        return outcome_points["lose"]
    elif player == opp:
        return outcome_points["draw"]
    else:
        return outcome_points["win"]

def points_for_round(round_input):
    opp_shape = opp_shape_letter[round_input[0]]
    # player_shape = player_shape_letter[round_input[2]]
    
    player_desired_outcome = player_outcome_letter[round_input[2]]
    player_shape = choose_shape_for_outcome(opp_shape, player_desired_outcome)
    
    points = shape_points[player_shape]
    points += points_for_outcome(opp_shape, player_shape)

    return points

def points_for_game(input):
    total_points = 0
    for round in input:
        total_points += points_for_round( round )
    return total_points


def display_answer():
    print("Example - Input:", example_input_list);
    example_game_points = points_for_game(example_input_list)
    print("Example - Game points:", example_game_points)

    game_points = points_for_game(input_list)
    print("Answer - Game points:", game_points)

parse_files()
display_answer()