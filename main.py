# def jazzify(lst):
#     lst1 = []
#     for x in lst:
#         lst1.append(f"{x}7")
#     return lst1
#
# print(jazzify(["G", "F", "C"])) #➞ ["G7", "F7", "C7"]
# print(jazzify(["Dm", "G", "E", "A"])) #➞ ["Dm7", "G7", "E7", "A7"]
# print(jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"])) #➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
# print(jazzify([])) #➞ []



#task2
# def find_odd(lst):
#     for x in lst:
#         if lst.count(x) % 2 != 0:
#             return x
# print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])) #➞ -1
# print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])) #➞ 5
# print(find_odd([10])) #➞ 10



#task3
# def filter_list(lst):
#     lst1 = []
#     for x in lst:
#         if type(x) != str:
#             lst1.append(x)
#     return lst1
#
# print(filter_list([1, 2, "a", "b"])) #➞ [1, 2]))
# print(filter_list([1, "a", "b", 0, 15])) #➞ [1, 0, 15])
# print(filter_list([1, 2, "aasf", "1", "123", 123])) #➞ [1, 2, 123])


#task4
# first, *middle, last = [1,2,3,4,5,6]
# print(first) #-> 1
# print(middle) #-> [2,3,4,5]
# print(last) #-> 6

#task5
# def count_characters(dict):
#     result = 0
#     for x in dict:
#         result += len(x)
#     return result
#
# print(count_characters([
#   "###",
#   "###",
#   "###"
# ])) #➞ 9
#
# print(count_characters([
#   "22222222",
#   "22222222",
# ])) #➞ 16
#
# print(count_characters([
#   "------------------"
# ])) #➞ 18
# print(count_characters([])) #➞ 0
# print(count_characters(["", ""])) #➞ 0)





