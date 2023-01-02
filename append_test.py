import numpy as np





#a = np.array([])
#b = np.array([1,2])
#c = np.array([4,5])
#d = np.concatenate(([a],[b]), axis = 0)
#d = np.concatenate(([b],[c]),axis=0)
#print(d)
#print(c)


#ar = np.array([[]])
#np.vstack([ar, [1,2,3]])
#print(ar)



""""a = np.array([[]])
print(a)
a = np.concatenate([a, [513,909]], axis=0)
print(a)
a = np.concatenate([a, [515, 911]], axis=0)
np.vstack([a, [513,909]])
print(a)"""

_list = [[1,2],[3,4],[5,6]]
start = [[7,8]]
new_list = np.append(_list,start,axis=1)
print(new_list)