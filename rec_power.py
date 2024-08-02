def pow(N,P):
    if P==0:
        return 1
    else:
        return N*pow(N,P-1)
#Driver code
N=5
P=2
print(pow(N,P))
#here, time complexity is O(P), and for greater values of P, time complexity increases. Hence, we need to use a different approach in order to reduce the time complexity. REFER TP day6>pow.py