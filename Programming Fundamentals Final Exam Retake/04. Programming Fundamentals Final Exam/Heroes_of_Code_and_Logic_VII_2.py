class Hero:


    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.max_hp = 100
        self.max_mp = 200


    def cast_spell(self, mp_needed, spell_name):
        if mp_needed <= self.mp:
            self.mp -= mp_needed
            print(f"{self.name} has successfully cast {spell_name} and now has {self.mp} MP!")
        else:
            print(f"{self.name} does not have enough MP to cast {spell_name}!")


    def take_damage(self, damage, attacker):
        self.hp = max(0, self.hp - damage)
        if self.hp > 0:
            print(f"{self.name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!")
        else:
            print(f"{self.name} has been killed by {attacker}!")


    def recharge(self, amount):
        amount_recovered = min(amount, self.max_mp - self.mp)
        self.mp += amount_recovered
        print(f"{self.name} recharged for {amount_recovered} MP!")


    def heal(self, amount):
        amount_recovered = min(amount, self.max_hp - self.hp)
        self.hp += amount_recovered
        print(f"{self.name} healed for {amount_recovered} HP!")


    def __str__(self):
        return f"{self.name}\n  HP: {self.hp}\n  MP: {self.mp}"


n = int(input())

heroes = []
for i in range(n):
    hero_data = input().split()
    hero = Hero(hero_data[0], int(hero_data[1]), int(hero_data[2]))
    heroes.append(hero)

while True:
    command = input()
    if command == "End":
        break

    tokens = command.split(" - ")
    action = tokens[0]
    hero_name = tokens[1]
    hero = next((h for h in heroes if h.name == hero_name), None)

    if hero is None:
        continue

    if action == "CastSpell":
        mp_needed = int(tokens[2])
        spell_name = tokens[3]
        hero.cast_spell(mp_needed, spell_name)

    elif action == "TakeDamage":
        damage = int(tokens[2])
        attacker = tokens[3]
        hero.take_damage(damage, attacker)
        if hero.hp == 0:
            heroes.remove(hero)

    elif action == "Recharge":
        amount = int(tokens[2])
        hero.recharge(amount)

    elif action == "Heal":
        amount = int(tokens[2])
        hero.heal(amount)

for hero in heroes:
    print(hero)