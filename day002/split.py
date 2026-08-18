
def split(data: str, sep=None, maxsplit=-1) -> list:
    """Split a string into a list using the specified separator."""
    if maxsplit == 0:
        return [data.strip()] if sep is None else [data]
    
    result = []
    length = len(data)
    i = 0
    splits_done = 0

    while i < length:
        if sep is None:
            while i < length and data[i].isspace():
                i += 1
            if i >= length:
                break
            start = i
            while i < length and not data[i].isspace():
                i += 1
        else:
            start = i
            idx = data.find(sep, i)
            if idx == -1 or (maxsplit != -1 and splits_done >= maxsplit):
                i = length
            else:
                i = idx

        word = data[start:i]
        result.append(word)
        splits_done += 1

        if sep is not None and i < length and data[i:i+len(sep)] == sep:
            i += len(sep)

        if maxsplit != -1 and splits_done >= maxsplit:
            if i < length:
                if sep is None:
                    while i < length and data[i].isspace():
                        i += 1
                result.append(data[i:])
            break
    
    if sep is not None and data.endswith(sep):
        result.append('')

    return result


if __name__ == '__main__':
     assert split('') == []
     assert split(',123,', sep=',') == ['', '123', '']
     assert split('test') == ['test']
     assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
     assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
     assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
     assert split('    set   3     4') == ['set', '3', '4']
     assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
     assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']
