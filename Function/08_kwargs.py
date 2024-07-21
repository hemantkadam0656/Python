def print_kwargs(**kwargs):
    # print("Name:",name , " age:", age)
    for key, value in kwargs.items():
        print(f"{key} : {value}")




print_kwargs(name="Henant", age="26", cmp="tcs")