class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        stack=[]
        
        for brack in s:
            if not brack in close_to_open:
                stack.append(brack)
            else:
                if len(stack)<1:
                    return False
                if stack.pop() != close_to_open.get(brack):
                    return False
        
        
        if len(stack) > 0 :
            return False
        return True