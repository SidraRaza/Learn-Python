from my_code import MyTestClass  # Assuming your class is in my_code.py

def test_add():
    add = MyTestClass(3, 4)
    assert add.add() == 7
