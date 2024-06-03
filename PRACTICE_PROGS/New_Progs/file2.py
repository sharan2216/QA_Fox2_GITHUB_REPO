
# Reverselist:----------
# def meth(list):
#     list2=[]
#     list2=list[::-1]
#     print(list2)
#
# list=[1,2,3,4,5]
# meth(list)

def meth(list):
    l=[]
    for i in list:
        if i%2!=0 and i%3!=0:

            l.append(i)
    print(l)
    l=l[::-1]
    print(l)
    print(l[0])


list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
meth(list)