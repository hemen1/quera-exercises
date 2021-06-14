def fruits(tuple_of_fruits: tuple):
    good_fruits = {}
    for fruit in tuple_of_fruits:
        if (fruit['shape'] == 'sphere') and (300 <= fruit['mass'] <= 600) and (100 <= fruit['volume'] <= 500):
            good_fruits[fruit['name']] = good_fruits.get(fruit['name'], 0) + 1
    return good_fruits
