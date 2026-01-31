import pickle
f = open("foo.txt",'rb')
data = pickle.load(f)
print(data)