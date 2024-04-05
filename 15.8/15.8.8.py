def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql',
              'select', 'update', 'exec', 'del', 'truncate']

    for word in ignore:
        if word in command:
            return True
    return False


def ignore_command_new(command):
    ignore = ['alias', 'configuration', 'ip', 'sql',
              'select', 'update', 'exec', 'del', 'truncate']
    listq = list(map(lambda x: True if x in command else False, ignore))
    return any(listq)


print(ignore_command_new('get ip'))
print(ignore_command_new('select all'))
print(ignore_command_new('delete'))
print(ignore_command_new('trancate'))
