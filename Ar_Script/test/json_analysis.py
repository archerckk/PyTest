import json

def end(level):
    return '  '*level+'-'

def start(level):
    return '  '*level+'+'

def find_dict(target,level):
    keys=iter(target)
    for i in keys:
        if type(target[i])is not dict:
            if type(target[i])is list:
                find_dict(target[i])
            else:
                print(end(level) + i + ':' + str(target[i]))

        else:
            next_level=level+1
            print(start(level)+i)
            find_dict(target[i],next_level)


def main():
    target=input()
    target=json.loads(target)
    find_dict(target,1)


if __name__ == '__main__':
    main()