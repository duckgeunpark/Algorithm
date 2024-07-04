from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 두 배열의 길이
        m, n = len(nums1), len(nums2)
        
        # 항상 nums1이 더 짧은 배열이 되도록 보장
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        # 이진 탐색을 위한 변수 초기화
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            
            if i < m and nums1[i] < nums2[j - 1]:
                # i가 너무 작음, 오른쪽으로 이동
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i가 너무 큼, 왼쪽으로 이동
                imax = i - 1
            else:
                # i가 완벽함
                if i == 0: max_of_left = nums2[j - 1]
                elif j == 0: max_of_left = nums1[i - 1]
                else: max_of_left = max(nums1[i - 1], nums2[j - 1])
                
                if (m + n) % 2 == 1:
                    return max_of_left
                
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                
                return (max_of_left + min_of_right) / 2.0