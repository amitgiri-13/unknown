from median import solution
nums1=[1,3]
nums2=[2,4]
nums3=[2,5,4]
m=solution()

def test_median1():
    assert m.findMedianSortedArrays(nums1,nums2)== 2.5

def test_median2():
    assert m.findMedianSortedArrays(nums1,nums3)==3
