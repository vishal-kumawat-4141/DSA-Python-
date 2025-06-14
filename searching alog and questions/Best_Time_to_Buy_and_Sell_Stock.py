#  Best Time to Buy and Sell Stock ....
# method 1:--> T.C = O(n(n+1)/2) ~~~O(n^2)  , S.C = O(1)
# price = [7, 2, 1, 5, 6, 4, 8]


# def profit(price):
#     # maxx = float("-inf")
#     # if len(price) == 1 or len(price) == 0:
#     #     return 0
#     maxx = 0
#     for i in range(0, len(price)):
#         for j in range(i + 1, len(price)):
#             if price[j] > price[i]:
#                 total = price[j] - price[i]
#                 maxx = max(maxx, total)
#     return maxx


# print(profit(price))


# method 2:----> T.C = O(n)  , S.C = O(1)

price = [7, 2, 1, 5, 6, 4, 8]


def max_profit(price):
    minn = float("inf")
    maximum_profit = 0
    for i in range(0, len(price)):
        minn = min(minn, price[i])
        maximum_profit = max(maximum_profit, price[i] - minn)

    return f"maximun profit is : {maximum_profit}"


print(max_profit(price))
