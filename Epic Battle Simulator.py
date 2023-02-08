import random
from time import sleep
import os
import json
from threading import Thread

os.system('title EPIC BATTLE SIMULATOR   V1.2')

try:
    from playsound import playsound
except ModuleNotFoundError:
    print("Error: Install \"playsound\" module. INSTALL 1.2.2  >>  pip install playsound==1.2.2")
    print("Game will continue...")
    sleep(3)


def start():
    
    playerHealth = maxPlayerHealth
    enemyHealth = enemy.getMaxEnemyHealth()
    playerCharged = 0
    enemyCharged = 0
    playerBlock = False
    enemyBlock = False
    
    thread = Thread(target=play_sound)
    thread.start()
    
    print(f" A wild {enemyName} approaches!")
    sleep(0.5)
    
    while playerHealth > 0 or enemyHealth > 0:
        
        attackChoice = attackMenu(playerCharged)
        
        match attackChoice:
            
            case 1:
                playerBlock = False
                enemyHealth, enemyBlock = attack(playerHealth, enemyHealth, enemyBlock)
                playerCharged += 1
                
            case 2:
                print("\n\n You raise your hands to block...")
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
        print(f"\n {enemyName}'s turn...")
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
    print(" [1] Attack")
    sleep(0.1)
    print(" [2] Block")
    sleep(0.1)
    print(" [3] Heal")
    
    if playerCharged >= 5:
        sleep(0.1)
        print(" [4] CHARGED ATTACK")
    
    while choice < 1 or choice > 4:
        
        sleep(0.25)
        
        try:
            choice = int(input(" >> "))
            
        except:
            print("Invalid option!")
            choice = -1
            continue
        
        if playerCharged < 5 and choice == 4:
            print("\n Charged attack not ready!")
            choice = -1
            
        elif choice < 1 or choice > 4:
            print(" Invalid option!")
    
    return choice
        
        
def attack(playerHealth, enemyHealth, enemyBlock):
    
    damage = playerAttackDamage
    
    print("\n\n You attack!")
    sleep(1)
    
    if enemyBlock:
        print(f" {enemyName} blocks!")
        damage -= enemy.getEnemyBlockDamage()
        enemyBlock = False
        
    if random.randint(0, 9) == 9:
        print(" Critical strike!")
        damage += playerCritDamage
        
    if damage < 0:
        damage = 0
    
    enemyHealth -= damage
    
    checkHealth(playerHealth, enemyHealth)
    
    print(f" {enemyName} health: {enemyHealth}/{enemy.getMaxEnemyHealth()}")
    sleep(1)
    
    return enemyHealth, enemyBlock


def heal(playerHealth):
    
    playerHealth += playerHealAmount
    
    print("\n\n You heal!")
    sleep(1)
    
    if playerHealth > maxPlayerHealth:
        playerHealth = maxPlayerHealth
    
    print(f" Your health: {playerHealth}/{maxPlayerHealth}")
    sleep(1)
    
    return playerHealth


def chargedAttack(playerHealth, enemyHealth, enemyBlock):
    
    damage = playerChargedAttackDamage
    
    print("\n\n You CHARGED ATTACK!")
    sleep(1)
    
    if enemyBlock:
        print(f" {enemyName} blocks!")
        damage -= enemy.getEnemyBlockDamage()
        enemyBlock = False
        
    if random.randint(0, 9) == 9:
        print(" Critical strike!")
        damage += playerCritDamage
        
    if damage < 0:
        damage = 0
    
    enemyHealth -= damage
    
    checkHealth(playerHealth, enemyHealth)
    
    print(f" {enemyName} health: {enemyHealth}/{enemy.getMaxEnemyHealth()}")
    sleep(1)
    
    return enemyHealth, enemyBlock
    

def enemyMoveset(playerHealth, enemyHealth, enemyCharged, playerBlock, enemyBlock):
    
    enemyMove = -1
    
    def enemyAttack(playerHealth, playerBlock):
        
        damage = enemy.getEnemyAttackDamage()
    
        print(f"\n\n {enemyName} attacks!")
        sleep(1)
        
        if playerBlock:
            print(" You block!")
            damage -= playerBlockDamage
            playerBlock = False
            
        if random.randint(0, 9) == 9:
            print(f" {enemyName} hits a critical strike!")
            damage += enemy.getEnemyCritDamage()
            
        if damage < 0:
            damage = 0
        
        playerHealth -= damage
        
        checkHealth(playerHealth, enemyHealth)
        
        print(f" Your health: {playerHealth}/{maxPlayerHealth}")
        sleep(1)
        
        return playerHealth, playerBlock
    
    
    def enemyHeal(enemyHealth):
        
        
        enemyHealth += enemy.getEnemyHealAmount()
    
        print(f"\n\n {enemyName} heals!")
        sleep(1)
        
        if enemyHealth > enemy.getMaxEnemyHealth():
            enemyHealth = enemy.getMaxEnemyHealth()
        
        print(f" {enemyName} health: {enemyHealth}/{enemy.getMaxEnemyHealth()}")
        sleep(1)
        
        return enemyHealth    
    
    
    def enemyChargedAttack(playerHealth, playerBlock):
        
        damage = enemy.getEnemyChargedAttackDamage()
    
        print(f"\n\n {enemyName} CHARGED ATTACKS!")
        sleep(1)
        
        if playerBlock:
            print(" You block!")
            damage -= playerBlockDamage
            playerBlock = False
            
        if random.randint(0, 9) == 9:
            print(f" {enemyName} hits a critical strike!")
            damage += enemy.getEnemyCritDamage()
            
        if damage < 0:
            damage = 0
        
        playerHealth -= damage
        
        checkHealth(playerHealth, enemyHealth)
        
        print(f" Your health: {playerHealth}/{maxPlayerHealth}")
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
            print(f"\n\n {enemyName} raises their hands to block...")
            enemyBlock = True
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
                    print("\n A meteor falls from the sky and hits you. It deals 300 damage!")
                    sleep(0.5)
                    
                    playerHealth -= 300
                    if playerHealth < 0:
                        playerHealth = 0
                    
                    print(f" Player Health: {playerHealth}/{maxPlayerHealth}")
                case 2:
                    print(f"\n A meteor falls from the sky and hits the {enemyName}. It deals 300 damage!")
                    sleep(0.5)
                    
                    enemyHealth -= 300
                    if enemyHealth < 0:
                        enemyHealth = 0
                    
                    print(f" Enemy Health: {enemyHealth}/{enemy.getMaxEnemyHealth()}")
                case 3:
                    print(f"\n A meteor falls from the sky and hits you and the {enemyName}. It deals 300 damage!")
                    sleep(0.5)
                    
                    enemyHealth -= 300
                    playerHealth -= 300
                    if playerHealth < 0:
                        playerHealth = 0
                    if enemyHealth < 0:
                        enemyHealth = 0
                    
                    print(f" Player Health: {playerHealth}/{maxPlayerHealth}")
                    sleep(0.2)
                    print(f" {enemy} Health: {enemyHealth}/{enemy.getMaxEnemyHealth()}")
        case 2:
            x = random.randint(1,3)
            
            match x:
                case 1:
                    print("\n A fairy emerges from the clouds and heals you for 250 health!")
                    sleep(0.5)
                    
                    playerHealth += 250
                    if playerHealth > maxPlayerHealth:
                        playerHealth = maxPlayerHealth
                        
                    print(f" Player Health: {playerHealth}/{maxPlayerHealth}")
                case 2:
                    print(f"\n A fairy emerges from the clouds and heals the {enemyName} for 250 health!")
                    sleep(0.5)
                    
                    enemyHealth += 250
                    if enemyHealth > enemy.getMaxEnemyHealth():
                        enemyHealth = enemy.getMaxEnemyHealth()
                        
                    print(f" Enemy Health: {enemyHealth}/{enemy.getMaxEnemyHealth()}")
                case 3:
                    print(f"\n A fairy emerges from the clouds and heals both you and the {enemyName} for 250 health!")
                    sleep(0.5)
                    
                    enemyHealth += 250
                    playerHealth += 250
                    if playerHealth > maxPlayerHealth:
                        playerHealth = maxPlayerHealth
                    if enemyHealth > enemy.getMaxEnemyHealth():
                        enemyHealth = enemy.getMaxEnemyHealth()
                    
                    print(f" Player Health: {playerHealth}/{maxPlayerHealth}")
                    sleep(0.2)
                    print(f" {enemy} Health: {enemyHealth}/{enemy.getMaxEnemyHealth()}")
    
    return playerHealth, enemyHealth


def event(playerHealth):
    
    foundRod =  False
    
    hotdog = random.randint(1,10000)
    rod = random.randint(1,500)
    
    if hotdog == 5164:
        sleep(2)
        print("\n\n !!!")
        sleep(1)
        print(" Sans emerges from the forest and gives you a hot dog. It was very tasty.")
        sleep(0.5)
        
    if rod == 345:
        
        sleep(2)
        print("\n\n !!!")
        sleep(1)
        print(" You found a Rod of Discord!")
        sleep(0.5)
        
        foundRod = True
    if foundRod:
        
        if random.randint(1,100) == 64:
            
            print("The Adult Eidolon Wyrm emerges from the depths of the abyss and kills you!")
            playerHealth = 0
    
    return playerHealth


def checkHealth(playerHealth, enemyHealth):
    
    if playerHealth <= 0:
            
        input("\n\n\n You died!")
        exit(0)
        
    if enemyHealth <= 0:
        input("\n\n\n You win!")
        exit(0)
        
    
def play_sound():
    
    playsound(f"{os.getcwd()}\\files\\Leviathan_SlendStone.wav")
    

def loadConfig():
    
    with open(f"{os.getcwd()}\\files\\config.json") as file:
        configData = json.load(file)
        
    return configData

with open(f'{os.getcwd()}\\files\\enemies\\enemies.enemies') as file:
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


with open(f"{os.getcwd()}\\files\\enemies\\{enemyName}.json") as file:
    enemyData = json.load(file)
    
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