
# program print grade according to subject marks

a = input("marks of science? ")
b = input("marks of maths? ")
c = input("marks of english? ")
d = input("marks of physics? ")
a = int(a)
b = int(b)
c = int(c)
d = int(d)
sum = (a+b+c+d)
p = ((sum/400)*100)
if p >= 90:
    print('A')
elif p >= 80 and p < 90:
    print('grade B')
elif p >= 70 and p < 80:
    print('grade C')
elif p >= 60 and p < 70:
    print('grade D')
else:
    print('fail')