# Modify the name of the file
def modify_name(filename):
    filename += ".txt"
    filename = "my_" + filename
    return filename
def modify_name_nonpara():
    filename = "syc.txt"
    filename = "nonpara function _" + filename
    return filename


new_filename = modify_name("f1")
print(new_filename)
new_filename = modify_name_nonpara()
print(new_filename)