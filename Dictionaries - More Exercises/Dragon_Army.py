from collections import defaultdict
from statistics import mean

default_stats = {'damage': 45, 'health': 250, 'armor': 10}

dragons = defaultdict(lambda: defaultdict(defaultdict))

for _ in range(int(input())):
    dragon_type, name, damage, health, armor = input().split()
    damage = int(damage) if damage != 'null' else default_stats['damage']
    health = int(health) if health != 'null' else default_stats['health']
    armor = int(armor) if armor != 'null' else default_stats['armor']
    dragons[dragon_type][name] = {'damage': damage, 'health': health, 'armor': armor}

for dragon_type in dragons.keys():
    type_damage = mean([dragons[dragon_type][name]['damage'] for name in dragons[dragon_type]])
    type_health = mean([dragons[dragon_type][name]['health'] for name in dragons[dragon_type]])
    type_armor = mean([dragons[dragon_type][name]['armor'] for name in dragons[dragon_type]])
    print(f"{dragon_type}::({type_damage:.2f}/{type_health:.2f}/{type_armor:.2f})")
    for name in sorted(dragons[dragon_type]):
        damage = dragons[dragon_type][name]['damage']
        health = dragons[dragon_type][name]['health']
        armor = dragons[dragon_type][name]['armor']
        print(f"-{name} -> damage: {damage}, health: {health}, armor: {armor}")