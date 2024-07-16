def take_magic_damage(health, resist, amp, spell_power):
    maximum_damage = amp*spell_power
    actual_damage = maximum_damage - resist
    return health - actual_damage