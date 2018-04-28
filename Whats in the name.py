t = input();
for i in xrange(t):
    name = map(str,raw_input().split())
    if len(name) == 1:print(name[0][0].capitalize()+name[0][1:].lower())
    elif len(name) == 2:print(name[0][0].capitalize()+'. '+name[1][0].capitalize()+ name[1][1:].lower())
    else:print(name[0][0].capitalize()+'. '+name[1][0].capitalize()+'. '+name[2][0].capitalize()+ name[2][1:].lower())
    
