class animal:
    def __init__(self,name,age):
        self.age =  age
        self.name = name
        print ("The animal called %s , %s years old !"%(name,age))
    def scream(self):
        print("the animal starts screaming:")

class cat(animal):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        animal.__init__(self,name,age)
        print 'the cat called',self.name
        print 'the cat aged',self.age,'\n\n'
    def scream(self):
        animal.scream(self)
        print("ίχίδίχίδ")

print 'The moudle name is :' , __name__,'\n'

if __name__ =='__main__':
    catname = raw_input('Pls input name:\n')
    catage = raw_input('Pls input age:\n')
    print '\n################\n\n'
    cat = cat(catname,catage)
    cat.scream()

