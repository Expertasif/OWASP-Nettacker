#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from glob import glob


def load_all_graphs():
    graph_names = []
    for lib in glob('lib/graph/*/engine.py'):
        lib = lib.rsplit('\\' if sys.platform == 'win32' or sys.platform == 'win64' else '/')[-2]
        if lib + '_graph' not in graph_names:
            graph_names.append(lib + '_graph')
    return graph_names


def load_all_modules():
    # Search for Modules
    module_names = []
    for lib in glob('lib/brute/*/engine.py'):
        lib = lib.rsplit('\\' if sys.platform == 'win32' or sys.platform == 'win64' else '/')[-2]
        if lib + '_brute' not in module_names:
            module_names.append(lib + '_brute')
    for lib in glob('lib/scan/*/engine.py'):
        lib = lib.rsplit('\\' if sys.platform == 'win32' or sys.platform == 'win64' else '/')[-2]
        if lib + '_scan' not in module_names:
            module_names.append(lib + '_scan')
    module_names.append('all')
    return module_names
