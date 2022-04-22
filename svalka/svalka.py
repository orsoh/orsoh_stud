test_list = ('11qwer', 22.2, 33, [4, 44], (5, 55), {6, 66}, {7: 77}, True, None)


def deter_type(test_var):
    result = type(test_var)
    print(result)


def converter_float(test_var):
    try:
        result = float(test_var)
    except:
        result = 0
    return result
    
    
def logical_operation(test_var1, test_var2):
    cond1 = isinstance(test_var1, int) or isinstance(test_var1, float)
    cond2 = isinstance(test_var2, int) or isinstance(test_var2, float)
    if cond1 and cond2:
        result = test_var1 - test_var2
    elif isinstance(test_var1, str) and isinstance(test_var2, str):
        result = test_var1 + test_var2
    elif isinstance(test_var1, str) and not isinstance(test_var2, str):
        result = {test_var1: test_var2}
    else:
        result = (test_var1, test_var2)
    return result


for test_var in test_list:
    deter_type(test_var)
    
   
for test_var in test_list:
    converter_result = converter_float(test_var)
    print(converter_result)
    
    
result_list = []

for test_var1 in test_list:
    for test_var2 in test_list:
        operation_result = logical_operation(test_var1, test_var2)
        result_list.append(operation_result)
print(result_list)
print(len(result_list))
