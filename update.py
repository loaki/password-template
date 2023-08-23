import sys
import json

def append():
    with open('<password_hash>/data.json', 'r') as data:
        j_data = json.load(data)
    new = {
        "name": sys.argv[2], 
        "id": sys.argv[3],
        "pw": sys.argv[4]
    } 
    j_data['passwords'].append(new)
    with open('<password_hash>/data.json', 'w') as data:
        json.dump(j_data, data, indent=4)

def remove():
    with open('<password_hash>/data.json', 'r') as data:
        j_data = json.load(data)
    for pw in j_data['passwords']:
        if pw['name'] + pw['id'] == sys.argv[2]:
            j_data['passwords'].remove(pw)
    with open('<password_hash>/data.json', 'w') as data:
        json.dump(j_data, data, indent=4)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'append' and len(sys.argv) == 5:
            append()
        if sys.argv[1] == 'remove' and len(sys.argv) == 3:
            remove()
