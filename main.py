memory={}

# t=True

def check_command(command):
    def wrapper(string):
        try:
            return command(string)
        except IndexError:
            return "Type all param for command. For help, type 'command'"
        except KeyError:
            return f"No record {string}, check param. For help, type 'command'"
        except ValueError:
            return "Phone must contains only digit"
    return wrapper


def exit(string):
    # global t
    # t=False
    return "Good bye!"


def command(string):
    help_text = ['exit: exit',
       'add: add new contact need write name and number with\
           space command shoulde be look like this "add name number"',
       'change: change numbers already created contact command\
           shoulde be look like this "change name number"',
       'show_all: show all the contacts',
       'phone: this command shows the persons phone command\
           should be look like this "name number"']
    return '\n'.join(help_text)


@check_command
def add(string):
    data = string.split(' ')
    memory[data[0]] = int(data[1])
    return 'Number was success add!'

@check_command
def phone(string):
    name_person = string
    return memory[name_person]
    # for k in filter(lambda x:x==name_person, memory.keys()):
    #     return memory[k]

@check_command
def change(string):
    data =string.split(' ')
    memory[data[0]] = int(data[1])
    # for k in filter(lambda x:x==list_of_elements[0],memory.keys()):
    #     memory[k]=list_of_elements[1]
    return 'Number was success change!'


def show_all(string):
    list_of_numbers=[]
    for k, v in memory.items():
        list_of_numbers.append(f'{k}: {v}')
    return '\n'.join(list_of_numbers)


# def check_comand(string):
#     def checks(list):
#         comands_on_check={2:3,
#                3:3,
#                4:2}
#         if len(list)==comands_on_check[command_user]:
#             try:
#                 if any(char.isdigit() for char in list[1])==False and any(char.isdigit() for char in list[2])==True:
#                     return dict_of_command[command_user](string)
#             except IndexError:
#                 return phone(string)
#             else:
#                 return 'The name must not contain numbers, and the number must not contain characters other than numbers'
#         elif len(list)>3:
#             return 'Remove spaces in the phone'
#         else:
#             return 'Give me name and phone please'
#     dict_of_command={1:exit,
#             0:command,
#             2:add,
#             4:phone,
#             3:change,
#             5:show_all}    
#     posibl_coommand=["command","exit",'add','change','phone','show_all']
#     list_from_string=string.split(' ')
#     try:
#         command_user=posibl_coommand.index(list_from_string[0].lower())
#     except ValueError:
#         return('You write wrong command, for  to get a list of commands write command')
#     try:
#         return dict_of_command[command_user]()
#     except TypeError:
#         return checks(list_from_string)
    
COMMANDS = {command: 'command',
            exit: 'exit',
            add: 'add',
            change: 'change',
            phone: 'phone',
            show_all: 'show_all'}


def command_handler(text: str):
    for command, key_word in COMMANDS.items():
        if text.lower().startswith(key_word):
            return command, text.replace(key_word, '').strip()
    return None, 'You write wrong command, for  to get a list of commands write command'


def main():
    # global t
    while True:
        command_user = input('>>>')
        command, data = command_handler(command_user)
        if command:
            print(command(data))
        else:
            print(data)
        if command == exit:
            break
main()