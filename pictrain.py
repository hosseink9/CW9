import pickle
import pathlib

class Person:

    def __init__(self,name,age,nationality):
        self.name=name
        self.age=age
        self.nationality=nationality
    def __str__(self):
        return f'{self.name= }, {self.age= }, {self.nationality= }'

p1=Person('hossein','22','iranian')

def read_file(a): 
    with open(a,'rb') as f:
        info=pickle.load(f)
        return info

def write_file(b,info):
    with open(b,'wb') as f:
        pickle.dump(info,f)

def save_object(obj):
    info_file=pathlib.Path("obj.pickle")
    if info_file.exists():
        info=read_file("obj.pickle")

        info.append(obj)

        write_file("obj.pickle", info)
    else:
        with open("obj.pickle", 'wb') as f:
            pickle.dump([obj], f)

if __name__ =="__main__":
    save_object(p1)

    info = read_file("obj.pickle")

    for i in info:
        print(i)