def read_input(filename):
    f = open(filename, "r")
    lines = []
    while True:
        line = f.readline()
        if line == "":
            break
        lines.append(line.strip())
    f.close()
    return lines


def count_elements(s):
    count = 0
    for _ in s:
        count += 1
    return count


def build_groups(edges):
    groups = []
    for edge in edges:
        groups.append([edge[0], edge[1]])
    return groups

def in_group(group, value):
    for x in group:
        if x == value:
            return True
    return False


def count_pairs(groups):
    males = []
    females = []

    for group in groups:
        m = 0
        f = 0
        for x in group:
            if x % 2 == 0:
                f += 1
            else:
                m += 1
        males.append(m)
        females.append(f)

    total = 0
    i = 0
    while True:
        try:
            mi = males[i]
            fi = females[i]
        except IndexError:
            break

        j = 0
        while True:
            try:
                if i != j:
                    mj = males[j]
                    fj = females[j]
                    total += mi * fj + fi * mj
                j += 1
            except IndexError:
                break
        i += 1

    return total // 2


lines = read_input("input.txt")

edges = []
i = 0
while True:
    try:
        parts = lines[i].split()
        if count_elements(parts) == 2:
            a = int(parts[0])
            b = int(parts[1])
            edges.append((a, b))
    except IndexError:
        break
    i += 1

groups = build_groups(edges)

result = count_pairs(groups)

print(result)