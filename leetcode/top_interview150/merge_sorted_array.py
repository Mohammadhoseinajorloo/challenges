from typing import List

def merge(nums1: List, nums2: List, m: int, n: int) -> List:
    if n == 0: return
    len1 = len(nums1)
    end_idx = len1-1
    while n > 0 and m > 0:
        if nums2[n-1] >= nums1[m-1]:
            nums1[end_idx] = nums2[n-1]
            n-=1
        else:
            nums1[end_idx] = nums1[m-1]
            m-=1
        end_idx-=1
    while n > 0:
        nums1[end_idx] = nums2[n-1]
        n-=1
        end_idx-=1
    print(nums1)



if __name__ == "__main__":
    merge([1,2,3,0,0,0], [2,5,6], 3, 3)
    merge([1], [], 1, 0)
    merge([0], [1], 0, 1)
    

