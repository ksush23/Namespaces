d = dict([('global', [''])])


def get(namespace, var):
    if namespace == 'global':
        if var not in d.get(namespace):
            print('None')
            return
    if var in d.get(namespace):
        print(namespace)
        return
    else:
        get(d.get(namespace)[0], var)


for i in range(int(input())):
    action, name1, name2 = input().split()
    if action == 'add':
        (d.get(name1)).append(name2)
    if action == 'create':
        new = dict([(name1, [name2])])
        d.update(new)
    if action == 'get':
        get(name1, name2)