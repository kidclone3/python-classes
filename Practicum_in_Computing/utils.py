import time
def time_it(method):
    """ Helper function to timing for debug. Not affect in production.
    """
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print(f'[TimeIt] {method.__code__.co_filename} {method.__name__}: {(te - ts) * 1000:.3f} ms')
        return result
    return timed

