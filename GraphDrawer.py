import turtle

print('Enter numbers')
print('After entering type STOP')
nums = list()
while True:
    a = input()
    if a == 'STOP':
        break
    elif a.isdigit():
        nums.append(int(a))
turtle.setup(1000, 1000)
turtle.width(5)
turtle.penup()
step = 1000 / len(nums)
sc = 0
vertical_step = 1000 / (max(nums) - min(nums))
turtle.goto(-500, -500)
turtle.pendown()
sc = sc + 1
for i in range(1, len(nums)):
    n = nums[i]
    turtle.goto(round(step * sc) - 500, round(nums[i] * vertical_step) - 500 - round(min(nums) * vertical_step))
    sc = sc + 1
turtle.done()
