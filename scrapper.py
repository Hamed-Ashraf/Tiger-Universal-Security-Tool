import requests
import re
from bs4 import BeautifulSoup
from bs4 import Comment


def find_tags(data, tag):
    soup = BeautifulSoup(data, 'lxml')
    tags = []
    for i in soup.find_all(tag):
        if i not in tags:
            tags.append(i)
    return tags
def find_comments(data):
    comments = []
    soup = BeautifulSoup(data, 'lxml')
    for i in soup.find_all(string = lambda text: isinstance(text, Comment)):
        comments.append(i.extract)
    return comments


def print_list():
    print("\n")
    print("1-  Get Tags \n")
    print("2-  Get Comments \n")
    print("3-  Get Domains \n")
    print("4-  Get URLS \n")

def __main__(file):
    url = str(raw_input(" Enter the website to scrap :"))
    print_list()
    choice = raw_input(" Enter the number of your choice : ")
    response = requests.get(url)
    data = response.text
    if choice == "1":
        tag = raw_input(" Enter the tag you want : ")
        outputs = find_tags(data, tag)
        if file:
            for i in outputs:
                file.write(str(i) + "\n")
        else:
            print(outputs)
    elif choice =="2":
        comments = find_comments(data)
        if file:
            for i in comments:
                file.write(str(i) + "\n")
        else:
            print(comments)
    elif choice == "3":
        reg = "([a-z0-9][a-z0-9\-]{1,61}\.)+[0-9a-z]{1}"
        domains= re.findall(reg, data)
        file.write(domains)

    elif choice =="4":
        reg = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        urls = re.findall(reg, data)
        if file:
            for i in urls:
                file.write(str(i) + "\n")
        else:
            for i in urls:
                print(str(i) + "\n")

if __name__ == "__main__":
    __main__()