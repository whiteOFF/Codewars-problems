def is_ham_dividable(n) -> bool:
    if n==1:
        return True
    elif n%2==0:
        return is_ham_dividable(n/2)
    elif n%3==0:
        return is_ham_dividable(n/3)
    elif n%5==0:
        return is_ham_dividable(n/5)
    else: return False

def ham_coefficients(n):
    i,j,k = 0,0,0
    while n!=1:
        if n%2==0:
            n /= 2
            i += 1
        elif n%3==0:
            n /= 3
            j += 1
        elif n%5==0:
            n /= 5
            k += 1
    return [i,j,k]

def hamming(n:int) -> int:
    if n == 1:
        return 1
    elif n<=100:
        c = 2
        total_counter = 2
        while c != n+1:
            while not is_ham_dividable(total_counter):
                total_counter += 1
            total_counter += 1
            c += 1
        return total_counter-1
    else:
        total_counter = 1536
        c = 100


print(hamming(100))
print(hamming.__annotations__)
