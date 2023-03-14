memory=[]
t=True
def exit():
    global t
    t=False
    return "Good bye!"
def command():
    l=['exit: exit',
       'add: add new contact need write name and number with space command shoude be look like this "add name number"',
       'change: change numbers already created contact command shoude be look like this "change name number"',
       'show_all: show all the contats',
       'phone: this command shows the persons phone command shoude be look like this "change name number"']
    return '\n'.join(l)
def add(string):
    l=string.split(' ')
    memory.append({l[1]:l[2]})
    return 'Number was success add!'
def phone(string):
    l=string.strip()[6:]
    for i in memory:
        for k in filter(lambda x:x==l,i.keys()):
            return i[k]

def change(string):
    l=string.split(' ') 
    for i in memory:
        for k in filter(lambda x:x==l[1],i.keys()):
            i[k]==l[2]
def show_all():
    l=[]
    for i in memory:
        for k, v in i.items():
            l.append(f'{k}: {v}')
    return '\n'.join(l)
def check_comand(string):
    def checks(name_command,list):
        coman={'add':3,
               'change':3,
               'phone':2}
        if len(list)==coman[name_command]:
            if any(char.isdigit() for char in list[1])==False:
                if len(list)==2:
                    return phone(string)
                else:
                    if any(char.isdigit() for char in list[2])==False:
                        return 'Give me  phone please without letter'
                    else:
                        return dict_1[x](string)
            else:
                return 'Enter name person not a number'
        else:
            return 'Give me name and phone please'
    dict_1={1:exit,
            0:command,
            2:add,
            4:phone,
            3:change,
            5:show_all}    
    coommand=["command","exit",'add','change','phone','show_all']
    j=string.split(' ')
    try:
        x=coommand.index(j[0].lower())
    except ValueError:
        return('You write wrong command, for  to get a list of commands write command')
    try:
        return dict_1[x]()
    except TypeError:
        return checks(j[0].lower(),j)
def main():
    global t
    while t:
        x=input()
        print(check_comand(x))
main()