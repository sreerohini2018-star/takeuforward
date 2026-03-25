
"""
w.a.p for binary_search
"""

class BinarySearch:
    def solution(self,arr,element):
        arr.sort()
        low=0
        upp=len(arr)-1
        is_present=False

        while(low<=upp):
            mid=(low+upp)//2
            
            if element==arr[mid]:
                is_present=True
                break
            elif element<arr[mid]:
                upp=mid-1
            elif element>arr[mid]:
                low=mid+1
        print(is_present)

bsearch_instance=BinarySearch()
arr=[10,12,14,25,36]
element=35
bsearch_instance.solution(arr,element)        



