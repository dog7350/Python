import pandas as pd

# DataFrame : 2차원 배열
df = pd.read_csv("../0.ML/1.pandas/data/1.pandas.csv")
print(df)

print("==== 시리즈 ====")
# Series : 1차원 배열
# [] Series 형식으로 가져온다
print(df["name"])
print(df.age)

print("==== 데이터 프레임 ====")
# [[]] DataFrame 형식으로 가져온다
# 여러 개의 값을 가져오고자 하는 경우[[]]
print(df[["name", "age"]])

print("==== 인덱싱 ====")
# 인덱싱 : 인덱스의 범위를 지정한다.
print(df[ 1:3 ])
print(df[ :3 ])
print(df[ 1: ])

print("==== LOC ====")
# LOC : DF.loc[ index조건식, 컬럼 조건식 ]
print(df.loc[ 1:3, "name" ])
print(df.loc[ 1:3, ["name", "score"] ])
print(df.loc[ :, "name":"grade" ])
print(df.loc[ 1:3,  ])
print("=============")
print(df["grade"] == 'A')
print(df[ df["grade"] == "A" ])
