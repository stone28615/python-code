with open("new_file2.txt", "r") as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break

with open("loveletter.txt", "r",encoding="gb2312") as f:
    for line in f.readlines():
        print(line)

with open("loveletter.txt", "r") as f:
    for line in f.readlines():
        print(line)