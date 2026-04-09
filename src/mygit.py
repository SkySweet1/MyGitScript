import os
import sys
from pathlib import Path

def loadIgnorelist():

#   чтение .mygitignore 
#   используеться библиотека: import os

    ignore = {".mygit"}

    if os.path.exists(".mygitignore"):
        with open(".mygitignore", "r") as File:
            for line in File:
                line = line.strip()
                
                if line and not line.startswith("#"):
                    ignore.add(line)
    return ignore

#   ignore = {".mygit"}                     создаем множество с одной строкой ".mygit" чтобы потом проверять в if name in ignore
#   os.path.exists                          проверка существование файла
#   open(".mygitignore", "r")               октрываем для чтения с помощью with
#     
#   проходимся по всем строкам файла -> удаляя все пробельные символы в начале и в конце строки (такие как \n \r) с помощью .strip()
#
#   if line and not line.startswith("#"):   проверяем не пустая ли строка и не начинаеться ли строка с символа # (коментарий)
#
#   ignore.add(line)                        если выполняется условие то добавляеться строка в множество ignore
#
#   строка добавляеться не просто так -> без ignore.add(line) игнорировался только файл .mygit, а все остальные правила из .mygitignore не работали. 
#   мы добавляем строку для того чтобы прочитаные правила запоминались для дальнейшего использования
#  
#   return ignore                           возвращаем список имен которые нужно игнорировать

def needIgnored(path, ignore_set):

#нужно ли игнорировать конкретный файл (по пути)
#   используеться библиотека: from pathlib import Path

    parts = Path(path).parts

    for pth in parts:
        if pth in ignore_set:
            return True
    return False

#   parts = Path(path).parts                    создаем обьект пути из строки path (чтото типа "src/1.txt")
#   for pth in parts: if pth in ignore_set:     циклом проверяем не принадлежит ли к ignore_set
#   
#   если принадлежит то true, если ни один компонент не совпал то false

def getAllFiles(ignore_set):

#возврат всех файлов в текущей дериктории (+игнорируемые)       надо обойти все файлы и вернуть список путей

    files_list = []

    for root, inside, files in os.walk("."):
#   root               текущая папка
#   inside             список имен подпапок внутри root
#   files              список имен файлов внутри root   
        inside[:] = [d for d in inside if not needIgnored(os.path.join(root, d), ignore_set)]

        for file in files:
            full_path = os.path.join(root, file)

            if not needIgnored(full_path, ignore_set):
                real_path = full_path[2:] if full_path.startswith("./") else full_path

                files_list.append(real_path)
    return files_list

#   files_list = []                             создаем список куда будем складывать имена файлов
# 
#   inside[:] = [d for d in inside if not needIgnored(os.path.join(root, d), ignore_set)]
#   основная строчка:
#   -> inside[:]           мы создаем срез всего списка - если присвоить ему новый список, 
#                          то это заменяет его исходное содержимое
#   
#   -> for d in inside     перебор всех подпапок текущей дериктории     
# 
#   -> os.path.join()      полный путь к подпапке ("./src/1.txt")
# 
#   for file in files:                      обход всех файлов в папке root
#   full_path = os.path.join(root, file)    создаем полный путь
#   if not needIgnored()                    проверяем не игнорируеться ли файл
#   
#   real_path = full_path[2:] if full_path.startswith("./") else full_path
#   полный путь часто начинается с "./" поэтому через full_path.startswith("./") проверяем есть ли это начало
#   если его нету то оставляем как есть (полный путь)
#
#   тут еще надо доработать ! (если не тачинаеться с "./")
# 
#   files_list.append(real_path)            добавляем полученный путь в конец списка files_list 
#
#   return files_list                       возвращаем нужные файлы

def getNextCommit():

#возврат след номера комита
#библиотеки: os

    commits_path = ".mygit/commits"

    if not os.path.exists(commits_path):
        return 1
    
    existing = [int(d) for d in os.listdir(commits_path) if d.isdigit()]

    return max(existing) + 1 if existing else 1
    
#   определяет номер след комита
#   
#   надо вернуть числовой номер папки + 1
#   
#   commits_path = ".mygit/commits"             путь к папке
#   
#   if not os.path.exists(commits_path): return 1
#   проверка на сущесвование файла .mygit/commits
#   если ее нету то возвращаем 1 (будет первым)
#   
#   [int(d) for d in os.listdir(commits_path) if d.isdigit()]
#   
#   os.listdir(commits_path)                    список имен которые лежат внутри .mygit/commits
#   if d.isdigit()                              оставляет только имена которые состоят целиком из цифр  
#   
#   existing                                    список чисел
#   
#   return max(existing) + 1 if existing else 1
#   если список не пустой то возвращает максимальный номер+1 

def saveCommit():

#сохранение всех файлов и метданных комита

def restoreCommit():

#замена директории на файлы из указанного комита

def cmdInit():

#инициализация репозитория

def cmdCommit():

#создание коммита

def cmdCheckout():

#переключение на коммит

def main():

#main