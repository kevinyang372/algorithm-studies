# Give an array of salaries. The total salary has a budget. At the beginning, the total salary of employees is larger than the budget. It is required to find the number k, and reduce all the salaries larger than k to k, such that the total salary is exactly equal to the budget.

# Example 1:

# Input: salaries = [100, 300, 200, 400], budget = 800
# Output: 250
# Explanation: k should be 250, so the total salary after the reduction 100 + 250 + 200 + 250 is exactly equal to 800.

# O(N) time
def salaryAdjustment(salaries, budget):

    salaries.sort()

    k = 1
    sums = sum(salaries)
    cur_mean = 0

    if sums <= budget: return max(budget)

    while k < len(salaries) - 1:
        
        sums -= salaries[-k]
        cur_mean = (budget - sums) / k

        if cur_mean >= salaries[-k - 1]:
            return cur_mean

        k += 1

    return budget / len(salaries)

