def os_pats(*args, sep='\\', **kwargs):
    path = sep.join(args)

    return path


p = os_pats('asdasdas', 'asdsad', 'sadasdasdwwqewe', 'eeeeeeeeeeee', sep='@', trim=True)
print(p)