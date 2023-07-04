import pytest
from sum import solution
s=solution()
nums1=[2,7,11,14]
nums2=[3,2,4]
nums3=[3,3]
nums4=[3,2,3]

def test_calc1():
    assert s.calc(nums1,9)==(0,1)

def test_calc2():
    assert s.calc(nums2,6)==(1,2)

def test_calc3():
    assert s.calc(nums3,6)==(0,1)

def test_calc4():
    assert s.calc(nums4,6)==(0,2)