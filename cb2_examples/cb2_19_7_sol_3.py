import itertools
def chop(iterable, length=2):
    var_a = (iter(iterable),) #tuple
    print str(var_a)
    print var_a*length
    return itertools.izip(*var_a*length)
if __name__ == '__main__':
    seq = 'foobarbazer'
    for length in (3, 4):
        for overlap in (0,):
            print '%d %d: %s' % (length, overlap,
                    map(''.join, chop(seq, length)))