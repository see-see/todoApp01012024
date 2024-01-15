def readfile():
    with open("todolist", "r") as f:
        todo = f.readlines()
    return todo


def writefile(todo):
    with open('todolist', 'w') as f:
        f.writelines(todo)

