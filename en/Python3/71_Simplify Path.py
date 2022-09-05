# @algorithm @lc id=71 lang=python3 
# @title simplify-path


from en.Python3.mod.preImport import *
# @test("/home/")="/home"
# @test("/../")="/"
# @test("/home//foo/")="/home/foo"
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split('/'):
            if part in ('', '.'):
                continue
            elif part == '..':
                if stack: 
                    stack.pop()
            else:
                stack.append(part)
        return '/' + "/".join(stack)