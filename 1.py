
def twoSum(nums, target):
    for i in range(len(nums)):
        # print("i",i)
        num1 = nums[i]
        index1 = i

        num2 = target - num1
        index2 = -1

        for j in range(i+1,len(nums)):
            # print("j",j)
            if num2 == nums[j]:
                index2 = j
                result = []
                result.append(index1)
                result.append(index2)

                print(result)

        
    

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9

    # nums = [3,2,4]
    # target = 6

    # nums = [3,3]
    # target = 6
    twoSum(nums,target)