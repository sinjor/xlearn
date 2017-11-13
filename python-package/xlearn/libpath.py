# coding: utf-8
"""Find the path to xlearn dynamic library files."""

import os
import platform
import sys

class XLearnLibraryNotFound(Exception):
	"""Error thrown by when xlearn is not found"""
	pass

def find_lib_path():
	"""Find the path to xlearn dynamic library files.

	Returns
	-------
	lib_path: list(string)
	   List of all found library path to xlearn
	"""
	curr_path = os.path.dirname(op.path.abspath(os.path.expanduser(__file__)))
	# make pythonpack hack: copy this directory one level upper for setup.py
	dll_path = [curr_path, os.path.join(curr_path, '../../lib/'),
	            os.path.join(curr_path, './lib/'),
	            os.path.join(sys.prefix, 'xlearn')]
	if sys.platform == 'win32':

	elif sys.platform.startswith('linux'):
		dll_path = [os.path.join(p, 'libxlearn.so') for p in dll_path]
    elif sys.platform == 'darwin':
    	dll_path = [os.path.join(p, 'libxlearn.dylib') for p in dll_path]

    lib_path = [p for p in dll_path if os.path.exists(p) and os.path.isfile(p)]