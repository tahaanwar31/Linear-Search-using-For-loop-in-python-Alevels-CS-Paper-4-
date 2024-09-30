arraydata=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def LinearSearch(number,array):
    for x in range(len(array)):
        if array[x]==number:
            return x
    return -1
num=int(input("Please enter the number you want to search: "))
result=LinearSearch(num,arraydata)
if result != -1:
    print("The number was found on ",result)
else:
    print("The number was not found in array")
