
"""
friends = 5

#friends = friends + 1

#friends += 1

friends -= 1


print(friends)
"""

"""
build in function
x = 3.14
y = 4
z = 5

#result = round(x)

#result = abs(y)
#result = pow(4,3)
#result = max(x,y,z)
#result = min(x,y,z)

print(result)

"""

# import math
#
# x =9.1
# # print(math.pi)
# # print(math.e)
#
# # result = math.sqrt(x)
#
# # result = math.ceil(x)
# result = math.floor(x)
# print(result)
import math
# radius = float(input("Input the radius of a circle: "))
# circumference = 2 * math.pi *radius
#
# print(f"the circumference is: {round(circumference,2)} cm")
# radius = float(input("Input the radius of a circle: "))
# area = math.pi * pow(radius,2)
# print(f"The are of a circle is: {round(area,2)} cm2")

a = float(input("Input the length of side a: "))
b = float(input("Input the length of side b: "))

compute = math.sqrt(pow(a,2)+ pow(b,2))
print(f"Side of C {compute}")
