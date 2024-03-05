import json
import os
import typer
import random

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
  def __init__(self, tier, num_of_items):
    self.tier = tier
    self.num_items = num_of_items
  def _load_loot_data(self):
    loot_data = []
    loot_paths = ['armor.json', 'consumables.json', 'weapons.json']

    for loot_path in loot_paths:
      with open(os.path.join(os.getcwd(), 'files', 'loot', loot_path)) as file:
        loot_data.extend(json.load(file))
      self.loot_data = loot_data
      # print(loot_data)

    return self._filter_loot_by_tier()

  def _filter_loot_by_tier(self):
      self.filtered_loot = [item for item in self.loot_data if item['tier'] == self.tier]
      return self._select_items_randomly()

  def _select_items_randomly(self):
      selected_items = []
      for _ in range(self.num_items):
          total_drop_chance = sum(item.get('drop_chance', 0) for item in self.filtered_loot)
          random_num = random.uniform(0, total_drop_chance)
          cumulative_chance = 0
          for item in self.filtered_loot:
              cumulative_chance += item.get('drop_chance', 0)
              if random_num <= cumulative_chance:
                  selected_items.append(item)
                  break
      return selected_items
    
  def loot(self):
    return self._load_loot_data()
    


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
def lootier(
  tier: int = typer.Argument(..., help="The tier of loot to generate (1-6)"),
  num_items: int = typer.Argument(5, help="Number of items to generate")

  ):
  loot=getloot(tier, num_items)
  looted=loot.loot()
  print(json.dumps(looted, indent=3))

if __name__ == "__main__":
  app()