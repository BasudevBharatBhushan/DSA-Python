"""
Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Recurance Relation
-------------------------

From observation, it could be found that
ultimately who has the 2 at the end will win.


so if n is even, Alice will always win
and if n is odd Alice will loose


"""
# RECURSION

def divisor_game(n:int)->bool:

    # # Base Case
    if n<=1:
        return False

    # # Recursive Soltion
    # Run the loop for Alice and let recursion handle the case of Bob

    for x in range(1, n):
        if n%x == 0:

            # # Bob gets a chance to play
            return not divisor_game(n-x)

        
    return False


# TABULATION