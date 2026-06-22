prices = (10,20,30,40,50) # print out 20 , 30, 40

# update 30 to 300 
# this cannot happen
# prices[2] = 300
# prices(prices)

# we can do also do it 
temp= list(prices)
temp[2] = 300
prices = tuple(temp)
print(prices)