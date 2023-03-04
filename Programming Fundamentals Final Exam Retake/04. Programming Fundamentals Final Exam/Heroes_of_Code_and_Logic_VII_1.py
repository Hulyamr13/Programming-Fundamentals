n = int(input())

heroes = []
for i in range(n):
    name, hp, mp = input().split()
    hp, mp = int(hp), int(mp)
    if hp > 100:
        hp = 100
    if mp > 200:
        mp = 200
    hero = {"name": name, "hp": hp, "mp": mp}
    heroes.append(hero)

while True:
    command = input()
    if command == "End":
        break

    tokens = command.split(" - ")
    action = tokens[0]
    hero_name = tokens[1]
    hero = next((h for h in heroes if h["name"] == hero_name), None)

    if hero is None:
        continue

    if action == "CastSpell":
        mp_needed = int(tokens[2])
        spell_name = tokens[3]
        if hero["mp"] >= mp_needed:
            hero["mp"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {hero['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage = int(tokens[2])
        attacker = tokens[3]
        hero["hp"] = max(0, hero["hp"] - damage)
        if hero["hp"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero['hp']} HP left!")
        else:
            heroes.remove(hero)
            print(f"{hero_name} has been killed by {attacker}!")

    elif action == "Recharge":
        amount = int(tokens[2])
        amount_recovered = min(amount, 200 - hero["mp"])
        hero["mp"] += amount_recovered
        print(f"{hero_name} recharged for {amount_recovered} MP!")

    elif action == "Heal":
        amount = int(tokens[2])
        amount_recovered = min(amount, 100 - hero["hp"])
        hero["hp"] += amount_recovered
        print(f"{hero_name} healed for {amount_recovered} HP!")

for hero in heroes:
    print(f"{hero['name']}\n  HP: {hero['hp']}\n  MP: {hero['mp']}")