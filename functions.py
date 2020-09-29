def invert_name(name="Enrique", lastname="Devars",invert=False):
    if invert:
        print(lastname,name)
    else:
        print(name,lastname)

invert_name()
invert_name("Linda","Fernandez", True)
invert_name("Linda","Fernandez")