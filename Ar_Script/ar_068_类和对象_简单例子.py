class Animal:

    weigth=0
    height=0

    def run(self):
        print('这是一个跑的方法')

    def eat(self):
        print('这是一个吃东西的方法')

'将属性和方法封装起来建立一个动物类'

'实例化一个猫的实例对象'
cat=Animal()
'调用动物类的方法'
cat.eat()

'继承'
class Dog(Animal):
    # pass

    def eat(self):
        print('这是小狗在吃东西')

class Bird(Animal):

    def eat(self):
        print('这是小鸟在吃东西')
dog=Dog()
bird=Bird()

'多态,同一个调用方法因为对象不同而显示不同的内容'
dog.eat()
bird.eat()

