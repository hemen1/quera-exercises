def compare(string1, string2):
    string1 = list(string1)
    string2 = list(string2)
    while True:
        a, b = string1[0], string2[0]
        if a <= b:
            string1.pop(0)
        if a >= b:
            string2.pop(0)
        if len(string1) == 0 and len(string2) == 0:
            return 'Both strings are empty!'
        if len(string1) == 0:
            return "".join(string2)
        elif len(string2) == 0:
            return "".join(string1)
        string1.reverse()
        string2.reverse()


