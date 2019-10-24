class A(object):
    __bar = 1
    @staticmethod
    def static_foo():
        print ('Hello, ', A.__bar)
print(A.__bar)
