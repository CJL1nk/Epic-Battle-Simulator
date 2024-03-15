from __future__ import annotations
import random
from time import sleep
import os
import json
from threading import Thread
from sys import platform
import pygame
from pydantic import BaseModel, ValidationError
from typing import Type

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

if platform == 'win32':
    os.system('title EPIC BATTLE SIMULATOR   V1.4')
else:
    print('Running in unix')

soundbase = os.path.join(os.getcwd(), 'files', 'sounds')
playersound = os.path.join(soundbase, 'player')
musicpath = os.path.join(soundbase, 'music')
enemypath = os.path.join(os.getcwd(), 'files', 'enemies')
confpath = os.path.join(os.getcwd(), 'files', 'config.json')

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
  rainbowedlist=[]
  number = 1
  for x in string:
    rainbowedlist.append(f'{rainbow[number % len(rainbow)]}{x}{color.END}')
    number+=1
  return ''.join(rainbowedlist)

def crit_calculator(crit_chance: float):
  return random.random() <= crit_chance

def random_probability(how_many: int, out_of: int) -> bool:
  """Generate a random probability event based on a given ratio.

  Args:
      how_many (int): Number of favorable outcomes.
      out_of (int): Total number of possible outcomes.

  Raises:
      ValueError: If 'out_of' is zero or negative.

  Returns:
      bool: True if the random event occurs, False otherwise.
  """
  probability = how_many / out_of
  return random.random() <= probability

pygame.mixer.init(frequency = 44100, size = -16, channels = 2, buffer = 2**12) 
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)

class config():
  class playerConfig(BaseModel):
    maxPlayerHealth: int
    playerAttackDamage: int
    playerChargedAttackDamage: int
    playerBlockDamage: int
    playerCritDamage: int
    playerHealAmount: int
    playerCritHeal: int
  class enemyConfig(BaseModel):
    name:str
    maxEnemyHealth: int
    enemyAttackDamage:int
    enemyChargedAttackDamage: int
    enemyBlockDamage: int
    enemyCritDamage: int
    enemyHealAmount: int
    tier: int

class Enemy:
    
  def randomEnemy(self):
    filename = os.path.join(enemypath, 'enemies.enemies')
    with open(filename) as file:
      a = file.read()
      enemies = a.splitlines()
      enemyName = random.choice(enemies)
      filename = os.path.join(enemypath, f'{enemyName}.json')

      with open(filename) as file:
        enemyData = json.load(file)
      
      enemyName = enemyData['name']
      
      return config.enemyConfig(**enemyData), enemyName

    # selected_line = random.choice(enemybehold)
    # formatted_line = selected_line.format(color=color, enemyName=enemyName)

class Player:
  def __init__(self):
    self.maxPlayeHealth = None
    self.playerAttackDamage = None
    self.playerChargedAttackDamage = None
    self.playerBlockDamage = None
    self.playerCritDamage = None
    self.playerHealAmount = None
    self.playerCritHeal = None
    pass
  
  def _load_player(self):
        
    filename = os.path.join(confpath)
    with open(filename) as file:
      configData = json.load(file)
    conf=config.playerConfig(**configData)
    self.conf=conf
    return conf





def disaster(game: Game):
  player=game.player
  enemy=game.enemyData
  enemyName=game.enemyName
  playerHealth=game.playerHealth
  enemyHealth=game.enemyHealth
  sleep(2)
  print("\n\n ???")
  sleep(1)

  disasterVar = random.randint(1,2)

  match disasterVar:

    case 1:
      x = random.randint(1,3)

      match x:
        case 1:
          print(f"\n A meteor falls from the sky and hits {game.playerCallPrint}. {color.RED}It deals 300 damage!{color.END}")
          sleep(0.5)

          playerHealth -= 300
          if playerHealth < 0:
            playerHealth = 0

          print(f" Player Health: {color.GREEN}{playerHealth}/{player.maxPlayerHealth}{color.END}")
        case 2:
          print(f"\n A meteor falls from the sky and hits the {color.ORANGE}{enemyName}{color.END}. {color.RED}It deals 300 damage!{color.END}")
          sleep(0.5)

          enemyHealth -= 300
          if enemyHealth < 0:
            enemyHealth = 0

          print(f" Enemy Health: {color.GREEN}{enemyHealth}/{enemy.maxEnemyHealth}{color.END}")
        case 3:
          print(f"\n A meteor falls from the sky and hits {game.playerCallPrint} and the {color.ORANGE}{enemyName}{color.END}. {color.RED}It deals 300 damage!{color.END}")
          sleep(0.5)

          enemyHealth -= 300
          playerHealth -= 300
          if playerHealth < 0:
            playerHealth = 0
          if enemyHealth < 0:
            enemyHealth = 0

          print(f" Player Health: {color.GREEN}{playerHealth}/{player.maxPlayerHealth}{color.END}")
          sleep(0.2)
          print(f" {color.ORANGE}{enemyName}{color.END} Health: {color.GREEN}{enemyHealth}/{enemy.maxEnemyHealth}{color.END}")

        case 2:
          x = random.randint(1,3)

      match x:
        case 1:
          print(f"\n A fairy emerges from the clouds and {color.GREEN}heals {game.playerCallPrint} for 250 health!{color.END}")
          sleep(0.5)

          playerHealth += 250
          if playerHealth > player.maxPlayerHealth:
            playerHealth = player.maxPlayerHealth

          print(f" Player Health: {color.GREEN}{playerHealth}/{player.maxPlayerHealth}{color.END}")
        case 2:
          print(f"\n A fairy emerges from the clouds and {color.GREEN}heals the {color.ORANGE}{enemyName}{color.END} for 250 health!{color.END}")
          sleep(0.5)

          enemyHealth += 250
          if enemyHealth > enemy.maxEnemyHealth:
            enemyHealth = enemy.maxEnemyHealth

          print(f" Enemy Health: {color.GREEN}{enemyHealth}/{enemy.maxEnemyHealth}{color.END}")
        case 3:
          print(f"\n A fairy emerges from the clouds and {color.GREEN}heals both {game.playerCallPrint} and the {color.ORANGE}{enemyName}{color.END} for 250 health!{color.END}")
          sleep(0.5)

          enemyHealth += 250
          playerHealth += 250
          if playerHealth > player.maxPlayerHealth:
            playerHealth = player.maxPlayerHealth
          if enemyHealth > enemy.maxEnemyHealth:
            enemyHealth = enemy.maxEnemyHealth

          print(f" Player Health: {color.GREEN}{playerHealth}/{player.maxPlayerHealth}{color.END}")
          sleep(0.2)
          print(f" {color.ORANGE}{game.enemyName}{color.END} Health: {color.GREEN}{enemyHealth}/{enemy.maxEnemyHealth}{color.END}")
  


class Game:
  def __init__(self):
    thread = Thread(target=self._music())
    thread.start()

    self.playerCallPrint=f'{color.CYAN}You{color.END}'
    self.enemyAppear=[
            " Behold, {color.ORANGE}{enemyName}{color.END} approaches!",
            " {color.ORANGE}{enemyName}{color.END} emerges from the shadows!",
            " With a roar, {color.ORANGE}{enemyName}{color.END} charges into view!",
            " The ground trembles as {color.ORANGE}{enemyName}{color.END} draws near!",
            " From the depths, {color.ORANGE}{enemyName}{color.END} emerges!",
            " {color.ORANGE}{enemyName}{color.END} looms ominously in the distance!",
            " In a flash of light, {color.ORANGE}{enemyName}{color.END} appears!",
            " {color.ORANGE}{enemyName}{color.END} is here to test your mettle!",
            " With a sinister grin, {color.ORANGE}{enemyName}{color.END} approaches!",
            " Prepare yourselves, for {color.ORANGE}{enemyName}{color.END} is near!",
            " {color.ORANGE}{enemyName}{color.END} strikes a menacing pose!",
            " It's {color.ORANGE}{enemyName}{color.END}! Get ready for a showdown!",
            " With a wicked cackle, {color.ORANGE}{enemyName}{color.END} arrives!",
            " Fear not the shadows, fear {color.ORANGE}{enemyName}{color.END}!",
            " {color.ORANGE}{enemyName}{color.END} lurks in the darkness, awaiting its prey!",
            " The air grows cold as {color.ORANGE}{enemyName}{color.END} draws closer!",
            " {color.ORANGE}{enemyName}{color.END} emerges from the mist, ready to strike!",
            " {color.ORANGE}{enemyName}{color.END} prowls into view, hunger in its eyes!",
            " {color.ORANGE}{enemyName}{color.END} stands tall, a formidable foe!",
            " With a thunderous roar, {color.ORANGE}{enemyName}{color.END} announces its presence!",
            " {color.ORANGE}{enemyName}{color.END} appears, a force to be reckoned with!",
            " {color.ORANGE}{enemyName}{color.END} descends upon you, ready for battle!"]

  def _music(self):
    filename = os.path.join(musicpath, 'Leviathan_SlendStone.wav')
    
    sound = pygame.mixer.Sound(filename)
    # channel1.set_volume(0.7)
    channel1.play(sound, loops = -1)

  def loadConfig(self, confpath):
    with open(confpath, 'r') as file:
      enemyData=json.load(file)
      try:
        return config(**enemyData)
      except ValidationError as e:
        raise ValueError(f"Invalid player config file at \n {confpath}: \n{e}")

  def returnjson(self): 
    """Does exactly what it says, returns enemy json"""
    return self.enemyData
  
  def _loadEnemy(self):
    enemy=Enemy()
    self.enemyData, self.enemyName = enemy.randomEnemy()

  def _loadPlayer(self):
    player=Player()
    self.player=player._load_player()

  def encounter(self):
    selected_line = random.choice(self.enemyAppear)
    formatted_line = selected_line.format(color=color, enemyName=self.enemyName)
    return formatted_line
  
  def start(self):
    self._loadEnemy()
    self._loadPlayer()
    self.playerHealth=self.player.maxPlayerHealth
    self.enemyHealth=self.enemyData.maxEnemyHealth



enemy=Enemy()
started=False
game=Game()
while True:
  if not started:
    started=True
    player=Player()
    game.start()
    p=player._load_player()
    print(game.encounter())
    if random_probability(1, 1): # Disasters
      disaster(game)
  
  else:
    pass

# game.load_config(confpath)
