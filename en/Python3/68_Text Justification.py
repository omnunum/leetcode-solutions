# @algorithm @lc id=68 lang=python3 
# @title text-justification


from en.Python3.mod.preImport import *
# @test(["This","is","an","example","of","text","justification."],16)=["This    is    an","example  of text","justification.  "]
# @test(["What","must","be","acknowledgment","shall","be"],16)=["What   must   be","acknowledgment  ","shall be        "]
# @test(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20)=["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "]
# @test(["Listen","to","many,","speak","to","a","few."], 6)=["Listen","to    ","many, ","speak ","to   a","few.  "]
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        formatted_lines = []
        # This will hold the words on our current line, as well as the count
        # of all the letters in those words
        stack, stack_len = [], 0
        for word in words:
            # If we add the next word, the length of our stack would be
            # the length of the next word, plus the length of all the 
            # other words in the stack, plus a space for each word in the stack.
            # If that puts us over our limit, we need to format what we have 
            # in the stack then reset it
            if len(word) + stack_len + len(stack) > maxWidth:
                # The total amount of spaces we'll need to format this line
                # will be the difference between the max and the length of 
                # our words in the stack.
                # The way we divide those spaces, is to reach as many as we 
                # can spread evenly *between* the words (so divided by the word
                # count minus one) and then take the remainder and add one space 
                # for each word left to right until we run out
                split_spaces, leftover_spaces = divmod(
                    maxWidth - stack_len, 
                    max(1, len(stack) - 1)
                )
                # This is where most of the logic is.  Each word will get the evenly
                # split amount of spaces, unless its the last word in which it will
                # get no spaces.  Of the ones that aren't the last word, and if we have
                # a remainder of spaces that didn't split evenly, we add one of those to 
                # the word in question if we have any to give it
                formatted_lines.append(
                    "".join(
                        f"{w}{' '*split_spaces}{' ' if i < leftover_spaces else ''}" 
                        if (i < len(stack)-1 or len(stack) == 1) else w
                        for i, w in enumerate(stack)
                    )
                )
                # Reset the stack and its length
                stack, stack_len = [], 0
            # Go ahead and add the word we considered in our first if statement
            stack.append(word)
            stack_len += len(word)
        # For the last line, we want to left align it so we'll just take whatever
        # is left on the stack and give it a single space between each word.
        # Then we'll pad the right side with as many spaces as we need to reach
        # the maxWidth.
        last_line_formatted = " ".join(stack)
        last_line_formatted += " "*(maxWidth - len(last_line_formatted))
        formatted_lines.append(last_line_formatted)
        return formatted_lines

