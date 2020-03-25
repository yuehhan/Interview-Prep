# There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], 
# and the cost of flying the i-th person to city B is costs[i][1].
# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.    

# Use a Greedy algorithm
def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    total = 0
    
    # sort by the difference of prices
    costs.sort(key = lambda x: x[0] - x[1])
    n = len(costs)//2
    
    for i in range(n):
        total += costs[i][0] + costs[i + n][1]
    
    return total