def format_name(f_name,l_name):
    #docstring
    """Take a first and last name
        and return the names with title case version
    """
    format_f_name = f_name.title()
    format_l_name  = l_name.title()

    return f"{format_f_name} {format_l_name}"

print(format_name("christian","GASPAR"))


def func_1(text):
    return text + text

def func_2(text):
    return text.title()

output = func_1("my namE ")

final_output=func_2(output)


# can add function to name you want and use it

def add(n1, n2):
    return n1 + n2

my_fav_operation = add

print(my_fav_operation(1,2))
