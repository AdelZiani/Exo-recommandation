
def est_palindrome(mot):
    n = len(mot)
    for i in range(n // 2):
        if mot[i] != mot[n - i - 1]:
            return False
    return True
