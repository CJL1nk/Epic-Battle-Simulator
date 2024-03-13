import json

files=['consumables.json', 'armor.json', 'weapons.json']

# for x in files:
  # print(x)
with open("weapons.json", 'r') as f:
  load=json.load(f)

for item in load:
  tier = item['tier']
  dropChance=item['dropChance'][f"{str(tier)}"]
  if dropChance is not None:
    del item['dropChance']
  if dropChance > 0.6:
    dropChance-=.2
  item['dropChance'] = dropChance

print(json.dumps(load, indent=4))
  