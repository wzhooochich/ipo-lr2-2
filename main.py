apples=int(input("введите количество яблок: "))
students=int(input("введите количество учеников: "))
ost=apples%students
apples-=ost
res=apples/students
print("в корзинке останется ",ost,"яблок")
print("каждому ученику достанется",res,"яблок")