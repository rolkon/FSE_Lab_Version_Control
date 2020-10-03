from storage import Storage

def test_add():
    pass

def test_remove():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    st.remove(key)
    val = st.get(key)
    assert val is None, "Value for the key {} should have been removed, but wasnt".format(key)
    key = 'a'
    val = st.get(key)
    assert val is not None, "Value for the key {} is None, although it hasn't been removed".format(key) 
    
def test_set():
    pass

def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def run_tests():
    test_add()
    test_remove()
    test_set()
    test_get()

if __name__ == "__main__":
    run_tests()