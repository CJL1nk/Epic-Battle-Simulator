import random
from time import sleep
import os
import json
from threading import Thread
from sys import platform
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
if platform == 'win32':
    os.system('title EPIC BATTLE SIMULATOR   V1.4')
else:
    print('Running in linux')


class color:
   ORANGE = '\033[38;5;208m'
   PINK = '\033[95m'
   PURPLE = '\033[95m'
   DARKCYAN = '\033[36m'
   OKBLUE = '\033[94m'
   CYAN = '\033[96m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   BLINK = '\033[5m'
   END = '\033[0m'

   
def rainbow(string):
    rainbow=[color.RED, color.ORANGE, color.YELLOW, color.GREEN, color.OKBLUE, color.PURPLE]
    number = 0
    if number == 6:
        number == 0
    for x in string:
        print(f'{rainbow[number]} {x}')
        number += 1

pygame.mixer.init(frequency = 44100, size = -16, channels = 2, buffer = 2**12) 
channel1 = pygame.mixer.Channel(0) # argument must be int
channel2 = pygame.mixer.Channel(1)

try:
    def start():

        playerHealth = maxPlayerHealth
        enemyHealth = enemy.getMaxEnemyHealth()
        playerCharged = 0
        enemyCharged = 0
        playerBlock = False
        enemyBlock = False

        thread = Thread(target=play_sound)
        thread.start()

        print(f" A wild {color.ORANGE}{enemyName}{color.END} approaches!")
        sleep(0.5)

        while playerHealth > 0 or enemyHealth > 0:

            attackChoice = attackMenu(playerCharged)

            match attackChoice:

                case 1:
                    playerBlock = False
                    enemyHealth, enemyBlock = attack(playerHealth, enemyHealth, enemyBlock)
                    playerCharged += 1

                case 2:
                    print(f"{color.YELLOW}\n\n You raise your hands to block...{color.END}")
                    if platform == 'win32':
                            filename=f"{os.getcwd()}\\files\\sounds\\player\\player_block.wav"

                    else:
                        filename=f"{os.getcwd()}/files/sounds/player/player_block.wav"

                    sound = pygame.mixer.Sound(filename)
                    channel2.play(sound)

                    playerBlock = True
                    sleep(1)

                case 3:
                    playerBlock = False
                    playerHealth = heal(playerHealth)

                case 4:
                    playerBlock = False
                    enemyHealth, enemyBlock = chargedAttack(playerHealth, enemyHealth, enemyBlock)
                    playerCharged = 0


            if enemyHealth <= 0:
                input("\n\n\n You win!")
                break
            
            sleep(0.25)
            print(f"\n {color.ORANGE}{enemyName}'s{color.END} turn...")
            sleep(0.75)

            playerHealth, enemyHealth, enemyCharged, playerBlock, enemyBlock = enemyMoveset(playerHealth, enemyHealth, enemyCharged, playerBlock, enemyBlock)

            checkHealth(playerHealth, enemyHealth)

            disaster = random.randint(1,100)
            if disaster >=2 and disaster <=3:
                playerHealth, enemyHealth = naturalDisaster(playerHealth, enemyHealth)
            checkHealth(playerHealth, enemyHealth)

            playerHealth = event(playerHealth)
            checkHealth(playerHealth, enemyHealth)      


    def attackMenu(playerCharged):

        choice = -1

        print("\n   ATTACK")
        sleep(0.1)
        print(f" [1] {color.RED}Attack{color.END}")
        sleep(0.1)
        print(f" [2] {color.YELLOW}Block{color.END}")
        sleep(0.1)
        print(f" [3] {color.GREEN}Heal{color.END}")

        if playerCharged >= 5:
            sleep(0.1)
            print(f" [4] {color.PINK}CHARGED ATTACK{color.END}")

        while choice < 1 or choice > 4:

            sleep(0.25)

            try:
                choice = int(input(" >> "))

            except:
                print("Invalid option!")
                choice = -1
                continue
            
            if playerCharged < 5 and choice == 4:
                print(f"\n {color.PINK}Charged attack not ready!{color.END}")
                choice = -1

            elif choice < 1 or choice > 4:
                print(" Invalid option!")

        return choice


    def attack(playerHealth, enemyHealth, enemyBlock):

        damage = playerAttackDamage

        print(f"\n\n You {color.RED}attack!{color.END}")

        if enemyBlock:
            sleep(1)
            print(f" {color.ORANGE}{enemyName}{color.END} blocks!")
            damage -= enemy.getEnemyBlockDamage()
            enemyBlock = False

        if random.randint(0, 9) == 9:
            print(f" {color.RED}C{color.ORANGE}r{color.YELLOW}i{color.GREEN}t{color.OKBLUE}i{color.PURPLE}c{color.RED}a{color.YELLOW}l{color.END} {color.GREEN}s{color.OKBLUE}t{color.PURPLE}r{color.RED}i{color.ORANGE}k{color.YELLOW}e{color.GREEN}!{color.END}")
            damage += playerCritDamage
            
            if platform == 'win32':
                    filename=f"{os.getcwd()}\\files\\sounds\\player\\player-crit.wav"
                
            else:
                filename=f"{os.getcwd()}/files/sounds/player/player-crit.wav"
                
            sound = pygame.mixer.Sound(filename)
            channel2.play(sound)
            sleep(1)
            
        else:
            if platform == 'win32':
                filename=f"{os.getcwd()}\\files\\sounds\\player\\player-hit-hurt.wav"
                
            else:
                filename=f"{os.getcwd()}/files/sounds/player/player-hit-hurt.wav"
                
            sound = pygame.mixer.Sound(filename)
            channel2.play(sound)
            sleep(1)

        if damage < 0:
            damage = 0

        enemyHealth -= damage

        checkHealth(playerHealth, enemyHealth)

        print(f" {color.ORANGE}{enemyName}{color.END} health: {color.GREEN}{enemyHealth}/{enemy.getMaxEnemyHealth()}{color.END}")
        sleep(1)

        return enemyHealth, enemyBlock


    def heal(playerHealth):

        playerHealth += playerHealAmount
        
        if platform == 'win32':
            filename=f"{os.getcwd()}\\files\\sounds\\player\\player_heal.wav"
        else:
            filename=f"{os.getcwd()}/files/sounds/player/player_heal.wav"
            
        sound = pygame.mixer.Sound(filename)
        channel2.play(sound)

        print(f"\n\n You {color.GREEN}heal!{color.END}")
        sleep(1)

        if playerHealth > maxPlayerHealth:
            playerHealth = maxPlayerHealth

        print(f" Your health: {color.GREEN}{playerHealth}/{maxPlayerHealth}{color.END}")
        sleep(1)

        return playerHealth


    def chargedAttack(playerHealth, enemyHealth, enemyBlock):

        damage = playerChargedAttackDamage
        if platform == 'win32':
            filename=f"{os.getcwd()}\\files\\sounds\\player\\player_charged.wav"
        else:
            filename=f"{os.getcwd()}/files/sounds/player/player_charged.wav"
        
        sound = pygame.mixer.Sound(filename)
        channel2.play(sound)

        print(f"\n\n You {color.PINK}CHARGED ATTACK!{color.END}")
        
        sleep(1)

        if enemyBlock:
            print(f" {color.ORANGE}{enemyName}{color.END} blocks!")
            damage -= enemy.getEnemyBlockDamage()
            enemyBlock = False

        if random.randint(0, 9) == 9:
            print(f" {color.RED}C{color.ORANGE}r{color.YELLOW}i{color.GREEN}t{color.OKBLUE}i{color.PURPLE}c{color.RED}a{color.YELLOW}l{color.END} {color.GREEN}s{color.OKBLUE}t{color.PURPLE}r{color.RED}i{color.ORANGE}k{color.YELLOW}e{color.GREEN}!{color.END}")
            damage += playerCritDamage

        if damage < 0:
            damage = 0

        enemyHealth -= damage

        checkHealth(playerHealth, enemyHealth)

        print(f" {color.ORANGE}{enemyName}{color.END} health: {color.GREEN}{enemyHealth}/{enemy.getMaxEnemyHealth()}{color.END}")
        sleep(1)

        return enemyHealth, enemyBlock


    def enemyMoveset(playerHealth, enemyHealth, enemyCharged, playerBlock, enemyBlock):

        enemyMove = -1

        def enemyAttack(playerHealth, playerBlock):

            damage = enemy.getEnemyAttackDamage()

            print(f"\n\n {color.ORANGE}{enemyName}{color.END} {color.RED}attacks!{color.END}")

            if playerBlock:
                sleep(1)
                print(f" You {color.YELLOW}block!{color.END}")
                damage -= playerBlockDamage
                playerBlock = False

            if random.randint(0, 9) == 9:
                print(f" {color.ORANGE}{enemyName}{color.END} hits a {color.RED}c{color.ORANGE}r{color.YELLOW}i{color.GREEN}t{color.OKBLUE}i{color.PURPLE}c{color.RED}a{color.YELLOW}l{color.END} {color.GREEN}s{color.OKBLUE}t{color.PURPLE}r{color.RED}i{color.ORANGE}k{color.YELLOW}e{color.GREEN}!{color.END}")
                damage += enemy.getEnemyCritDamage()
                
                if platform == 'win32':
                    filename=f"{os.getcwd()}\\files\\sounds\\player\\player-crit.wav"
                
                else:
                    filename=f"{os.getcwd()}/files/sounds/player/player-crit.wav"
                
                sound = pygame.mixer.Sound(filename)
                channel2.play(sound)
                sleep(1)
                
            else:
                if platform == 'win32':
                    filename=f"{os.getcwd()}\\files\\sounds\\player\\player-hit-hurt.wav"
                
                else:
                    filename=f"{os.getcwd()}/files/sounds/player/player-hit-hurt.wav"
                
            sound = pygame.mixer.Sound(filename)
            channel2.play(sound)
            sleep(1)

            if damage < 0:
                damage = 0

            playerHealth -= damage

            checkHealth(playerHealth, enemyHealth)

            print(f" Your health: {color.GREEN}{playerHealth}/{maxPlayerHealth}{color.END}")
            sleep(1)

            return playerHealth, playerBlock


        def enemyHeal(enemyHealth):


            enemyHealth += enemy.getEnemyHealAmount()
            
            if platform == 'win32':
                filename=f"{os.getcwd()}\\files\\sounds\\player\\player_heal.wav"
            else:
                filename=f"{os.getcwd()}/files/sounds/player/player_heal.wav"
            
            sound = pygame.mixer.Sound(filename)
            channel2.play(sound)

            print(f"\n\n {color.ORANGE}{enemyName}{color.END} {color.GREEN}heals!{color.END}")
            sleep(1)

            if enemyHealth > enemy.getMaxEnemyHealth():
                enemyHealth = enemy.getMaxEnemyHealth()

            print(f" {color.ORANGE}{enemyName}{color.END} health: {color.GREEN}{enemyHealth}/{enemy.getMaxEnemyHealth()}{color.END}")
            sleep(1)

            return enemyHealth    


        def enemyChargedAttack(playerHealth, playerBlock):

            damage = enemy.getEnemyChargedAttackDamage()
            
            if platform == 'win32':
                filename=f"{os.getcwd()}\\files\\sounds\\player\\player_charged.wav"
            else:
                filename=f"{os.getcwd()}/files/sounds/player/player_charged.wav"

            print(f"\n\n {color.ORANGE}{enemyName}{color.END} {color.PINK}CHARGED ATTACKS!{color.END}")
            sleep(1)

            if playerBlock:
                print(f" You {color.YELLOW}block!{color.END}")
                damage -= playerBlockDamage
                playerBlock = False

            if random.randint(0, 9) == 9:
                print(f" {color.ORANGE}{enemyName}{color.END} hits a {color.RED}c{color.ORANGE}r{color.YELLOW}i{color.GREEN}t{color.OKBLUE}i{color.PURPLE}c{color.RED}a{color.YELLOW}l{color.END} {color.GREEN}s{color.OKBLUE}t{color.PURPLE}r{color.RED}i{color.ORANGE}k{color.YELLOW}e{color.GREEN}!{color.END}")
                damage += enemy.getEnemyCritDamage()

            if damage < 0:
                damage = 0

            playerHealth -= damage

            checkHealth(playerHealth, enemyHealth)

            print(f" Your health: {color.GREEN}{playerHealth}/{maxPlayerHealth}{color.END}")
            sleep(1)

            return playerHealth, playerBlock


        while enemyMove < 1 or enemyMove > 4:

            enemyMove = random.randint(1, 4)

            if enemyCharged >= 5:
                enemyMove = 4

            if enemyCharged != 5 and enemyMove == 4:
                enemyMove = -1

        match enemyMove:

            case 1:
                enemyBlock = False
                playerHealth, playerBlock = enemyAttack(playerHealth, playerBlock)
                enemyCharged += 1

            case 2:
                print(f"\n\n {color.ORANGE}{enemyName}{color.END} {color.YELLOW}raises their hands to block...{color.END}")
                enemyBlock = True
                if platform == 'win32':
                    filename=f"{os.getcwd()}\\files\\sounds\\player\\player_block.wav"
                
                else:
                    filename=f"{os.getcwd()}/files/sounds/player/player_block.wav"
                
                sound = pygame.mixer.Sound(filename)
                channel2.play(sound)

                sleep(1)

            case 3:
                enemyBlock = False
                enemyHealth = enemyHeal(enemyHealth)

            case 4:
                enemyBlock = False
                playerHealth, playerBlock = enemyChargedAttack(playerHealth, playerBlock)
                enemyCharged = 0

        return playerHealth, enemyHealth, enemyCharged, playerBlock, enemyBlock


    def naturalDisaster(playerHealth, enemyHealth):

        sleep(2)
        print("\n\n ???")
        sleep(1)

        disasterVar = random.randint(1,2)

        match disasterVar:

            case 1:
                x = random.randint(1,3)

                match x:
                    case 1:
                        print(f"\n A meteor falls from the sky and hits you. {color.RED}It deals 300 damage!{color.END}")
                        sleep(0.5)

                        playerHealth -= 300
                        if playerHealth < 0:
                            playerHealth = 0

                        print(f" Player Health: {color.GREEN}{playerHealth}/{maxPlayerHealth}{color.END}")
                    case 2:
                        print(f"\n A meteor falls from the sky and hits the {color.ORANGE}{enemyName}{color.END}. {color.RED}It deals 300 damage!{color.END}")
                        sleep(0.5)

                        enemyHealth -= 300
                        if enemyHealth < 0:
                            enemyHealth = 0

                        print(f" Enemy Health: {color.GREEN}{enemyHealth}/{enemy.getMaxEnemyHealth()}{color.END}")
                    case 3:
                        print(f"\n A meteor falls from the sky and hits you and the {color.ORANGE}{enemyName}{color.END}. {color.RED}It deals 300 damage!{color.END}")
                        sleep(0.5)

                        enemyHealth -= 300
                        playerHealth -= 300
                        if playerHealth < 0:
                            playerHealth = 0
                        if enemyHealth < 0:
                            enemyHealth = 0

                        print(f" Player Health: {color.GREEN}{playerHealth}/{maxPlayerHealth}{color.END}")
                        sleep(0.2)
                        print(f" {color.ORANGE}{enemyName}{color.END} Health: {color.GREEN}{enemyHealth}/{enemy.getMaxEnemyHealth()}{color.END}")

            case 2:
                x = random.randint(1,3)

                match x:
                    case 1:
                        print(f"\n A fairy emerges from the clouds and {color.GREEN}heals you for 250 health!{color.END}")
                        sleep(0.5)

                        playerHealth += 250
                        if playerHealth > maxPlayerHealth:
                            playerHealth = maxPlayerHealth

                        print(f" Player Health: {color.GREEN}{playerHealth}/{maxPlayerHealth}{color.END}")
                    case 2:
                        print(f"\n A fairy emerges from the clouds and {color.GREEN}heals the {color.ORANGE}{enemyName}{color.END} for 250 health!{color.END}")
                        sleep(0.5)

                        enemyHealth += 250
                        if enemyHealth > enemy.getMaxEnemyHealth():
                            enemyHealth = enemy.getMaxEnemyHealth()

                        print(f" Enemy Health: {color.GREEN}{enemyHealth}/{enemy.getMaxEnemyHealth()}{color.END}")
                    case 3:
                        print(f"\n A fairy emerges from the clouds and {color.GREEN}heals both you and the {color.ORANGE}{enemyName}{color.END} for 250 health!{color.END}")
                        sleep(0.5)

                        enemyHealth += 250
                        playerHealth += 250
                        if playerHealth > maxPlayerHealth:
                            playerHealth = maxPlayerHealth
                        if enemyHealth > enemy.getMaxEnemyHealth():
                            enemyHealth = enemy.getMaxEnemyHealth()

                        print(f" Player Health: {color.GREEN}{playerHealth}/{maxPlayerHealth}{color.END}")
                        sleep(0.2)
                        print(f" {color.ORANGE}{enemyName}{color.END} Health: {color.GREEN}{enemyHealth}/{enemy.getMaxEnemyHealth()}{color.END}")

        return playerHealth, enemyHealth


    def event(playerHealth):

        foundRod =  False

        hotdog = random.randint(1,10000)
        rod = random.randint(1,500)

        if hotdog == 5164:
            sleep(2)
            print("\n\n !!!")
            sleep(1)
            print(f" {color.PINK}Sans{color.END} emerges from the forest and gives you a hot dog. It was very tasty.")
            sleep(0.5)

        if rod == 345:

            sleep(2)
            print("\n\n !!!")
            sleep(1)
            print(f" You found a {color.GREEN}Rod of Discord!{color.END}")
            sleep(0.5)

            foundRod = True
        if foundRod:

            if random.randint(1,100) == 64:

                print(" The Adult Eidolon Wyrm emerges from the depths of the abyss and kills you!")
                playerHealth = 0

        return playerHealth


    def checkHealth(playerHealth, enemyHealth):

        if playerHealth <= 0:

            input(f"\n\n\n {color.RED}You died!{color.END}")
            exit(0)

        if enemyHealth <= 0:
            input(f"\n\n\n {color.YELLOW}You win!{color.END}")
            exit(0)


    def play_sound():
        
        if platform == 'win32':    
            filename=f"{os.getcwd()}\\files\\sounds\\music\\Leviathan_SlendStone.wav"
        else:
            filename=f"{os.getcwd()}/files/sounds/music/Leviathan_SlendStone.wav"   
        
        sound = pygame.mixer.Sound(filename)
        # channel1.set_volume(0.7)
        channel1.play(sound, loops = -1)
        
        
    def loadConfig():
        
        if platform == 'win32':
            with open(f"{os.getcwd()}\\files\\config.json") as file:
                configData = json.load(file)
        else:
            with open(f"{os.getcwd()}/files/config.json") as file:
                configData = json.load(file)

        return configData


    if platform == 'win32':
        with open(f'{os.getcwd()}\\files\\enemies\\enemies.enemies') as file:
            a = file.read()
            enemies = a.splitlines()
            enemyName = random.choice(enemies)
            
    else:
        with open(f'{os.getcwd()}/files/enemies/enemies.enemies') as file:
            a = file.read()
            enemies = a.splitlines()
            enemyName = random.choice(enemies)

    class Enemy:

        def __init__(self, maxEnemyHealth, enemyAttackDamage, enemyChargedAttackDamage, enemyBlockDamage, enemyCritDamage, enemyHealAmount): 

            self.maxEnemyHealth = maxEnemyHealth
            self.enemyAttackDamage = enemyAttackDamage
            self.enemyChargedAttackDamage = enemyChargedAttackDamage
            self.enemyBlockDamage = enemyBlockDamage
            self.enemyCritDamage = enemyCritDamage
            self.enemyHealAmount = enemyHealAmount


        def getMaxEnemyHealth(self):
            return self.maxEnemyHealth

        def getEnemyAttackDamage(self):
            return self.enemyAttackDamage

        def getEnemyChargedAttackDamage(self):
            return self.enemyChargedAttackDamage

        def getEnemyBlockDamage(self):
            return self.enemyBlockDamage

        def getEnemyCritDamage(self):
            return self.enemyCritDamage

        def getEnemyHealAmount(self):
            return self.enemyHealAmount

    if platform == 'win32':
        with open(f"{os.getcwd()}\\files\\enemies\\{enemyName}.json") as file:
            enemyData = json.load(file)
            
    else:
        with open(f"{os.getcwd()}/files/enemies/{enemyName}.json") as file:
            enemyData = json.load(file)
        enemyData = enemyData
    enemy = Enemy(int(enemyData["maxEnemyHealth"]), int(enemyData["enemyAttackDamage"]), int(enemyData["enemyChargedAttackDamage"]), int(enemyData["enemyBlockDamage"]), int(enemyData["enemyCritDamage"]), int(enemyData["enemyHealAmount"]))

    try:
        configData = loadConfig()
        maxPlayerHealth = int(configData["maxPlayerHealth"])
        playerAttackDamage = int(configData["playerAttackDamage"])
        playerChargedAttackDamage = int(configData["playerChargedAttackDamage"])
        playerBlockDamage = int(configData["playerBlockDamage"])
        playerCritDamage = int(configData["playerCritDamage"])
        playerHealAmount = int(configData["playerHealAmount"])

    except:
        maxPlayerHealth = 1000
        playerAttackDamage = 75
        playerChargedAttackDamage = 150
        playerBlockDamage = 50
        playerCritDamage = 50
        playerHealAmount = 50

    start()
except KeyboardInterrupt:
    print('KeyboardInterrupt')
