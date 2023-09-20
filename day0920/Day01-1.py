num = 10
print("안녕 : ", num)

li = [100, "안녕", 1.123]
print(li)

li = (100, "안녕", 1.123)
print(li)

li = {"one" : 100000}
print(li["one"])

if 100 < 200 :
    print("100은 200보다 작다")

for i in range(1, 10, 2) :
    print(i, end=" ")

print()

li = [100, 200, 300]
for i in li :
    print(i, end=" ")

print()

def test(str) :
    print(str, " : test 호출")
    return "리턴값"

result = test("안녕")
print(result)
