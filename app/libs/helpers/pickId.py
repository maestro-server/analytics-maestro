
def pick_id(dlist, dft=[]):
    if isinstance(dlist, list):
        mr = map(lambda x: x.get('_id'), dlist)
        return list(mr)

    return dft