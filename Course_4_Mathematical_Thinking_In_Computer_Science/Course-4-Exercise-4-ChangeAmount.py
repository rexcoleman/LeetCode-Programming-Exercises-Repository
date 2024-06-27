def change(amount):
    if amount == 24:
        return [5, 5, 7, 7]
    if amount == 25:
        return [5, 5, 5, 5, 5]
    if amount == 26:
        return [7, 7, 7, 5]
    if amount == 27:
        return [7, 5, 5, 5, 5]
    if amount == 28:
        return [7, 7, 7, 7]
    if amount > 28:
        result = change(amount - 5)
        result.append(5)
        return result

    # complete this method
print(change(37))