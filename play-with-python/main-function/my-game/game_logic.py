import player
import enemies

def game_loop():
    """Main game loop."""
    player_obj = player.Player(0, 0)  # Create a player instance
    enemy_obj = enemies.Enemy(5, 5)  # Create an enemy instance

    while True:
        print(f"Player Position: ({player_obj.x}, {player_obj.y})")
        print(f"Enemy Position: ({enemy_obj.x}, {enemy_obj.y})")

        player_input = input("Enter movement (w: up, s: down, a: left, d: right, q: quit): ")
        if player_input == 'w':
            player_obj.move(0, -1)  # Move up
        elif player_input == 's':
            player_obj.move(0, 1)  # Move down
        elif player_input == 'a':
            player_obj.move(-1, 0)  # Move left
        elif player_input == 'd':
            player_obj.move(1, 0)  # Move right
        elif player_input == 'q':
            print("Game Over")
            break

        enemy_obj.update()  # Update enemy position (simple example)

        if check_collisions(player_obj, enemy_obj):
            print("Game Over: Collision!")
            break

def check_collisions(player, enemy):
    """Check for collisions between player and enemy."""
    if player.x == enemy.x and player.y == enemy.y:
        return True
    return False