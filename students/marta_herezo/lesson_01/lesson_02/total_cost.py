print('Give A - dollars: ')
A = int(input())

print('Give B - cents: ')
B = int(input())

print('Give N - numbers of cupcakes: ')
N = int(input())

cents = B / 100
print(cents)

#rr = (((A + cents)*N) % 1) * 100
#print(str(int(-(-rr))))

print('Your order will cost: ' + str((A+cents)*N))