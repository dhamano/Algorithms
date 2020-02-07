#!/usr/bin/python

import argparse

def find_max_profit(prices):
    profit = [];

    for i in range(1, len(prices)):
        profit.append({"start": prices[i-1], "next": prices[i], "profit":prices[i]-prices[i-1]})

    max_profit = profit[0]["profit"]
    
    for i in range(0, len(profit)):
        if profit[i]["profit"] > max_profit:
            max_profit = profit[i]["profit"]

    return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))