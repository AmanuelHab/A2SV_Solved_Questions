def swap_case(s):
    r = ""
    for ch in s:
        if ch.islower():
            r += ch.upper()
        else:
            r += ch.lower()
    return r

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
