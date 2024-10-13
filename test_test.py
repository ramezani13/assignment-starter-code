from check_word import contains_word

def test_contains_word1():
    assert contains_word("The quick brown fox", "quick") == True

def test_contains_word2():
    assert contains_word("The quick brown fox", "slow") == False

def test_contains_word3():
    assert contains_word("Hello world", "world") == True

def test_contains_word4():
    assert contains_word("Hello world", "earth") == False

def test_contains_word5():
    assert contains_word("Python is fun", "Python") == True

