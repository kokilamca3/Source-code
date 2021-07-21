num=371
result=0
temp=num
while num>0:
    remainder=num%10
    result=result+remainder**3
    num=num//10
print(result)
if result==temp:
    print("The mentioned numer is armstrong number")
else:
    print("The mentioned number is not a armstrong number")
