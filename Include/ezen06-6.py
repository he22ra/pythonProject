
dic_prd = {
    'L' : [5141, 5365, 5084],
    'M' : [4968, 4977, 4915],
    'S' : [5012, 4991, 5029],
    'XL' : [5071, 4976, 5023],
    'XS' : [5195, 4954, 5088]
}

import pandas as pd
agg_prd_pd = pd.DataFrame({
  'L' : [5141, 5365, 5084],
  'M' : [4968, 4977, 4915],
  'S' : [5012, 4991, 5029],
  'XL' : [5071, 4976, 5023],
  'XS' : [5195, 4954, 5088]
}, index = ['Jacket','Shirt','Trousers'])

print(agg_prd_pd)
print("=========================================")

import pandas as pd
df = pd.DataFrame({
      'SIZE' : ['XL','L','M','S','XS'],
      'product_type' : ['Jacket','Shirt','Jacket','Trousers','Shirt'],
      'color' : ['red', 'black','black', 'red', 'blue'],
      'quantity' : ['5', '15', '10', '20', '15'] 
})
print(df)
print()
#열삭제
print(df.drop(['color'], axis = 1))

print()
print(df.drop(['color', 'quantity'], axis = 1))

print()
print(df.drop(['SIZE', 'product_type'], axis = 1))

print()
#행 삭제
print(df.drop([0], axis = 0))

print()
#중복여부 >처음 값을 기준으로
print(df.duplicated(['product_type'], keep='first'))

print()
#중복여부 >마지막 값을 기준으로
print(df.duplicated(['product_type'], keep='last'))

print()
#중복값 삭제 keep>남길값
print(df.drop_duplicates(['product_type'], keep='first'))

print()
print(df)

print()
#중복값 삭제 keep>남길값
print(df.drop_duplicates(['product_type'], keep='last'))