#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if n < 0: return 0
    if n == 0: return 1
    
    ways_to_eat = [3,2,1]; diff_ways = 0; i = 0

    def find_ways_to_eat(ttl_cookies, j):
        if ttl_cookies - ways_to_eat[j] == 0:
           nonlocal diff_ways
           diff_ways += 1
        elif ttl_cookies - ways_to_eat[j] > 0:
            ttl_cookies -= ways_to_eat[j]
            for b, way in enumerate(ways_to_eat):
                find_ways_to_eat(ttl_cookies, b)
    
    for i, way in enumerate(ways_to_eat):
        find_ways_to_eat(n, i)

    return diff_ways

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')