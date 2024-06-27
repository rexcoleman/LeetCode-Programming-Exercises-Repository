data = [[0.4, 0.1], [0.5, 0.25], [0.6, 0.55], [0.7, 0.75], [0.8, 0.85]]


def x_bar_y_bar(data):
    sum_x = 0
    sum_y = 0
    for x, y in data:
        sum_x += x
        sum_y += y
    x_bar = sum_x / len(data)
    y_bar = sum_y / len(data)

    return x_bar, y_bar

def m_numerator(data, x_bar):
    numerator = 0
    denominator = 0
    for x, y in data:
        numerator += (x - x_bar) * y
        denominator += (x - x_bar) ** 2
    m = numerator / denominator
    return m



if __name__ == '__main__':
    x_bar, y_bar = x_bar_y_bar(data)
    gradient = m_numerator(data, x_bar)
    intercept = y_bar - (gradient * x_bar)

    print(f"m = {gradient}, c = {intercept}")


