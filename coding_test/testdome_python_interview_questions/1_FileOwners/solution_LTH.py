from collections import defaultdict
def group_by_owners(files):
    dict = defaultdict(list)
    for key, value in files.items():
        dict[value].append(key)
    return dict

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))