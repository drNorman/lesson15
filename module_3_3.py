print("1st Task\n") #1st Task

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(55, 'OK')
print_params(b = 25)
print_params(c = [1, 2, 3])


print("\n2nd Task\n") #2nd Task

value_list = [999, 'entertainment', 3.14]
value_dict = {'a':108, 'b':'xyz', 'c':False}
print_params(*value_list)
print_params(**value_dict)


print("\n3rd Task\n") #3rd Task

value_list_2 = [220, 'AC/DC']
print_params(*value_list_2, 42)
























