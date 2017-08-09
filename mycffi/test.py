#Interfaces to the functions.
#Alternatively one can call mycffi._lib.myfunc() directly.
def mybasic():
    import mycffi
    mycffi._lib.mybasic()

def myprint(message):
    import mycffi
    mycffi._lib.myprint(message)
    return

def myadd(x, y):
    """Adds two numbers together.

    x: first number
    y: second number

    returns the sum
    """
    import mycffi
    return mycffi._lib.myadd(x, y)
    
