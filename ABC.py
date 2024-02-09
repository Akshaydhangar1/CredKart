## Importing Modules from  single package

# import packagedemo2.module1
# packagedemo2.module1.add(20,10)
# packagedemo2.module1.sub(20,10)

# from packagedemo2 import module1
# module1.add(20,10)
# module1.sub(20,10)

## Importing Modules from 2 different packages

# import PackageDemo1.bharat
# import PackageDemo1.india
# import PackageDemo2.Module1
# import PackageDemo3.M1
# import PackageDemo3.PackageDemo3_Sub1.M2
#
packagedemo1.bharat.indian()
packagedemo1.india.indian()
packagedemo2.module1.add(10,20)
packagedemo3.M1.add(200,100)
# packagedemo3.PackageDemo3_Sub1.M2.add(10,200)


## From keyword
# from PackageDemo1 import india
# from PackageDemo1 import bharat
# from PackageDemo3.PackageDemo3_Sub1 import M2
#
# india.indian()
# bharat.indian()
# M2.add(10,20)

# import sys
# sys.path.append("D:/CT16 17 PYTHON AUTOMATION/Pack3")
#
# sys.path.append("D:/CT16 17 PYTHON AUTOMATION/Pack4/Pack5")


