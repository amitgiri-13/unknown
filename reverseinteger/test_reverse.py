from reverse import solution

s=solution()

def test1():
    assert s.reverse(-123)==-321
def test2():
    assert s.reverse(120)==21

def test3():
    assert s.reverse(123)==321

def test4():
    assert s.reverse(1534236469)==0

def test5():
    assert s.reverse(-2147483412)==-2143847412

