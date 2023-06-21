"""public module."""


def list_intro():
    """List intro."""
    names = list()
    print(len(names))
    names.append("William")
    print(len(names) == 0)
    names.append("John")
    names.append("Amanda")
    print(len(names))
    print(names[2])
    for i in names:
        print(i)
    for i, name in enumerate(names):
        print(f"{i + 1}. {name}")
    names.pop(1)
    for i in range(len(names)):
        print(names[len(names) - i - 1])
    names.clear()
    print(len(names))


list_intro()
