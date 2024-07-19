def remove_duplicates(spells):
    set_learned_spells = set()
    list_learned_spells = []

    for i in spells:
        set_learned_spells.add(i)

    for j in set_learned_spells:
        list_learned_spells.append(j)

    return list_learned_spells