# Return a new list that is the result of
# adding element to the head (i.e. front) of input_list
def attach_head(element, input_list):
    return [element] + input_list


print(attach_head(1,                     # Will return [1, 46, -31, "hello"]
            attach_head(46,              # Will return [46, -31, "hello"]
            attach_head(-31,             # Will return [-31, "hello"]
            attach_head("hello", []))))) # Will return ["hello"]
