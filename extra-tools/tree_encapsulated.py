import os

def generate_tree(path="."):
    def _generate_tree(current_path, prefix=""):
        contents = os.listdir(current_path)
        pointers = ['├── '] * (len(contents) - 1) + ['└── ']

        tree = []
        for pointer, name in zip(pointers, contents):
            tree.append(prefix + pointer + name)
            subpath = os.path.join(current_path, name)
            if os.path.isdir(subpath):
                extension = '│   ' if pointer == '├── ' else '    '
                tree.append(_generate_tree(subpath, prefix + extension))

        return "\n".join(tree)

    if not os.path.isdir(path):
        return f"{path} is not a valid directory."
    
    return _generate_tree(path)

# Example usage:
path = "."  # Replace with the path to the directory you want to list
print(generate_tree(path))
