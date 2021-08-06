def raise_to_power(base_num, pow_num):
    result=1
    for index in range(pow_num):
        result= result*base_num
    return result

base      = int(input("Enter the base number: "))
pwr_number= int(input("Enter the power number: "))


print("the result of that math is " + str(raise_to_power(base,pwr_number)))    