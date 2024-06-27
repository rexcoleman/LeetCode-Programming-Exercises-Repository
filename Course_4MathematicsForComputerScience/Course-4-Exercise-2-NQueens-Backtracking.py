def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True

def extend(perm, n):
    global count
    if len(perm) == n:
        count += 1
        print(perm)

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n)

            perm.pop()

if __name__ == '__main__':
    count = 0
    extend(perm = [], n = 8)
    print(count)