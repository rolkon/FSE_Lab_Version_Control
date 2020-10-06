from storage import Storage

def test_add():
    st = Storage({'a':1, 'b':2})
    key = 'c'
    val = 3
    st.add(key, val)
    assert st.data[key] == val, "Wrong value added for key {}".format(key)

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
    st = Storage({'a':1, 'b':2})
    key= 'b'
    value=5 
    val = st.set(key,value)
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
