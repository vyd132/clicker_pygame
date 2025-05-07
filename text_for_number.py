def text(ch,m):
    number = []
    cycle_number = 1000
    text_number = ''
    while True:
        if cycle_number//1000>ch:
            break
        number.append((ch%cycle_number-ch%(cycle_number//1000))//(cycle_number//1000))
        cycle_number*=1000
    if ch==0:
        return '0'
    for letter in range(len(number)):
        if letter==0:
            text_number = str(int(number[letter]))
            continue
        if number[letter]==0:
            continue
        if letter-1>=len(m):
            text_number = str(int(number[letter])) +' '+ text_number
            continue
        text_number = str(int(number[letter]))+m[letter-1]+' '+text_number
    return text_number

