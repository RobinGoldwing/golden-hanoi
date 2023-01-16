

# def Mover():
#     final = torres
#     mientras final > 1
#         saca 1º de torre 1 > torre final
#         final -=1
#     mientras disco origen < disco destino
#         mover disco 
        
#         saca 1º de torre 1 > torre final-1
#     saca


# def hanoi_lower_bound(n, k):
#     return 2**n - 1 - (k-1)**n

# print(hanoi_lower_bound(5, 5))

def hanoi_lower_bound(n, k):
    h_prime = 0
    for h in range(k):
        h_prime += (k-1+h)*(2**h) + (n-(k+n))*2**(n+1)
    return h_prime

print(hanoi_lower_bound(3, 2))