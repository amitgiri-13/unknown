class solution:
    def findMedianSortedArrays(self,nums1,nums2):
        #merging two sorted arrays
        for i in nums2:
            nums1.append(i)

        #sorting the merged array
        nums3=sorted(nums1)

        #calculating size of array
        n=len(nums3)

        #calculating position of median
        position=(n+1)/2

        #evaluationg median
        if position.is_integer():
            position=int(position)
            median=nums3[position-1]
        else:
            position=int(position)
            median=(nums3[position-1]+nums3[position])/2
        return median


