from storage import Storage

def test_add():
    pass

def test_remove():
    pass

def test_set():
    st = Storage({'a':1, 'b':2})
    key= 'b'
    value=5 
    val = st.set(key,value)
    print(st.get(key))
    assert val==5, "Value for the key {} should be  setted, but wasn't".format(key)
    key = 'c' 
    val = st.set(key,value)
    assert val is None,  "Value was setted, but wasn't".format(key)

def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def run_tests():
    test_get()
    test_add()
    test_remove()
    test_set()
    

if __name__ == "__main__":
    run_tests()
