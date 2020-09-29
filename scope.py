"""This variable refers to the global scope"""
global_scope_name = "Enrique Devars"


def change_name(name="Enrique", lastname="Devars"):
    # This variable is called globale scope to but
    # is refered to the local scpoe of the function
    global_scope_name = name + lastname
    print(f"Name changed! {global_scope_name}")


print(f"My name is {global_scope_name}")
change_name("Miguel", "Morales")
print(f"My name is {global_scope_name}")
change_name()
print(f"My name is {global_scope_name}")
