numlist = [8,3,5,1]
index = 0
integer = 0
for power in range((len(numlist) - 1),-1 ,-1):
    digit = numlist[index]
    number = digit*(10**power)
    integer +=number 
    index +=1
print(integer)
