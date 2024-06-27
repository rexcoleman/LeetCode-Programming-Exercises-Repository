class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        self.stack.append([price, ans])

        return ans


if __name__ == '__main__':

    commands_1 = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
    daily_temps_1 = [[], [100], [80], [60], [70], [60], [75], [85]]
    expected_output_1 = [None, 1, 1, 1, 2, 1, 4, 6]

    stock_spanner = StockSpanner()
    output = [None]
    for i in range(1, len(commands_1)):
        output.append(stock_spanner.next(daily_temps_1[i][0]))

    print(f"\nTest Output: {output} \nExpected Output: {expected_output_1}")