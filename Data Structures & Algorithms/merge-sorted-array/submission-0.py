class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #In: nums1 = [1,2,2,3,5,6]; m=3; 
        #               k
        #.              i
        #       nums2=[2,5,6]; n=3;
        #            j
        #Out:nums1 = [1,2,2,3,5,6]
        # m+n=len(nums1)

        #nums1=[0,0,10,20,20,40]
        #.   i    k
        #nums2=[1,2]
        #.        j
        i=m-1
        k=m+n-1
        j=n-1
        while j>=0 and i>=0:
            if nums1[i]<=nums2[j]:
                nums1[k]=nums2[j]
                j-=1
            else:
                nums1[k]=nums1[i]
                nums1[i]=0
                i-=1
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            k-=1
            j-=1







            


        


