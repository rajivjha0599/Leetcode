class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    for index in range(j + 1, len(nums2)):
                        if nums2[index] > nums2[j]:
                            res.append(nums2[index])
                            found = True
                            break
                    if not found:
                        res.append(-1)
                    break
        return res
                