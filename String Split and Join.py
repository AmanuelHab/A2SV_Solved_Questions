def split_and_join(line):
    r = line.split()
    return "-".join(r)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
