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
'''


Course_list = []


class School(object):
    def __init__(self, school_name):
        self.school_name = school_name
        self.students_list = []
        self.teachers_list = []

    global Course_list

    def hire(self, obj):
        self.teachers_list.append(obj.name)
        print("我们现在聘请一个新老师{}".format(obj.name))

    def enroll(self, obj):
        self.students_list.append(obj.name)
        print("我们又有了一个新学员{}".format(obj.name))


class Grade(School):
    def __init__(self, school_name, grade_code, grade_course):
        super(Grade, self).__init__(school_name)
        self.code = grade_code
        self.course = grade_course
        self.members = []
        Course_list.append(self.course)

        print("我们现在有了{}的{}的{}".format(self.school_name, self.code, self.course))

    def course_info(self):
        print("课程大纲{} 是 day01，day02，day03".format(self.course))


Python = Grade("BJ", 3, 'Python')
Linxu = Grade("CD", 1, "Linux")


class School_member(object):
    def __init__(self, name, age, sex, role):
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        self.course_list = []

        print("我叫{}，我是一个{}".format(self.name, self.role))


stu_num_id = 00


class Students(School_member):
    def __init__(self, name, age, sex, role, course):
        super(Students, self).__init__(name, age, sex, role)
        global stu_num_id
        stu_num_id += 1
        stu_id = course.school_name + "S" + str(course.code) + str(stu_num_id).zfill(2)
        # zfill 填充的作用，当只有一位数时前面填充0， 只能对str类型做操作

        self.id = stu_id
        self.mark_list = {}

    def study(self, course):
        print("我来这里学习{}课，我的学号是{}".format(course.course, self.id))

    def pay(self, course):
        print("我交了1000块钱给{}".format(course.course))
        self.course_list.append(course.course)

    def praise(self, obj):
        print("{}觉得{}课真棒".format(self.name, obj.name))

    def mark_check(self):
        for i in self.mark_list.items():
            print(i)

    def out(self):
        print("我离开了")


tea_num_id = 00


class Teachers(School_member):
    def __init__(self, name, age, sex, role, course):
        super(Teachers, self).__init__(name, age, sex, role)
        global tea_num_id
        tea_num_id += 1
        tea_id = course.school_name + "T" + str(course.code) + str(tea_num_id).zfill(2)
        self.id = tea_id

    def teach(self, course):
        print("我来这里讲{}门课，我的id是{}".format(course.course, self.id))

    def record_mark(self, Date, course, obj, level):
        obj.mark_list["Day" + Date] = level


a = Students("小张", 18, "M", "student", Python)
Python.enroll(a)
a.study(Python)
a.pay(Python)

b = Students("小王", 22, "F", "student", Python)
Python.enroll(b)
b.study(Python)
b.pay(Python)

t = Teachers("小周", 30, "M", "teacher", Python)
Python.hire(t)
t.teach(Python)
t.record_mark('1', Python, a, "A")
t.record_mark("1", Python, b, "B")
t.record_mark('2', Python, a, "A")
t.record_mark("2", Python, b, "A")
print("小王查看了自己的课程")
print(b.course_list)
print("小王查看了自己的成绩")
b.mark_check()
print("小王退出了")
b.out()
print("给好评")
a.praise(t)
