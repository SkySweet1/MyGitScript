import os
from core import loadIgnorelist, getAllFiles, getNextCommit, saveCommit, restoreCommit


def cmdInit():

#инициализация репозитория
#библиотеки: os

    if os.path.exists(".mygit"):
        print("already exists")

        return

    os.makedirs(".mygit/commits")
    
    print("repository inits")

#   инициализация
#   if os.path.exists(".mygit"):                провека на существование
#   
#   os.makedirs(".mygit/commits")               создаем папку .mygit и внутри папку commits

def cmdCommit(message):

#создание коммита
#библиотеки: os

    if not os.path.exists(".mygit"):
        print("no inited youre repository! 'init' it ")

        return
    
    if not message or not message.strip():
        print("commit can not be empty")

        return

    ignore = loadIgnorelist()

    #   определяем номер след коммита

    files = getAllFiles(ignore)

    #    список игнорируемых файлов

    if not files:
        print("not files for commit")

        return
    
    #   проверка на наличие файлов для сохранения

    commitID = getNextCommit()

    #   определяем номер след коммита

    saveCommit(commitID, message, files)

    #   сохранеxние

    print("commit created")

#   if not os.path.exists(".mygit"):                проверка на существование репозитория (иначе не идем)
#   
#   if not message or not message.strip():          проверка сообщения (коммита)
#   
#   ignore = loadIgnorelist()                       загружаем игнорируемые файлы
#   
#   files = getAllFiles(ignore)                     собираем файлы для коммита
#   
#   if not files:                                   проверка на наличие файлов
#     
#   commitID = getNextCommit()
#   saveCommit(commitID, message, files)
#   
#   создаем коммит

def cmdCheckout(commitID):

#переключение на коммит
#библиотеки: os

    if not os.path.exists(".mygit"):
        print("repository not found")

        return
    
    try:
        commitID = int(commitID)
    except ValueError:
        print("invalid commit ID")

        return
    
    filesDirectory = f".mygit/commits/{commitID}/files"

    if not os.path.exists(filesDirectory):
        print("fault -> commit was not created")

        return
    
    restoreCommit(commitID)

#   if not os.path.exists(".mygit"):              проверка на существование папки .mygit
#
#   commitID = int(commitID)                      преобразование строки в число (проверка на валидность)
#
#   except ValueError:                            если не число то выполнение идет сюда
#   
#UPD
#   
#   if not os.path.exists(filesDirectory):          проверка что коммит с таким ID реально существует
#   
#UPD   
#   restoreCommit(commitID)                       восстановление комита с данным ID
