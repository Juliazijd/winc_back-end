def get_none():
    return None


def flatten_dict(d):
    values = d.values()
    print(values)
    for item in values:
        print(values)
        if type(item) is dict:
            print(values)
            flatten_dict(item)
            return values
    # print(list(values))


flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})