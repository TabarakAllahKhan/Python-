import os as os

direactory_path='C:/Users/Microsoft/Desktop/testing'

entries=os.listdir(direactory_path)
count=1
for i in entries:
    if i.endswith('.txt'):
       print(i)
       os.rename(f"C:/Users/Microsoft/Desktop/testing/{i}",f"C:/Users/Microsoft/Desktop/testing/{count}.txt")
       count+=1
       print(i)