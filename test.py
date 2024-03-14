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
        


def random_test(dropchance: float):
  import random
  yesGacha = 0
  noGacha = 0
  def event_occurs():
    event=random.random() <= dropchance
    # print(event)
    return event 
  
  try:
    for x in range(10000):
      if event_occurs():
        yesGacha+=1
        pass
      else:
        noGacha+=1
        pass
    
    print(f'Draw: {yesGacha}')
    print(f'No Draw: {noGacha}')
  except:
    print()
    print(f'Draw: {yesGacha}')
    print(f'No Draw: {noGacha}')
    
def calculate_drop_chance(desired_outcomes:int, possible_outcomes:int):
  return desired_outcomes/possible_outcomes

print(rainbow('This is a test'))
dropchance=calculate_drop_chance(1, 100)
print(dropchance)
random_test(dropchance)