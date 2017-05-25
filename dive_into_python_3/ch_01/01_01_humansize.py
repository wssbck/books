SUFFIXES = {1000: ['KB',  'MB',  'GB',  'TB',  'PB',  'EB',  'ZB',  'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# define a function with arguments, one with default value
def approximate_size(size, a_kb_is_1024_b=True):
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kb_is_1024_b else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

if __name__ == '__main__':
    
    # one named parameter - works
    print(approximate_size(size=1024))
    
    # one unnamed parameter - works
    print(approximate_size(1024))
    
    # two named arguments, order as declared - works
    print(approximate_size(size=1024, a_kb_is_1024_b=False))

    # two named arguments, order reversed - works
    print(approximate_size(a_kb_is_1024_b=False, size=1024))

    # two unnamed arguments - works
    print(approximate_size(1024, True))

    # first argument named, second unnamed - will not work
    # in Python unnamed arguments after named ones are forbiden
    # print(approximate_size(size=1024, True))

    # passing a negative number for size raises an error
    # print(approximate_size(-1))
