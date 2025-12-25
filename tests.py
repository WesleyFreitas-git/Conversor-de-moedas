nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
nums2 = [numero % 10 if numero > 9 else numero for numero in nums ]
nums3 = [numero % 10 for numero in nums]

print(nums)
print(nums2)
print(nums3)

