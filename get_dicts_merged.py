import itertools

def get_dicts_merged(dict_1, dict_2):
    result = {}

    for k, v in itertools.chain(dict_1.iteritems(), dict_2.iteritems()):
        val = result.get(k, '')
        val += v if not val else ':' + v
        result[k] = val

    return result


dict1 = {'k1' : 'key1', 'k2' : 'key2', 'k4' : 'key4'}
dict2 = {'k1' : 'mey1', 'k3' : 'key3', 'k4' : 'mey4', 'k5' : 'key5'}

dictm = get_dicts_merged(dict1, dict2)

print dict1
print dict2
print dictm
