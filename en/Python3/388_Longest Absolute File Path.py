# @algorithm @lc id=388 lang=python3 
# @title longest-absolute-file-path


from en.Python3.mod.preImport import *
# @test("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")=20
# @test("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")=32
# @test("a")=0
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        