
"""
w.a.p for linea_searching
"""

class LinearSearching:
    def solution(self,arr,element):
        
        i=0
        is_present = False
        while(i<len(arr)):
            if arr[i]==element:
                is_present = True
                break
            i+=1
        print(is_present)
        

linstance=LinearSearching()    
lst=[12,11,25,21,6]
element=21        
linstance.solution(lst,element)      