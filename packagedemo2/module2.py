# import module1
# module1.add(20,30)
# module1.sub(30,20)
# module1.mul(30,20)
# module1.div(30,15)
#
# from module1 import add,div
# add(20,10)
# div(20,10)

# from module1 import *
# add(20,30)
# sub(50,20)
# mul(20,10)
# div(30,5)

# import module1 as a
# a.add(10,50)
# a.div(50,10)
# a.mul(5,5)
# a.sub(50,60)

# import with math
# x = dir(math)
# print(x)

# import math
#
# print(math.sqrt(12))
# print(math.factorial(10))
# print(math.factorial(4))
#####################################################

## Importing Modules from  single package

# import packagedemo2.module1
# packagedemo2.module1.add(20,10)
# packagedemo2.module1.sub(20,10)

# from packagedemo2 import module1
# module1.add(20,10)
# module1.sub(20,10)

## Importing Modules from 2 different packages

# import packagedemo1.bharat
# import packagedemo1.india
# import packagedemo2.module1
# import packagedemo3.M1
# import PackageDemo3.PackageDemo3_Sub1.M2
#
# packagedemo1.bharat.indian()
# packagedemo1.india.indian()
# packagedemo2.module1.add(10,20)
# packagedemo3.M1.add(200,100)
# packagedemo3.PackageDemo3_Sub1.M2.add(10,200)


## From keywo rd
# from packagedemo1 import india
# from packagedemo1 import bharat
# from PackageDemo3.PackageDemo3_Sub1 import M2

# india.indian()
# bharat.indian()
# M2.add(10,20)

# import sys
# sys.path.append("D:/CT16 17 PYTHON AUTOMATION/Pack3")
#
# sys.path.append("D:/CT16 17 PYTHON AUTOMATION/Pack4/Pack5")