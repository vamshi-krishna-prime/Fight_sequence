import random
import time

def print_pause(message):
    print(message)
    time.sleep(1)
    
enemy_defense= 20
player_defense= 20
player_health = 100
enemy_health = 100

# damage= int((abs(damage)+damage)/2)
# print(damage)
# print("Net damage: " + damage)


def fight():
    global enemy_defense
    global player_defense
    global player_health
    global enemy_health
    for turn in range(20):
        if turn % 2 == 0 and player_health > 0:
            print_pause("Player Attacks")
            player_offense= random.randint(20,50)
            enemy_damage= enemy_defense - player_offense
            print_pause("Enemy damage: "+ str(enemy_damage))
            enemy_health += enemy_damage
            print_pause("Player_health: "+ str(player_health))
            print_pause("Enemy_health: "+ str(enemy_health) + "\n")

        elif turn % 2 == 1 and enemy_health > 0:
            print_pause("Enemy Attacks")
            enemy_offense= random.randint(20,50)
            player_damage= player_defense - enemy_offense
            print_pause("Player damage: "+ str(player_damage))
            player_health += player_damage
            print_pause("Player_health: "+ str(player_health))
            print_pause("Enemy_health: "+ str(enemy_health) + "\n")
            
        if player_health > 0 and enemy_health <= 0:
            print_pause("You have successfully slain the enemy")
            print_pause("You emerge victorious !!")
            return "player wins"
        
        elif player_health <= 0 and enemy_health > 0:
            print_pause("Game Ends !!, Better luck next time...")
            return "enemy wins"
            
fight()
