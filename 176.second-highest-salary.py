#
# @lc app=leetcode id=176 lang=MySQL
#
# [9] Palindrome Number
#

# @lc code=start
select (
    select
        distinct salary
        from employee
        order by 1 desc
        limit 1 
        offset 1
) as SecondHighestSalary
;
# @lc code=end