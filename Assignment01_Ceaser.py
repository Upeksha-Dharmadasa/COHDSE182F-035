inp=input('Enter the text')
inp=inp.lower()
key=int(input('Enter the key'))
def cc(input,key)
if key>25:
   key=25
elif key<2
   key=2:
   finaltext=''
for letter in input:
if letter.isalpha():
   num=ord(letter)
if(num+key>122):
   x=(num+key)-122
   finaltext+=chr(x+ord('a')-1)
elif(num+key<=122):
   finaltext.+=chr(num+key)
else:
   finaltext+=letter
   print(finaltext)
cc(inp,key)
   
