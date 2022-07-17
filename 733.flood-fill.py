#
# @lc app=leetcode id=733 lang='python3'
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        y_bounds = len(image) - 1
        x_bounds = len(image[0]) - 1
        def fill(image, y, x, newColor):
            old_color = image[y][x]
            image[y][x] = newColor
            for yd, xd in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                in_bounds = (
                    0 <= x+xd <= x_bounds
                    and 0 <= y+yd <= y_bounds
                )
                if in_bounds and old_color == image[y+yd][x+xd]:
                    fill(image, y+yd, x+xd, newColor)
        if image[sr][sc] != newColor:
            fill(image, sr, sc, newColor)
        return image
# @lc code=end