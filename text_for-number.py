ch=10000000000000000000
m=['K','M','B']

number=[]
cycle_number=1000
cycle_text=0
cycle_letter=0
text=''

while True:
    if cycle_number//1000>=ch:
        break
    number.append((ch%cycle_number-ch%(cycle_number//1000))//(cycle_number//1000))
    # print(ch%(10*cycle_number))
    cycle_number*=1000

if ch==0:
    print(0)

for letter in range(len(number)):
    if letter==0:
        text = str(number[letter])
        continue
    if number[letter]==0:
        continue
    if letter-1>=len(m):
        text = str(number[letter]) +' '+ text
        continue
    text = str(number[letter])+m[letter-1]+' '+text

print(text)