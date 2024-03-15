import random
from time import sleep
import os
import json
from threading import Thread
from sys import platform
import pygame
from pydantic import BaseModel, ValidationError
from munch import munchify
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
    name:int
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
      
      return enemyData, enemyName



    # selected_line = random.choice(enemybehold)
    # formatted_line = selected_line.format(color=color, enemyName=enemyName)



class Game:
  def __init__(self):
    thread = Thread(target=self._music())
    thread.start()
    self._loadEnemy()
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

  def _loadEnemy(self):
    self.enemy=Enemy()
    self.enemyData, self.enemyName = self.enemy.randomEnemy()

  def encounter(self):
    selected_line = random.choice(self.enemyAppear)
    formatted_line = selected_line.format(color=color, enemyName=self.enemyName)
    return formatted_line
  
  def play(self):
    
    
    pass


enemy=Enemy()
started=False
while True:
  if not started:
    game=Game()
    print(game.encounter())
    started=True
  else:
    pass

# game.load_config(confpath)
