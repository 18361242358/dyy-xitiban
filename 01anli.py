'''
定义是一个学生类，用来形容学生
'''
class Student():
    #一个空类 pass必须有
    pass
mingyue = Student()

#再定义一个类，用来描述听Python的学生
class PythonStudent():
    #用none给不确定赋值
    name = None
    age = 18
    course = "python"

    #def 的缩进层级
    #系统默认有一个self参数

    def doHomework(self):
        print("I 在做作业")

        return None


yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.doHomework()