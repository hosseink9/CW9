def dic(*args):
    newdic={}
    for key, value in enumerate(args):
        newdic[key+1]=value
    return newdic
    
print(dic(1,2,3,4,'mahdi','farzam','mohammad'))