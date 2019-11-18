#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:  # pragma: no cover
    basestring
except NameError:  # pragma: no cover
    basestring = str


def is_string_type(needle):
    if isinstance(needle, basestring):
        return True
    else:
        return False


def is_int_type(needle):
    if isinstance(needle, int):
        return True
    else:
        return False


def is_int_in_a_string(needle):
    try:
        int(needle)
        return True
    except ValueError:
        return False


def is_float_type(needle):
    if isinstance(needle, float):
        return True
    else:
        return False


def is_float_in_a_string(needle):
    try:
        float(needle)
        return True
    except ValueError:
        return False


def is_int_or_float_type(needle):
    if is_int_type(needle) is True or is_float_type(needle) is True:
        return True
    else:
        return False


def is_list_type(needle):
    if isinstance(needle, list):
        return True
    else:
        return False
