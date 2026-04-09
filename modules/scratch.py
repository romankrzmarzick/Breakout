import pygame  
# tilemap = [[0 for _ in range(4)] for _ in range(10)]


# for row_index, row in enumerate(tilemap):
#             for col_index, _ in enumerate(row):
#                 # Only puts rects in the first 4 rows. Note: 0 - 3.
#                 if row_index < 4:
#                     tilemap[row_index][col_index] = 1 
                    
# # print(tilemap)
# def test_floor_and_mod():
#     for i in range(30):
#         floor_division = i // 3
#         print(f"floor {i}:    {floor_division}")
#         modulus = i % 3
#         print(f"modul {i}:    {modulus}")   

# # test_floor_and_mod()

# def test_extend():
#     test_list = [pygame.Rect(0,0,0,0)]
#     second_list = [pygame.Rect(0,0,0,0), "5", "4", "3"]

#     print(test_list)
#     test_list.extend(second_list)
#     print(test_list)
#     return test_list

# list_stuff = test_extend()
# print(list_stuff[0])
test_list = [1, 2, 3, 5, 6]

print(test_list[7%4])
