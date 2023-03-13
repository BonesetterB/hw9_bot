memory=[]
#Можете залишити у коментаріях підсказку як опрацювати помилку, бо я не зовсім розумію як це зробити(
def add_num(string):
    l=string.split(' ')
    memory.append({l[1]:l[2]})
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
def main():
    while True:
        x=input()
        if x.lower()=="good bye" or x.lower()=="close" or x.lower()=="exit":
            print("Good bye!")
            break
        elif x.strip()[0:3].lower()=='add':
            add_num(x)
        elif x.strip()[0:6].lower()=='change':
            print(change(x))
        elif x.strip()[0:5].lower()=='phone':
            print(phone(x))
        elif x.lower()=='show all':
            print(show_all())
main()