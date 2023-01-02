import numpy as np





a = np.array([])
b = np.array([1,2])
c = np.array([1,5])
d = np.concatenate(([b],[c]), axis = 0)
#print(np.isin(d, c))
print(np.all(c==d, axis=1))
print(np.any(np.all(c == d, axis=1)))
np.any(np.isin(b, c))
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
