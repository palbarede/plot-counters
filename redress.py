
def redress(list1:list)->list:
    """Downshifts first values so that the sequence is increasing (not strictly) but the last element is unchanged."""
    list2=[]+list1 # /!\ make a local copy
    list2.reverse() # of course beginning from the end is much easier
    # the reversed list must made decreasing
    i=0
    downshift=0
    while True:
        list2[i]-=downshift
        if i>=len(list2)-1:
            break
        if list2[i+1]-downshift>list2[i]: 
            downshift+=list2[i+1]-downshift-list2[i]
            # position with respect to the original list
            print('Warning: downshift',downshift,'at position',len(list1)-i-2,".")
        i+=1
    list2.reverse()
    return list2

   #import ipdb; ipdb.set_trace()
   #sys.exit()

# # uncomment for testing
# #list1=[80,86,90,95,100,5,10,12,15,17,24,0,2,4,5]
# list1=[10,18,20,20,21,24,0,3,6,7,0,3,7,9]
# list2=redress(list1)
# for i in range(len(list1)):
#     print(i,list1[i],list2[i])
# import pandas as pd
# import matplotlib.pyplot as plt
# #list1.reverse()
# #list2.reverse()
# df=pd.DataFrame([list1,list2])
# df.T.plot()
# plt.show()
