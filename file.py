# #f=open('sample.txt','w')
# #string ="""hi
#           hello
#           hpw are you"""
# #f.write(string)
# #f.close()
# #print("content added successfully")


#w+ mode
f=open('sample.txt','r+')
#string ="""java programming"""
#f.write(string)
f.write('sql quary language')
content =f.read()
print(content)
f.close()
print("content added successfully")
