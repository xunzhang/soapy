import os
import glob
import types

def expand_dir_rec(dn):
    flst = []
    if not dn.endswith('/'):
        dn += '/'
    items = glob.glob(dn + '*')
    for it in items:
        if os.path.isfile(it):
            flst.append(it)
        else:
            flst += expand_dir_rec(it)
    return flst

def expand(fns):
    flst = []
    if isinstance(fns, list):
        for it in fns:
            if os.path.isfile(it):
                flst.append(it)
            else:
                flst += expand_dir_rec(it)
        return flst
    elif os.path.isfile(fns):
        return [fns]
    elif os.path.isdir(fns):
        return expand_dir_rec(fns)
    else:
        return glob.glob(fns)
