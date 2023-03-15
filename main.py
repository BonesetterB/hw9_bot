memory={}
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
    list_of_elements=string.split(' ')
    memory[list_of_elements[1]]=list_of_elements[2]
    return 'Number was success add!'
def phone(string):
    name_person=string.strip()[6:]
    for k in filter(lambda x:x==name_person,memory.keys()):
        return memory[k]

def change(string):
    list_of_elements=string.split(' ') 
    for k in filter(lambda x:x==list_of_elements[1],memory.keys()):
        memory[k]=list_of_elements[2]
    return 'Number was success change!'
def show_all():
    list_of_numbers=[]
    for k, v in memory.items():
        list_of_numbers.append(f'{k}: {v}')
    return '\n'.join(list_of_numbers)
def check_comand(string):
    def checks(list):
        comands_on_check={2:3,
               3:3,
               4:2}
        if len(list)==comands_on_check[command_user]:
            try:
                if any(char.isdigit() for char in list[1])==False and any(char.isdigit() for char in list[2])==True:
                    return dict_of_command[command_user](string)
            except IndexError:
                return phone(string)
            else:
                return 'The name must not contain numbers, and the number must not contain characters other than numbers'
        elif len(list)>3:
            return 'Remove spaces in the phone'
        else:
            return 'Give me name and phone please'
    dict_of_command={1:exit,
            0:command,
            2:add,
            4:phone,
            3:change,
            5:show_all}    
    posibl_coommand=["command","exit",'add','change','phone','show_all']
    list_from_string=string.split(' ')
    try:
        command_user=posibl_coommand.index(list_from_string[0].lower())
    except ValueError:
        return('You write wrong command, for  to get a list of commands write command')
    try:
        return dict_of_command[command_user]()
    except TypeError:
        return checks(list_from_string)
def main():
    global t
    while t:
        command_user=input()
        print(check_comand(command_user))
main()