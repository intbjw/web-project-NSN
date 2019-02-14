### 简述python中的@staticmethod作用及用法
关于@staticmethod,这里抛开修饰器的概念不谈，只简单谈它的作用和用法。
<br>@staticmethod用于修饰类中的方法,使其可以在不创建类实例的情况下调用方法，这样做的好处是执行效率比较高。当然，也可以像一般的方法一样用实例调用该方法。该方法一般被称为静态方法。静态方法不可以引用类中的属性或方法，其参数列表也不需要约定的默认参数self。我个人觉得，静态方法就是类对外部函数的封装，有助于优化代码结构和提高程序的可读性。当然了，被封装的方法应该尽可能的和封装它的类的功能相匹配。
<br>这里给出一个样例来直观的说明一下其用法。
```python
class Time():
    def __init__(self,sec):
        self.sec = sec
    #声明一个静态方法
    @staticmethod
    def sec_minutes(s1,s2):
        #返回两个时间差
        return abs(s1-s2)

t = Time(10)
#分别使用类名调用和使用实例调用静态方法
print(Time.sec_minutes(10,5),t.sec_minutes(t.sec,5))
#结果为5 5
```
