def k(heads, legs):
    rabbits = (legs - 2 * heads) / 2
    chickens = heads - rabbits
    return ("rabbits:", rabbits),  ("chickens:", chickens)

heads = 35
legs = 94
print(k(heads, legs))