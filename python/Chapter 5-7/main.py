def unlock_achievement(before_xp, ach_xp, ach_name):
    player_xp = before_xp + ach_xp
    # print("player_xp : " + str(player_xp))
    alert = "Achievement Unlocked: " + ach_name
    # print("alert: " + alert)
    return player_xp, alert