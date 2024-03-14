import json
import os
import typer
import random
from enum import Enum
from typing_extensions import Annotated
from typing import Optional

app = typer.Typer(no_args_is_help=True, add_completion=False)


enemypath=os.path.join(os.getcwd(), 'files', 'enemies')
jsons = os.path.join(enemypath, 'enemies.json')

def tier_generator(maxhealth):
  if maxhealth <= 1000:
    tier = 1
  elif maxhealth <= 2000:
    tier = 2
  elif maxhealth <= 3000:
    tier = 3
  elif maxhealth <= 4000:
    tier = 4
  elif maxhealth <= 7000:
    tier = 5
  elif maxhealth >= 7001:
    tier = 6
  return tier

class getloot:
  def __init__(self, tier:Optional[int], num_of_items: Optional[int]):
    self.tier = tier
    self.num_items = 1
    self.num_items = num_of_items
    print(self.num_items)
    
  def _load_loot_data(self):
    loot_data = []
    loot_paths = ['armor.json', 'consumables.json', 'weapons.json']

    for loot_path in loot_paths:
      with open(os.path.join(os.getcwd(), 'files', 'loot', loot_path)) as file:
        loot_data.extend(json.load(file))
      self.loot_data = loot_data

    return self._filter_loot_by_tier()

  def _filter_loot_by_tier(self):
      self.filtered_loot = [item for item in self.loot_data if item['tier'] == self.tier]
      return self._select_items_randomly()

  def _select_items_randomly(self):
      selected_items = []
      for _ in range(self.num_items):
        FilteredLootLen=len(self.filtered_loot)
        randnumber=random.randrange(0, FilteredLootLen)
        selected_loot=self.filtered_loot[randnumber]
        # print(selected_loot)
        selected_items.append(selected_loot['name'])

      return selected_items
    
  def loot(self):
    return self._load_loot_data()
  def describe(self):
    pass
    


@app.command()
def enemycreate():
  with open(jsons) as file:
    loadedjson = json.load(file)
  for x in loadedjson:
    writepath=os.path.join(os.getcwd(), 'files', 'enemies', f"{x['name']}.json")
    if os.path.exists(writepath):
      os.remove(writepath)
    if not os.path.exists(writepath):
      with open(writepath, 'w+') as f:
        f.write(f'''{{
        "name": "{x['name']}",
        "maxEnemyHealth": {x['maxEnemyHealth']},
        "enemyAttackDamage": {x['enemyAttackDamage']},
        "enemyChargedAttackDamage": {x['enemyChargedAttackDamage']},
        "enemyBlockDamage": {x['enemyBlockDamage']},
        "enemyCritDamage": {x['enemyCritDamage']},
        "enemyHealAmount": {x['enemyHealAmount']},
        "tier": {tier_generator(x['maxEnemyHealth'])}
      }}''')
        with open(os.path.join(enemypath, 'enemies.enemies'), "a") as file:
          file.write(f'{x['name']}\n')
          pass
    else:
      pass

@app.command()
def loot(
  tier: int = typer.Argument(1  , help="The tier of loot to generate (1-6)"),
  num_items: int = typer.Argument(5, help="Number of items to generate")

  ):
  gotloot=getloot(tier, num_items)
  looted=gotloot.loot()
  print(json.dumps(looted, indent=3))

@app.command()
def get_description(
  item: str = typer.Argument(default=None, help='The Name of the item to describe')
):
  looted=getloot()
  pass

if __name__ == "__main__":
  app()