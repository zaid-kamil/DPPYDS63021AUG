class Hello:
    # class attributes
    info = "hello class"
    version = 1.0    

    # instance method
    def world(self):
        print("Hello, World!")

    # instance method
    def india(self):
        print("Hello, India!")

obj = Hello()
obj.world()
obj.india()
print(obj.info)
print(obj.version)

abc = Hello()
abc.world()
abc.info = 'abc property h ye' # changed class attribute
print(abc.info)
print(Hello.info)