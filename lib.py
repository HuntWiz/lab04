def per(a, b):
    c = []
    for item in a:
        if item not in c:
            a_item = a.count(item)
            b_item = b.count(item)
            min_count = min(a_item, b_item)
            # c += [item] * min_count
            for i in range(min_count):
                c.append(item)
    return c

a = [5, 2, 4, 'r', 4, 'ee', 1, 1,  4]
b = [4, 1, 'we', 'ee', 'r', 4, 1, 1]

c = per(a, b);

print(c)