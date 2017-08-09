# cffi_example
This is a working example of how to use cffi when you have a bunch of already written `.h` and `.c` files that you want to bundle into some Python code without using ctypes.

This repo should be used as a template for anyone that wants to write faster code or wrap their C code, but doesn't want to deal with following the regular cffi examples or fiddling with ctypes.

The gist is the following:
1) Have a directory structure similar to this one, with a `src`, `include`, and `project` directory.
2) Use `setup.py` to compile everything and link the python package with the `.so` file created.
3) Use `__init__.py` to access your library when you do an import.

That's it. In this project you can get everything working immediately by changing `mycffi` to whatever project name you need.
