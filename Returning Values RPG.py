# Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes..
# then add this number to the amount of seconds in 45 minutes and 15 seconds.

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
