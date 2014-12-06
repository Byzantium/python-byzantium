# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4 :


def mknum(value, _type, base=10):
    try:
        value = _type(value, base)
    except:
        pass
    return value
