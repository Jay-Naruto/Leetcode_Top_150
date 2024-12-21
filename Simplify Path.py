class Solution:
    def simplifyPath(self, path: str) -> str:
        stack =[]
        words = path.split("/")
        for word in words:
            if word == "..":
                if stack:
                    stack.pop()
            elif stack and word == "/" and stack[len(stack) - 1] =="/":
                stack.pop()
            else:
                if word and word != ".":
                    stack.append(word)
        
        return "/" + "/".join(stack)
