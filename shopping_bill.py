total=0
items=int(input("enter numer of items"))
for i in range(items):
    price=int(input("enter price"))
    total=total+price
average=total/items
print('total=',total)
print('average=',average)
    

