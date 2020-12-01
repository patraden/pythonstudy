from json import JSONDecoder
import sys

def parse_object_pairs(pairs):
    dct = dict()
    dct_tmp = dict()
    for key, value in pairs:
        if key in dct:
            if key in dct_tmp:
                dct_tmp[key].append(value)
            else:
                dct_tmp[key]=[value]
        else:
            dct[key] = value
    for key in dct_tmp.keys():
        dct[key] = [dct[key]] + dct_tmp[key]
    return dct

if __name__ == "__main__":
    f = open('{file_path}'.format(file_path=sys.argv[1]))
    f_data = f.read()
    decoder = JSONDecoder(object_pairs_hook=parse_object_pairs)
    obj = decoder.decode(f_data)
    print(obj)
