import sys
from commands import cmdInit, cmdCommit, cmdCheckout


def main():

#основная функция
#библиотеки: sys

    if len(sys.argv) < 2:
        print("use:")
        print("python mygit.py init")
        print("python mygit.py commit \"message\"")
        print("python mygit.py checkout <id>")
        
        return
    
    command = sys.argv[1]

    if command == "init":
        cmdInit()

            #   инициализация

    elif command == "commit":
        if len(sys.argv) < 3:
            print("identity commit's message")

            #   нужно создать новую папку для коммита
            #   сохранить туда файлы

            return
        
        cmdCommit(sys.argv[2])

    elif command == "checkout":
        if len(sys.argv) < 3:
            print("identity commit's ID")

            #   переключение на коммит

            return 
        
        cmdCheckout(sys.argv[2])

    else:
        print("unknown command")

#   if len(sys.argv) < 2:                           проверка аргументов командной строки
#   
#   command = sys.argv[1]                           сохраняем первый аргумент
#   
#   проверяем на соответствие слов -> init commit checkout 
#   
#   if len(sys.argv) < 3:                           проверка на четвертое сообщение
#   
#   анологично в checkout но только мы проверяем на наличие ID
#   
#   ну и если видим везде соответсвие, то вызываем функции:
#   cmdCommit("инициализация репозитория") 
#   cmdCheckout("переключение на коммит")

if __name__ == "__main__":
    main()