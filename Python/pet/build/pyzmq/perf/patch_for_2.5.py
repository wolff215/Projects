"""patch the perf tests for Python 2.5.

This just replaces the handful of b'msg' instances with 'msg'.
"""

for prefix in ('local', 'remote'):
    for test in ('lat', 'thr'):
        fname = '%s_%s.py'%(prefix, test)
        print "patching %s for Python2.5"%fname
        with open(fname) as f:
            text = f.read()
        fixed = text.replace("b'", "'").replace('b"', '"')
        if fixed == text:
            print "no change"
        else:
            with open('%s_%s.py'%(prefix, test), 'w') as f:
                f.write(fixed)