# a="aadasd"
# b="a"
# for i in a:
#     if i == b:
#         print("valid")
#     else:
#         print("not....")
#     break
# from collections import Counter
# list1=[1,2,3,3,1]
# print(*Counter(list1))
# unique_list=[]
# # for x in list1:
#         # check if exists in unique_list or not
#         if x not in unique_list:
#             unique_list.append(x)
#             if x in unique_list:
#                   print("its not")
#             else:
#                   print("its Uniq",x)
            
# print(unique_list)
    # if i == a:
    #     print("Error..")
    # else:
    #     print(f"its unic {i}")
    # break
def decimalToBinary(n):
    return bin(n).replace("0b", "")
   
# Driver code
if __name__ == '__main__':
    print(decimalToBinary(8))
    print(decimalToBinary(18))
    print(decimalToBinary(7))