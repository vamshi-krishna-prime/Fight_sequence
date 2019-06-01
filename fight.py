import random

enemy_defense= 20
player_defense= 20
player_health = 100
enemy_health = 100

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
