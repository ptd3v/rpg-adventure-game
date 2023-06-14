#Assumed damage is 1d20, DnD based combat system.

def hit_points(hp):
    con = 10
    max_hp = con * 10
    current_hp = max_hp - damage_taken
    damage_taken = enemy_damage
    enemy_damage = enemy_str
    enemy_str = 10
    return con, max_hp, current_hp, damage_taken, enemy_damage, enemy_str

    print(con, max_hp, current_hp, damage_taken, enemy_damage, enemy_str)
    print(max_hp)
    print(hit_points)
    print(hp)

    #1d20 Dice Roll could be an awesome idea.
