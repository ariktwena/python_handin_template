

def get_one_name_bad(list):
    current = 0
    while (current < len(list)):
        yield list[current]
        current += 1

def get_one_name_good(file):
    with open(file) as f:
        for line in f:
            yield line.strip()
