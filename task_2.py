def unique(data):
    is_present = set()
    result = []
    for elem in data:
        if elem not in is_present:
            result.append(elem)
            is_present.add(elem)
    return data
