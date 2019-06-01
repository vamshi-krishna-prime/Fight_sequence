import random
import time

player_offense_moves= ["You step forward to slash the enemy",
                       "You rise high to deliver a mighty blow",
                       "You make a lunge and slash attack",
                       "You deliver an counter attack",
                       "A power blow was directed towads the enemy",
                       "You rain down a series of short swings",
                       "A sharp delivery to penetrate the defense of enemy",
                       "You run towards the enemy at great speed",
                       "You duck down and deliver a low swing",
                       "You stand tall and attck the enemy from the front",
                       "You run around and penetrate the back of the enemy"]

player_defense_moves= ["You hold the sword to counter the enemy attck",
                        "The enemy attacks are repelled by you",
                        "The enemy jumps on you and you roll to the side",
                        "You swing your sword in rythm to the enemy attacks",
                        "You step back away from the enemy",
                        "You dodge the enemy sword and ready to make an attack"]

enemy_offense_moves= ["The enemy charges at you like a mad bull",
                      "The enemy has a arm streangth of a boulder",
                      "Enemy has wits and great strategy to corner you",
                      "The enemy attacks from behind",
                      "The enemy rolls around and attacks from the side",
                      "The enemy jumps on you",
                      "The enemy fights you head on"]

enemy_defense_moves= ["Enemy has a strong defense",
                        "Your enemy has brains to dodge your attacks",
                        "Your enemy has speed advantage to evade your attacks",
                        "Your enemy has a strength to with stand your attack",
                        "Enemy is determined to take you head on",
                        "Your enemy is a formidable opponent"]

def health_decrease(health, num):
    if health > 0:
        health += num
        if health < 0:
            health = 0
        return health
    else:
        health = 0
        return health
      
def print_pause(message):
    print(message)
    time.sleep(1)

def health_decrease(health, num):
    if health > 0:
        health += num
        if health < 0:
            health = 0
        return health
    else:
        health = 0
        return health


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
            enemy_health = health_decrease(enemy_health, enemy_damage)
            print_pause("Player_health: "+ str(player_health))
            print_pause("Enemy_health: "+ str(enemy_health) + "\n")

        elif turn % 2 == 1 and enemy_health > 0:
            print_pause("Enemy Attacks")
            enemy_offense= random.randint(20,50)
            player_damage= player_defense - enemy_offense
            print_pause("Player damage: "+ str(player_damage))
            player_health = health_decrease(player_health, player_damage)
            print_pause("Player_health: "+ str(player_health))
            print_pause("Enemy_health: "+ str(enemy_health) + "\n")

        if player_health > 0 and enemy_health <= 0:
            print_pause("You have successfully slain the enemy")
            print_pause("You emerge victorious !!")
            return "player wins"
        
        elif player_health <= 0 and enemy_health > 0:
            print_pause("Game Ends !!, Better luck next time...")
            return "enemy wins"

fight_result= fight()
print_pause(fight_result)
