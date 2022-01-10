#vars
bool_var = True
int_var = 10
float_var = 3.7
string_var = "Hello World"
list_var = ["blue", 1, True, 2.2]
list_comprehension_var = [i for i in range(0, int_var)]
dict_var = {
    "color": "white",
    "plays with lego": False,
    "age(years)": 3.2,
    "species": "rat"
}

#funcs
def hello_world_counter():
    n_hello_worlds = 0
    for i in list_comprehension_var:
        for x in range(0, i):
            print(string_var)
            n_hello_worlds += 1

    return n_hello_worlds


hello_world_count = hello_world_counter()
print(f"Variable int_var produces {hello_world_count} 'Hello_Worlds'" )
