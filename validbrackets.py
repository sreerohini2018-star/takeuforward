
"""
validbrackets
input_str="()","{()}","{}()" =>valid
input_str=")(","{][}","{}><" =>invalid
"""

class ValidBrackets:
    def solution(self,input_str):
        symbol_dictionary={
            "(":")",
            "{":"}",
            "[":"]",
            "<":">"
        }
        symbol_stack=[]
        for i in input_str:
            if i in symbol_dictionary:
                symbol_stack.append(i)
            i+=1    
