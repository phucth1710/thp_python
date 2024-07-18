def calculate_experience_points(level):
    total_gained_xp = 0
    i = 1
    while i <= level:
        total_gained_xp += (i - 1) * 5
        i += 1
    return total_gained_xp