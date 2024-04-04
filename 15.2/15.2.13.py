def greet(name, *args):
    if not args:
        return (f'Hello, {name}!')
    else:
        return (f"Hello, {name} and {' and '.join(args)}!")
