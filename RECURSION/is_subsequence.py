"""

RECURSIVE SOLUTION

f(index ,str, pattern, n = len(str), index_pattern)

# # Base case

if len(pattern) == 0
    return True

if i == n:
    return False


Recursive Solution
--------------------------

if str(index) == pattern(index_pattern)
    index = index_pattern+1

 return f(index+1, str, pattern, n, index_pattern)



"""

def is_subsequence(s:str, t:str ,si:int, ti:int)->bool:
        ## s = main string
        ## t = pattern string
        ## si = index of s
        ## ti = index of t

    # # Base Cases
    
    if ti == len(t):
        return True

    if si == len(s):
        return False
    
    # # Recursive Function
    
    if s[si] == t[ti]:
        ti = ti+1

    return is_subsequence(s, t, si+1, ti)


# # Tabulation
def is_subsequence_tabulation(s:str, t:str)->bool:

    n = len (s)

    ti = 0
    for si in range(0, n):
        if s[si] == t[ti]:
            ti +=1
        
        if ti == len(t):
            return True
    
    return False


if __name__ == '__main__':
    s = "ahbgdc"
    t = ""

    print(is_subsequence(s, t, 0, 0))
    # print(is_subsequence_tabulation(s, t))    