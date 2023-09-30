def modify_name(filename):
    filename += ".txt"
    filename = "my_" + filename
    return filename

new_filename = modify_name("f1")
print(new_filename)
