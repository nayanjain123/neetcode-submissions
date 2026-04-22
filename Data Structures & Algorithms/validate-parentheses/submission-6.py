class Solution:
    def isValid(self, s: str) -> bool:
        map={ "}":"{" , ")":"(" , "]":"[" }
        stack=[]
        for ch in s:
            if ch in map.keys():
                if not stack or stack.pop()!=map[ch]:
                    return False
            else:
                stack.append(ch)
        return len(stack)==0
            
