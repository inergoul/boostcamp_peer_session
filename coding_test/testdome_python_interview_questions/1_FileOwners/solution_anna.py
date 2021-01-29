from collections import defaultdict

def group_by_owners(files):
    owners = defaultdict(list)
    for v, k in files.items():
        owners[k].append(v)
    return owners
