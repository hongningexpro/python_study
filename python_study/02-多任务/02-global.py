num = 100
nums = [1,2,3]

def test1():
    global num
    num +=100

def test2():
    global nums
    #nums.append(4)
    nums +=[100,200]

print(num)
print(nums)

test1()
test2()


print(num)
print(nums)
