import json
import os
from time import sleep

config = {
    "maxPlayerHealth": 1000,
    "playerAttackDamage": 75,
    "playerChargedAttackDamage": 150,
    "playerBlockDamage": 50,
    "playerCritDamage": 50,
    "playerHealAmount": 50,
    "playerCritHeal": 100
}

print(" Default config: ")
print("", config)

def get_user_input(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Please enter a valid integer.")


config["maxPlayerHealth"] = get_user_input("\n\n Enter max player health: ")
config["playerAttackDamage"] = get_user_input(" Enter attack damage: ")
config["playerChargedAttackDamage"] = get_user_input(" Enter charged attack damage: ")
config["playerBlockDamage"] = get_user_input(" Enter block resistance: ")
config["playerCritDamage"] = get_user_input(" Enter crit damage: ")
config["playerHealAmount"] = get_user_input(" Enter heal amount: ")
config["playerCritHeal"] = get_user_input(" Enter crit heal amount: ")

file_path = os.path.join(os.getcwd(), "files", "config.json")

with open(os.path.join(os.getcwd(), 'files', 'config.json'), "w") as file:
    json.dump(config, file, indent = 4)
    
print("Success!")
sleep(3)
