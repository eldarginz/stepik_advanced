def generate_ip():
    import random
    return (f'{random.randrange(256)}.{random.randrange(256)}.{random.randrange(256)}.{random.randrange(256)}')
