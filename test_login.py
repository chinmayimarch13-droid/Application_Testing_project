def login(username, password):
    return username == "admin" and password == "1234"

def test_valid_login():
    assert login("admin", "1234") == True

def test_invalid_login():
    assert login("admin", "wrong") == False

def test_empty_login():
    assert login("", "") == False
