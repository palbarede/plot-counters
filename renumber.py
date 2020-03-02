def renumber(list1):
    """Renumbers sorted list minimally (like RENUM in BASIC language) beginning with 0."""
    list2=[]+list1
    i=0
    downshift=list2[0]
    while True:
        list2[i]-=downshift
        if i>=len(list2)-1: # if last element break out
            break
        if list2[i+1]-downshift>list2[i]+1:
            downshift += list2[i+1]-downshift-(list2[i]+1)
        i+=1
    return list2

# # test
# list1=[3,3,5,8,10,10,13,15,15]
# #list1=[-3,-3,-3,5,5,5,7,7,9]
# list2=renumber(list1)
# for i in range(len(list1)):
#     print(list1[i],list2[i])
