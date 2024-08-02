class Super:
    #public data member
    var1=None
    #protected data member
    _var2=None
    #private data member
    __var3=None
    #constructor
    def __init__(self,var1,var2,var3):
        self.var1=var1
        self._var2=var2
        self.__var3=var3
    
    #public member function
    def displayPublicmembers(self):
        #accessing public data members
        print("Public data member:",self.var1)
    #protected member function
    def _displayProtectedMembers(self):
        #accessing protected data members
        print("Protected data member:",self._var2)
    #private member function
    def __displayPrivateMembers(self):
        #accessing protected data members
        print("Private data member:",self.__var3)
    #public member function
    def accessPrivateMembers(self):
        #access private member
        self.__displayPrivateMembers()
#derived class/child class
class Sub(Super):
    #constructor
    def __init__(self, var1, var2, var3):
        Super.__init__(self,var1, var2, var3)
    #public member function
    def accessProtectedMembers(self):
        #accessing protected member functions of super class
        self._displayProtectedMembers()
#creating objects
obj=Sub("Hello","all","people!")
#calling public member functions of the class
obj.displayPublicmembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

#object can access protected member
print("Object is accessing protected member:",obj._var2)
#object cannot access private member, so it will generate Attribute
#print(obj.__var3)