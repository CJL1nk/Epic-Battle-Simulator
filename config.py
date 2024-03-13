import json
import os
from time import sleep

config = {
    "maxPlayerHealth": "1000",
    "playerAttackDamage": "75",
    "playerChargedAttackDamage": "150",
    "playerBlockDamage": "50",
    "playerCritDamage": "50",
    "playerHealAmount": "50",
    "playerCritHeal": "100"
}

print(" Default config: ")
print("", config)


config["maxPlayerHealth"] = input("\n\n Enter max player health: ")
config["playerAttackDamage"] = input(" Enter attack damage: ")
config["playerChargedAttackDamage"] = input(" Enter charged attack damage: ")
config["playerBlockDamage"] = input(" Enter block resistance: ")
config["playerCritDamage"] = input(" Enter crit damage: ")
config["playerHealAmount"] = input(" Enter heal amount: ")
config["playerCritHeal"] = input(" Enter crit heal amount: ")

with open(f"{os.getcwd()}\\files\\config.json", "w") as file:
    json.dump(config, file, indent = 4)
    
print("Success!")
sleep(3)
