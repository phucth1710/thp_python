def get_most_common_enemy(enemies_dict):
    if enemies_dict == {}:
        return None

    most_common_appearance = float('-inf')

    for key in enemies_dict:
        value = enemies_dict[key]
        if value > most_common_appearance:
            most_common_appearance = value
            enemies_highest_count = key

    return enemies_highest_count