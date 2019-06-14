#Finding the version of python in Unix Terminal
import sys
print(sys.version)
3.6.5 (default, Apr 1 2018, 05:46:30)

If you want to know all the functions that are present in the sys module, you can do as dir(sys). 
Now, when I ran the dir(sys) in my terminal, this is what I got - 

['__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', 
'__loader__', '__name__', '__package__', '__spec__', '__stderr__',
'__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', 
'_debugmallocstats', '_getframe', '_git', '_home', '_xoptions', 'abiflags',
'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 
'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 
'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 
'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_wrapper', 'getallocatedblocks',
'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 
'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof',
'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', '
is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 
'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'set_asyncgen_hooks',
'set_coroutine_wrapper', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval',
'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions']
