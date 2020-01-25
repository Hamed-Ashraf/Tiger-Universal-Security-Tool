from os import listdir
from os import stat
from os.path import isfile, join
import os, time

path = ""
last_mod = {}
logs =""

def __main__(file):
    global path, logs
    logs = file
    path = raw_input("Enter the directory path to monitor :  ")
    initialize()
    for i in range(100):
        check()
        time.sleep(2)
def check():
    global current
    check_new_contents()
    check_deleted_contents()
    check_file_updates()

def check_new_contents():
    global last_mod
    check_new_directories(path)
    check_new_files(path)

def check_new_directories(d):
    global logs, last_mod
    for i in listdir(d):
        if join(d, i) not in last_mod.keys() and not isfile(join(d, i)) :
            if logs == "":
                print("this directory was added " + join(d, i) + "\n")
            else:
                logs.write("this directory was added " + join(d, i) + "\n")
            last_mod[join(d, i)] = {}

    for i in listdir(d):
             if join(d, i) in last_mod.keys() and not isfile(join(d, i)):
                 check_new_directories(join(d, i))

def check_new_files(p):
    global logs, last_mod
    for e in listdir(p):
        if isfile(join(p, e)):
            if e not in last_mod[p]:
                last_mod[p][e] = time.ctime(stat(join(p, e))[8])
                if logs == "":
                    print("this file was added " + join(p, e) + " at " + last_mod[p][e] + "\n")
                else:
                    logs.write("this file was added " + join(p, e) + " at " + last_mod[p][e] + "\n")
        else:
            check_new_files(join(p, e))


def check_deleted_contents():
    check_deleted_directories()
    check_deleted_files()

def check_deleted_directories():
    global logs, last_mod
    try:
        for d in last_mod:
            if not os.path.exists(d):
                if logs == "":
                    print("this directory was deleted " + d + "\n")
                else:
                    logs.write("this directory was deleted " + d + "\n")
                del last_mod[d]
    except:
            print()

def check_deleted_files():
    global logs, last_mod
    try:
        for d in last_mod:
            for f in last_mod[d]:
                if f not in listdir(d):
                    del last_mod[d][f]
                    if logs == "":
                        print("this file was deleted " + join(d, f) + "\n")
                    else:
                        logs.write("this file was deleted " + join(d, f) + "\n")
    except:
        print()

def check_file_updates():
    global logs, last_mod
    for d in last_mod:
        for i in last_mod[d]:
            if last_mod[d][i] != time.ctime(stat(join(d, i))[8]):
                last_mod[d][i] = time.ctime(stat(join(d, i))[8])
                if logs == "":
                    print("this file " + join(d, i) + "was updated at " + last_mod[d][i] + "\n")
                else:
                    logs.write("this file " + join(d, i) + "was updated at " + last_mod[d][i] + "\n")
def initialize():

    if os.path.exists(path):
        print("This directory "+ path + " will be watched recursively ^_^ \n")
        get_files(path)
    else:
        print("this path doesn't exist")
def get_files(p):
    global last_mod
    last_mod[p] = {}
    for e in listdir(p):
        if isfile(join(p, e)):
            last_mod[p][e] = time.ctime(stat(join(p, e))[8])
        else:
            get_files(join(p, e))

if __name__ == "__main__":
    main()
