
def redress(list1):
    """Shifts elements so that the sequence is just increasing and the last element is unchanged"""
    #print(list1)
    #import ipdb; ipdb.set_trace()
    #sys.exit()
    list2=[]+list1# /!\ make a local copy
    list2.reverse()
    i=0
    downshift=0
    y=list2[0]
    while i<len(list2)-1:
        x=y
        y=list2[i+1]-downshift
        if y>x: # False is x or y is nan
            downshift+=y-x
            print('Warning: downshift',downshift,'at position',len(list1)-i-2,".")
        list2[i+1]-=downshift
        y=list2[i+1]
        i+=1
    list2.reverse()
    return list2

# test
from numpy import nan
#list1=[49514.0, 49675.0, 50394.0, 51090.0, 51265.0, 51386.0, 51552.0, 51595.0, 51824.0, 51889.0, nan, 52358.0, 52434.0, 52451.0, 52712.0, 52759.0, 53087.0, nan, 53087.0, 450.0, 655.0, 696.0, 859.0, nan, nan, 1222.0, 1555.0, 1882.0, 1981.0, nan, 2011.0, 2023.0, 2238.0, 2535.0, 2619.0]
#list1=[80,86,90,95,100,5,10,12,15,17,24,0,2,4,5]
list1=[21,24,0,3,6,7,0,3,6,9]
list2=redress(list1)
for i in range(len(list1)):
    print(i,list1[i],list2[i])

