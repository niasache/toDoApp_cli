def get_todos(filepath):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath):
    with open(filepath, 'w') as file:
        file.writelines(todos)
