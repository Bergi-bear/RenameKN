#Это код удаляет имя Получателя выписки на всех страницах всех XML
# документов в текущей папке и подпапках
import os
import re

name = "Таратухина Марина Алексеевна"
newName = "Иванов Алексей Семенович"


# Получаем список всех XML
def GetXMLList():
    s = []
    xml = []
    for root, dirs, files in os.walk("."):
        for filename in files:
            s.append(filename)

    for i in s:
        x = re.search(".xml", i)
        if x is not None:
            xml.append(i)
            # print(i)
    return xml


def ReplaceName(filename, oldname, newname):
    f = open(filename, "r", encoding="utf-8")
    copy = []
    for line in f:
        # print(line)
        x = re.search(oldname, line)
        if x is not None:
            line = line.replace(oldname, newname)
            #print(x)
        copy.append(line)
    f = open(filename, 'w', encoding="utf-8")
    for index in copy:
        f.write(index)
    f.close()


for i in GetXMLList():
    print(i)
    #if os.path.exists(i):
    ReplaceName(i, name, newName)
