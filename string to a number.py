def get_index(data_list, a_string):
    result = 0
    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number
    list_index = result % len(data_list)
    return list_index

def is_index_equal(data_list, a_string, given_value):
    list_index = get_index(data_list, a_string)
    return list_index == given_value

# Test the functions
data_list = [None]*48
print(get_index(data_list, "Aakash"))  # Output the index
print(is_index_equal(data_list,"Aakash", 9)) 
print(is_index_equal(data_list,"Aakash", 10)) 
print(get_index(data_list, "hemant"))
