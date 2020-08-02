def numerus(roman): 
    romans = list(roman)
    letters = ['i', 'v', 'x', 'l', 'c', 'm']  
    values = [1, 5, 10, 50, 100, 1000] 

    total = 0
    prev_index = -1

    for r in romans:
        if r not in letters:
            return "This is not a roman number.!!"
        else:
            rindex = letters.index(r)
            if prev_index == -1:
                total += values[rindex]
            elif prev_index == rindex:
                total += values[rindex]
            elif prev_index > rindex:
                total -= values[rindex]
            elif prev_index < rindex:
                total += values[rindex]
            prev_index = rindex
    return total

numerus('xiv')


