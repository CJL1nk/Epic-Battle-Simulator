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
        
print(rainbow('This is a test'))


def random_test():
  import random
  yesGacha = 0
  noGacha = 0
  def event_occurs():
    event=random.random() <= 0.000002
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
    print(yesGacha)
    print(noGacha)
  except:
    print()
    print(yesGacha)
    print(noGacha)
    
def calculate_drop_chance(desired_outcomes:int, possible_outcomes:int):
  return desired_outcomes/possible_outcomes

print(calculate_drop_chance(1, 1000))