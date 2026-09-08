class Solution:
    def isValid(self, s: str) -> bool:
        temp=[]
        pairs={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for char in s:
            if char in pairs:
                if not temp or temp[-1]!=pairs[char]:
                    return False
                temp.pop()
            else:
                temp.append(char)
        return not temp
