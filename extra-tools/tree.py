import os

def generate_tree(path, prefix=""):
    if not os.path.isdir(path):
        return f"{path} is not a valid directory."

    contents = os.listdir(path)
    pointers = ['├── '] * (len(contents) - 1) + ['└── ']
    
    tree = []
    for pointer, name in zip(pointers, contents):
        tree.append(prefix + pointer + name)
        subpath = os.path.join(path, name)
        if os.path.isdir(subpath):
            extension = '│   ' if pointer == '├── ' else '    '
            tree.append(generate_tree(subpath, prefix + extension))

    return "\n".join(tree)

# Example usage:
path = "."  # Replace with the path to the directory you want to list
print(generate_tree(path))
