def split_and_join(line):
    line=line.split(' ')
    applesauce='-'.join(line)
    return applesauce

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
