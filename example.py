#An example of how to use the python module.
import mycffi
mycffi.test.mybasic()
mycffi.test.myprint("Hah! It worked. Now, what's 3.141+2.718?")
print(mycffi.test.myadd(3.141, 2.718))
