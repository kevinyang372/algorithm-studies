# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].

# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

# According to the example above:

# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

def calcEquation(self, equations, values, queries):
    d = collections.defaultdict(dict)
    
    for i, (x, y) in enumerate(equations):
        d[x][y] = values[i]
        d[y][x] = 1 / values[i]
    
    cache = {}
    def dfs(entry, target, visited = []):
        if entry == target: return 1
        if (entry, target) in cache: return cache[entry, target]
        
        for i in d[entry]:
            if i not in visited:
                temp = dfs(i, target, visited + [entry])
                if temp != -1:
                    cache[entry, target] = d[entry][i] * temp
                    return d[entry][i] * temp
        return -1
            
        
    res = []
    for x, y in queries:
        if x not in d or y not in d:
            res.append(-1.0)
        elif x == y:
            res.append(1.0)
        else:
            res.append(dfs(x, y))
    
    return res
    