import json
import os
import typer

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
    



if __name__ == "__main__":
  app()