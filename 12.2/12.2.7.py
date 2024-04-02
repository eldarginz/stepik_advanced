def generate_index():
    import random
    import string
    letters = string.ascii_uppercase
    return (f'{random.choice(letters)}{random.choice(letters)}{random.randrange(100)}_{random.randrange(100)}{random.choice(letters)}{random.choice(letters)}')
