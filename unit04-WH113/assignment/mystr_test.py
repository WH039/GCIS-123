# Assignment 4.1
# mystr_test.py by Weicheng Huang
import mystr

# trim
def test_slice1():
    # setup
    word = "cabaab"
    start = 2
    end = 5
    expected = "baa"
    #invoke
    actual = mystr.slice(word, start, end)
    #analyze
    assert actual == expected

def test_slice2():
    # setup
    word = "help"
    start = 0
    end = 2
    expected = "he"
    #invoke
    actual = mystr.slice(word, start, end)
    #analyze
    assert actual == expected

def test_slice3():
    # setup
    word = "withthistreasure"
    start = 4
    end = 8
    expected = "this"
    #invoke
    actual = mystr.slice(word, start, end)
    #analyze
    assert actual == expected

def test_slice4():
    # setup
    word = "ihopethisworks"
    expected = "ihopethisworks"
    #invoke
    actual = mystr.slice(word)
    #analyze
    assert actual == expected

def test_slice5():
    # setup
    word = "whatisacatfishwarrior"
    start = 4
    expected = "isacatfishwarrior"
    #invoke
    actual = mystr.slice(word, start)
    #analyze
    assert actual == expected

def test_slice6():
    # setup
    word = "icommanduponthee"
    expected = "icommand"
    #invoke
    actual = mystr.slice(word, end = 8)
    #analyze
    assert actual == expected

# contains
def test_contains1():
    # setup
    string1 = "cabaab"
    string2 = "ab"
    expected = 1
    #invoke
    actual = mystr.contains(string1, string2)
    #analyze
    assert actual == expected

def test_contains2():
    # setup
    string1 = "lobster"
    string2 = "er"
    expected = 5
    #invoke
    actual = mystr.contains(string1, string2)
    #analyze
    assert actual == expected

def test_contains3():
    # setup
    string1 = "leftorright"
    string2 = "or"
    expected = 4
    #invoke
    actual = mystr.contains(string1, string2)
    #analyze
    assert actual == expected

# replace
def test_replace1():
    # setup
    str1 = "cabaab"
    str2 = "ab"
    str3 = "X"
    expected = "cXaab"
    #invoke
    actual = mystr.replace(str1, str2, str3)
    #analyze
    assert actual == expected

def test_replace2():
    # setup
    str1 = "bone"
    str2 = "on"
    str3 = "e"
    expected = "bee"
    #invoke
    actual = mystr.replace(str1, str2, str3)
    #analyze
    assert actual == expected

def test_replace3():
    # setup
    str1 = "i dont know"
    str2 = "dont"
    str3 = "do"
    expected = "i do know"
    #invoke
    actual = mystr.replace(str1, str2, str3)
    #analyze
    assert actual == expected

# replace_all
def test_replace_all1():
    # setup
    str1 = "ineedanewchair"
    str2 = "i"
    str3 = "h"
    expected = "hneedanewchahr"
    # invoke
    actual = mystr.replace_all(str1, str2, str3)
    # analyze
    assert actual == expected

def test_replace_all2():
    # setup
    str1 = "reddotbluedotgreen"
    str2 = "dot"
    str3 = "--"
    expected = "red--blue--green"
    # invoke
    actual = mystr.replace_all(str1, str2, str3)
    # analyze
    assert actual == expected

def test_replace_all3():
    # setup
    str1 = "for I can no longer serve, I shall perish"
    str2 = "I"
    str3 = "you"
    expected = "for you can no longer serve, you shall perish"
    # invoke
    actual = mystr.replace_all(str1, str2, str3)
    # analyze
    assert actual == expected

# trim
def test_trim1():
    # setup
    string = "\t\n aa a \ta\n"
    expected = "aa a \ta"
    #invoke
    actual = mystr.trim(string)
    #analyze
    assert actual == expected

def test_trim2():
    # setup
    string = "\n wait    \t"
    expected = "wait"
    #invoke
    actual = mystr.trim(string)
    #analyze
    assert actual == expected

def test_trim3():
    # setup
    string = "\t\n why does it look like that\n"
    expected = "why does it look like that"
    #invoke
    actual = mystr.trim(string)
    #analyze
    assert actual == expected