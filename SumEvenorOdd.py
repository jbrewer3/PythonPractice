#Write a function named sum_eo with n (positive number) and t(string) as parameters

#if t = e return the sum of all even numbers in the range n
#if t = o return the sum of all odd numbers in the range n


def sum_eo(n, t):
    if t == "e":
        start = 2
    elif t == "o":
        start = 1
    else:
        return -1
    
    return sum(range(start, n, 2))
            

