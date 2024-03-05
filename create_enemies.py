import json
import os
enemypath=os.path.join(os.getcwd(), 'files', 'enemies')
jsons = os.path.join(enemypath, 'enemies.json')
with open(jsons) as file:
  loadedjson = json.load(file)
for x in loadedjson:
  writepath=os.path.join(os.getcwd(), 'files', 'enemies', f"{x['name']}.json")
  if not os.path.exists(writepath):
    with open(writepath, 'w+') as f:
      f.write(f'''{{
      "name": "{x['name']}",
      "maxEnemyHealth": {x['maxEnemyHealth']},
      "enemyAttackDamage": {x['enemyAttackDamage']},
      "enemyChargedAttackDamage": {x['enemyChargedAttackDamage']},
      "enemyBlockDamage": {x['enemyBlockDamage']},
      "enemyCritDamage": {x['enemyCritDamage']},
      "enemyHealAmount": {x['enemyHealAmount']}
    }}''')
      with open(os.path.join(enemypath, 'enemies.enemies'), "a") as file:
        file.write(f'{x['name']}\n')
        pass
  else:
    pass
    

