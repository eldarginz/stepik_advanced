from decimal import *
num = Decimal(input())
num_tuple = num.as_tuple()
if int(num) == 0:
    print(max(num_tuple.digits))
else:
    print(min(num_tuple.digits)+max(num_tuple.digits))
