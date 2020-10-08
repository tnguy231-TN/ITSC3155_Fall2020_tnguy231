import pythonBasics2 as pythonBasics2
# main() is already set up to call the functions
# we want to test with a few different inputs,
# printing 'OK' when each function call is correct.
# the simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.


# Calls the functions in pythonBasics2 with various inputs.
def main():
    # set which functions to test
    char_exists = True
    char_remove = True

    if char_exists:
        print()
        print('char_exists')
        test(pythonBasics2.char_exists("hello",'l'),2)
        test(pythonBasics2.char_exists("hi",'l'),0)
        test(pythonBasics2.char_exists("",'a'),0)
        test(pythonBasics2.char_exists("  ",' '),2)
        test(pythonBasics2.char_exists("abracadabra",'a'),5)
        test(pythonBasics2.char_exists("pumpkin spice pie",'p'),4)

    if char_remove:
        print()
        print('char_remove')
        test(pythonBasics2.char_remove("hello",'l'),"he__o")
        test(pythonBasics2.char_remove("hi",'l'),"hi")
        test(pythonBasics2.char_remove("",'a'),"")
        test(pythonBasics2.char_remove("abracadabra",'a'),"_br_c_d_br_")
        test(pythonBasics2.char_remove("pumpkin spice pie",'p'),"_um_kin s_ice _ie")


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

# when we run this file we want only the code inside main() to be executed
if __name__ == '__main__':
    main()
