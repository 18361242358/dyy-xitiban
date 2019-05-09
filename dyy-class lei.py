'''
#学生类
class Student(object):
    def __init__(self,name,age,scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_score(self):
        return max(self.scores)

dyy = Student("yangyang",18,[20,60,90])
#get_name后的括号一定要记得 否则不是调用函数
print(dyy.get_name())
print(dyy.get_age())
print(dyy.get_score())

#字典
class DictClass(object):
    def __init__(self,dict):
        self.dict = dict
    def del_dict(self,key):
        if key not in self.dict.keys():
            #上面用self.dict.keys()注意括号 使用self.dict
            return "没有这个"
        else:
            self.dict.pop(key)
            return "删除成功"

    def get_dict(self,key):
        if key not in self.dict.keys():
            return "这里没有这个"
        else:
            #key用中括号阔
            return self.dict[key]

    def get_key(self):
        return self.dict.keys()

    def update_dict(self,dict2):
        self.dict = dict(self.dict,**dict2)
        return self.dict.values()
d = DictClass({"a":1,"b":2})
print(d.del_dict("c"))
print(d.get_dict("c"))
print(d.get_key())
print(d.update_dict({"c":3}))

#列表类
class ListInfo(object):
    def __init__(self,list_val):
        self.list = list_val

    def add_key(self,key_name):
        if isinstance(key_name,(int,str)):
            self.list.append(key_name)
            print(self.list)
            return"ok"
        else:
            return"我要字符串或者数字"

    def get_key(self,index):
        if 0 <= index <= len(self.list):
            return self.list[index]
        else:
            return "查不到"

    def update_list(self,new_list):
        self.list.extend(new_list)
        return self.list

    def del_list(self):
        if len(self.list) > 0:
            return self.list.pop(-1)
        else:
            return"空的"

list_info = ListInfo([0,4,3,5,6,])
print(list_info.add_key([1,2,3]))
print(list_info.get_key(3))
print(list_info.update_list([1,2,3,4]))
print(list_info.del_list())
'''
#集合操作类
class SetInfo(object):
    def __init__(self,my_set):
        self.sett = my_set

    def add_setinfo(self,keyname):
        self.sett.add(keyname)
        return self.sett

    def get_intersection(self,unioninfo):
        if isinstance(unioninfo,set):
            return self.sett & unioninfo
        else:
            return"传入的不是集合"

    def get_union(self,unioninfo):
        if isinstance(unioninfo, set):
            return self.sett | unioninfo
        else:
            return"传入的不是集合"


    def del_difference(self,unioninfo):
        if isinstance(unioninfo, set):
            return self.sett - unioninfo
        else:
            return"传入的不是集合"

A = set([1,2,3,4,5])
B = set([3,5,6])
setinfo = SetInfo(A)
print(setinfo.add_setinfo(7))
print(setinfo.get_intersection(B))
print(setinfo.get_union("123"))
print(setinfo.get_intersection(B))

