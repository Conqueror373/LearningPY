global data, columns
FileN = input(str("Путь до файла .csv: ")) #"C:\File\data.csv"



def get_line():
    global s
    s = list(input("Укажите Айди, Имя пользователя, Логин, Пароль, Статус аккаунта и цену в долларах: ").split())
    return (s[0], s[1], s[2], s[3], s[4], int(s[5]))

def insert(line):
    if line not in data:
        data.append(line)
        write_to_file(FileN)


def write_to_file(FileN):
    with open(FileN, 'a') as file:
        if "Id,Nickname,Login,Password,Status,Price in $" in open(FileN).read():
            for line in data:
                line=[str(i) for i in line]
                file.write(','.join(line)+'\n')
        else:
            file.write(','.join(columns)+'\n')
            for line in data:
                line=[str(i) for i in line]
                file.write(','.join(line)+'\n')

def read_from_file(FileN):
    with open(FileN, 'r') as file:
        columns = tuple(file.readline().split(','))
        data = []
        for line in file:
            line = line.split(',')
            data.append((line[0], line[1], line[2], line[3], line[4], int(line[5])))
    for i in columns:
        print(str(i).ljust(size), end=" ")    
    for line in data:
        for i in line:
            print(str(i).ljust(size), end=' ')
        print()



size = 11
columns = ("Id", "Nickname", "Login", "Password", "Status", "Price in $")
data = []


#write_to_file(FileN)
insert(get_line())
print(read_from_file(FileN))
