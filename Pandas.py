import pandas as pd
data={
    'Student Id':[1,2,3],
    'Name': ['A','B','C'],
    'Marks 1':[45,81,39],
    'Marks 2':[67,72,61],
    'Marks 3':[75,35,57],
    'Marks 4':[50,55,44],
    'Marks 5':[98,70,80],
    'Marks 6':[44,45,39]
}
df=pd.DataFrame(data)


sum=df["Marks 1"]+df["Marks 2"]+df["Marks 3"]+df["Marks 4"]+df["Marks 5"]+df["Marks 6"]
per=sum/6
df["Percentage"]=per
print(df[['Student Id','Name']][df.Percentage==df.Percentage.max()])


print("Students who got lowest marks in more than 2 subjects")
list=[]
for i in range(1,len(df.axes[1])-3+1):
    marks_no='Marks '+str(i)
    low=df[marks_no].min()
    index=df[df[marks_no] == low].index.values
    index=index[0]
    list.append(df.loc[index]['Name'])
list
frequency = {}
for item in list:
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1

for keys, value in frequency.items():
   if frequency[keys]>2:
    print(keys)


df.to_csv("Marksheet.csv")