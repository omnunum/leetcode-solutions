# @algorithm @lc id=1371 lang=python3 
# @title minimum-remove-to-make-valid-parentheses


from en.Python3.mod.preImport import *
# @test("lee(t(c)o)de)")="lee(t(c)o)de"
# @test("a)b(c)d")="ab(c)d"
# @test("))((")=""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = []
        opens = []
        for i, c in enumerate(s):
            # always valid to add, since the only invalid case
            # for an open is decided when there end up not being
            # enough closes
            if c == "(":
                opens.append(i)
                chars.append(c)
            elif c == ")":
                # if we have opens to match our close, pop off the
                # stack of potentially invalid opens, and add our
                # close to the valid chars list
                if opens:
                    opens.pop()
                    chars.append(c)
                # if no open to match, add empty string to represent
                # this close as invalid
                else:
                    chars.append("")
            # letters are always valid
            else:
                chars.append(c)
        # now that we know how many opens were matched to closes
        # "remove" the remaining opens that didn't have closes
        for i in opens:
            chars[i] = ""
        # the empty strings in the list won't show up in the final result
        return "".join(chars)