# @algorithm @lc id=1205 lang=python3
# @title defanging-an-ip-address
from en.Python3.mod.preImport import *
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')