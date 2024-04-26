# Longest Character without repeating characters

"""


"""

# Brute Force | Using Dictonary
def longest_substring_without_repeating_chars(s:str)->int:

    n = len(s)

    if n == 0:
        return 0
    

    maxans = -1


    for i in range(n):
        set = {}

        for j in range(i,n):

            if s[j] in set: # Not Unique
                maxans = max(maxans, j-i)
                break

            set[s[j]] = 1

        return maxans


# Optimal Approach Dry Run

"""
DRY RUN

ind  0 1 2 3 4 5 6 7 8 9
s = "a b c a a b c d b a"

i = 0 , num[i] = a

l = 0, r = 0 , maxan = 1 , set = {(a, 0)}

----
i = 1 , num[i] = b
l = 0
r = 1

b exist in set -- No  , set = {(a, 0), (b, 1)} , maxan = 2

----
i = 2, num[i] = c
l = 0
r = 2

c exist in set -- No  , set = {(a, 0), (b, 1), (c, 2)} , maxan = 3

----
i = 3 , num[i] = a
l = 0
r = 3

a exist in set --- Yes, at index 0
so move the left pointer index to a->index + 1 , i.e 0+1 = 1
why? so that in our new range l r, we will not have the repeating character a

now update the index of a to 3, in the set

set = {(a, 3), (b, 1), (c, 2)} , maxan = 3

---
i = 4 , num[i] = a
l = 1
r = 4

a exist in set --- Yes, at index 3
so move the left pointer index to a->index + 1 , i.e 3+1 = 4
why? so that in our new range l r, we will not have the repeating character a

now update the index of a to 4, in the set

set = {(a, 4), (b, 1), (c, 2)} , maxan = 3

---
i = 5 , num[i] = b
l = 4
r = 5

b exist in set -- Yes, but at index 1 which is less than l
so will update the index of b in set and move ahead

set = {(a, 4), (b, 5), (c, 2)} , maxan = 3

---
i = 6, num[i] = c
l = 4
r = 5

c exist in set -- Yes, but at index 2 which is less than l
so will update the index of c in set and move ahead

set = {(a, 4), (b, 5), (c, 6)} , maxan = 3

---

i = 7 , num[i] = d
l = 4
r = 7

d exist in set -- No
set = {(a, 4), (b, 5), (c, 6), (d, 7)} , maxan = 4

---
i = 8 , num[i] = b
l = 4
r = 8

b exist in set -- Yes, at index 5
so move the left pointer index to b->index + 1 , i.e 5+1 = 6
why? so that in our new range l r, we will not have the repeating character b

now update the index of b to 8, in the set

set = {(a, 4), (b, 8), (c, 6), (d, 7)} , maxan = 4

---
i = 9, num[i] = a
l = 6
r = 9

a exist in set -- Yes, at index 4 which is less than l
so will update the index of a in set and move ahead

set = {(a, 9), (b, 8), (c, 6), (d, 7)} , maxan = 4

loop ends ####


"""

# TC - O(N), SC - O(N)
def longest_substring_without_repeating_chars_optimal(s:str)->int:

    n = len(s)
    mpp = [-1]*256

    left = 0
    right = 0
    maxen = 0


    while right<n:

        key = ord(s[right])

        if mpp[key] != -1: # Similar to mapp.containsKey(s.chartAt[i])
            left = max(left, mpp[key]+1)
        
        mpp[key] = right
        maxen = max(maxen, right-left+1)
        right+=1

    return maxen