# Dungeon Game
# Create a player (P), a door(D) and a monster(M)
# The player must reach the door and avoid the monster
# The monster makes a random move after the player moves
# If the player touches a monster, the player loses
# If the player reaches/touches the door, the player wins the game

# The player moves using keys "w" "a" "s" "d"

import random

# Define the size of the game board
BOARD_SIZE = 5

# Define the game board
def create_board(size):
    return [['.' for _ in range(size)] for _ in range(size)]

# Print the game board
def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

# Randomly place player, door, and monster on the board
def place_items(board):
    positions = random.sample(range(BOARD_SIZE * BOARD_SIZE), 3)
    player_pos = divmod(positions[0], BOARD_SIZE)
    door_pos = divmod(positions[1], BOARD_SIZE)
    monster_pos = divmod(positions[2], BOARD_SIZE)
    board[player_pos[0]][player_pos[1]] = 'P'
    board[door_pos[0]][door_pos[1]] = 'D'
    board[monster_pos[0]][monster_pos[1]] = 'M'
    return player_pos, door_pos, monster_pos

# Move the player on the board
def move_player(player_pos, move):
    x, y = player_pos
    if move == 'w' and x > 0:
        x -= 1
    elif move == 's' and x < BOARD_SIZE - 1:
        x += 1
    elif move == 'a' and y > 0:
        y -= 1
    elif move == 'd' and y < BOARD_SIZE - 1:
        y += 1
    return (x, y)

# Move the monster randomly
def move_monster(monster_pos):
    x, y = monster_pos
    move = random.choice(['w', 's', 'a', 'd'])
    return move_player((x, y), move)

# Check if the player has won or lost
def check_win_or_lose(player_pos, door_pos, monster_pos):
    if player_pos == door_pos:
        return "win"
    elif player_pos == monster_pos:
        return "lose"
    return None

# Main game loop
def main():
    board = create_board(BOARD_SIZE)
    player_pos, door_pos, monster_pos = place_items(board)
    
    while True:
        print_board(board)
        move = input("Move (w/a/s/d): ").strip().lower()
        
        # Update player position
        board[player_pos[0]][player_pos[1]] = '.'
        player_pos = move_player(player_pos, move)
        board[player_pos[0]][player_pos[1]] = 'P'
        
        # Check win/lose condition
        result = check_win_or_lose(player_pos, door_pos, monster_pos)
        if result == "win":
            print("You reached the door! You win!")
            break
        elif result == "lose":
            print("The monster got you! You lose!")
            break
        
        # Move monster
        board[monster_pos[0]][monster_pos[1]] = '.'
        monster_pos = move_monster(monster_pos)
        board[monster_pos[0]][monster_pos[1]] = 'M'
        
        # Check win/lose condition again after monster moves
        result = check_win_or_lose(player_pos, door_pos, monster_pos)
        if result == "win":
            print("You reached the door! You win!")
            break
        elif result == "lose":
            print("The monster got you! You lose!")
            break

if __name__ == "__main__":
    main()

    