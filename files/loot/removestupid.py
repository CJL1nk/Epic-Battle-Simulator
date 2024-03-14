import json

files=['consumables.json', 'armor.json', 'weapons.json']

# for x in files:
  # print(x)
with open("armor.json", 'r') as f:
  load=json.load(f)

for item in load:
  tier = item['tier']
  tier = int(tier)
  dropChance=item['dropChance'][f"{tier}"]
  if dropChance is not None:
    del item['dropChance'] 
  
  if dropChance > 0.9:
    dropChance-=.2
  
  print(item)
  item['dropChance'] = dropChance

print(json.dumps(load, indent=4))
