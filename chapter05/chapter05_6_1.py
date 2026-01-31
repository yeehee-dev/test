import pickle
f = open("foo.txt",'wb')
data = {1: 'python', 2:'you need'}
pickle.dump(data,f)
f.close()