# 레퍼런스 코드
def anagram(words):
    anagrams = {}

    for word in words:
        key = ''.join(sorted(word))
        anagrams.setdefault(key, [])
        anagrams[key].append(word)
    list(anagrams.values())

# #  뻘짓
#
# def group_anagrams(words):
#     word_list = []
#     stk = []
#     word = ''
#
#     # str 인풋을 리스트로 바꿔주기
#     for i in range(len(words)):
#         if stk:
#             if words[i] == "'":
#                 stk.pop()
#                 word_list.append(word)
#                 word = ''
#                 continue
#             else:
#                 word += words[i]
#
#
#         if words[i] == "'":
#             stk.append("'")
#
#     anagrams = []
#
#
#     while word_list:
#         char_set = set(word_list[-1])  # 비교할 단어
#         tmp_anagram_group = [word_list[-1]]  # 임시 애너그램 그룹
#         word_list.pop()  # 비교할 단어를 워드 리스트에서 삭제
#
#         for word in word_list:
#             if set(word) == char_set:  # 비교할 단어와 애너그램이면
#                 tmp_anagram_group.append(word)  # 임시 그룹에 추가
#         for i in range(1, len(tmp_anagram_group)):
#             word_list.remove(tmp_anagram_group[i])  #  임시 그룹에 들어간 단어들 워드 리스트에서 삭제
#         anagrams.append(tmp_anagram_group)  # 애너그램에 임시 애너그램 그룹 추가
#
#     return anagrams
#
# user_input = input()
# print(group_anagrams(user_input))

