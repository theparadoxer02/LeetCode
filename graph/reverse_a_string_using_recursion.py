
def reverse_string(prefix, string):
    if not string:
        return prefix
    
    top_elem = string.pop()
    prefix += top_elem
    final_res = reverse_string(prefix, string)
    
    return final_res


input_str = "abc"

result = reverse_string("", list(input_str))
print(result)
