# for loop W, profit, weight, weight< W = sub(W-weight), then add profit 1st profit, 2nd profit, sub
# profit*W/weight

class greedy:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

    # to sort the weight and profit


def find_profit(W, arr):
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)

    # to get the fianl result
    final_result = 0.0

    # iterate to each item
    for greedy in arr:
        if greedy.weight <= W:
            W -= greedy.weight
            final_result += greedy.profit

        else:
            final_result += greedy.profit * W / greedy.weight
            break

        return final_result


if __name__ == "__main__":
    W = 50
    arr = [greedy(60, 10), greedy(100, 20), greedy(120, 30)]

    # Function call
    max_val = find_profit(W, arr)
    print(max_val)
