def compute_position(item, n):
    dots = []
    index = item[0]
    direction = item[1]
    x = (index - 1) % n
    y = (index - 1) // n
    if direction == "L":
        dots.append((x, y))
        dots.append((x + 1, y + 1))
    else:
        dots.append((x, y + 1))
        dots.append((x + 1, y))
    return dots


def can_extend(combination, n):
    dots_list = []
    for item in combination:
        dots = compute_position(item, n)
        dots_list.extend(dots)
    dots_set = set(dots_list)
    if len(dots_list) != len(dots_set):
        return False
    else:
        return True


def backtrack_with_direction(combination, start, k, n, directions):
    if k == 0:
        print(combination)
        # exit()
        return
    for i in range(start, n * n):
        for j in range(2):
            combination.append([i + 1, directions[j]])
            if can_extend(combination, n):
                backtrack_with_direction(combination, i + 1, k - 1, n, directions)
            combination.pop()


directions = ["L", "R"]
backtrack_with_direction([], 0, 16, 5, directions)