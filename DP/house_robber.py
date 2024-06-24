"""
HOUSE ROBBER PROBLEM

2 3 2 ---> here 2 and 2 will be adjacent because houses are in circular order

Clearly, answer can either include the first element or the last element

so two cases arises

1[]. -----houses------- *[exclude last element]             ans1 = max_sum_of_non_adjacent(1[])
2[]. [exclude first element] -----houses-------             ans2 = max_sum_of_non_adjacent(2[])

ans = max(ans1, ans2)



"""
from max_sum_of_non_adjacent_elements import max_sum_tabulation_optimized


def house_robber(a):
    if len(a) == 1:
        return a[0]
    
    ans1 = max_sum_tabulation_optimized(a[:-1])
    ans2 = max_sum_tabulation_optimized(a[1:])
    
    return max(ans1, ans2)



# Test Cases
a = [2,3,2]
print(house_robber(a)) # 3