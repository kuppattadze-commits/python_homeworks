# ამოცანის
# პირობა
# მოცემულია
# სტრინგი, რომელიც
# შეიცავს
# ფრჩხილებს:
# (და)
# [და]
# {და}
# შეამოწმე, არის
# თუ
# არა
# ფრჩხილები
# სწორად
# დაბალანსებული
# და
# დალაგებული.
# მაგალითები
# "()"
# # True
#
# "()[]{}"
# # True
#
# "(]"
# # False
#
# "([)]"
# # False
#
# "{[]}"
# # True
#
# შექმნას
# კლასი:
#
#
# class Solution:
#     def isValid(self, s: str) -> bool:
#         pass
#
#
# შეზღუდვები:
#
# გამოიყენოს
# list
# როგორც
# Stack.
#
# გამოიყენოს
# dict
# შესაბამისი
# ფრჩხილების
# შესამოწმებლად.
#
# არ
# გამოიყენოს
# მზა
# ბიბლიოთეკა
# ფრჩხილების
# ვალიდაციისთვის.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if not stack:
                    return False
                if pairs[stack.pop()] != char:
                    return False

        return not stack