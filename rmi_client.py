import Pyro4

name = input("What is your name?").strip()

greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")
print(greeting_maker.get_fortunate(name))
