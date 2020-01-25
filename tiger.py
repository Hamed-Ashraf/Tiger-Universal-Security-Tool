import scan
import parse_logs
import monitor
import watch_port
import scrapper
#import scrapper


def print_list():
    print("""
        1-   Tiger Log Parser
        2-   Tiger Directory monitor
        3-   Tiger network scanner
        4-   Tiger port Defender
        5-   Tiger Web Scrapper
    """)
    choice = int(input("Enter the number of the function you want : "))
    if choice in range(1, 6):
        pass
    else:
        print_list()
    output = raw_input("Enter f to print to a file or s to print on screen :  ")
    file = ""
    if output == "f":
        try:
             file = raw_input("Enter the path to the file to put outputs : ")
             file = open(file, 'w')
        except:
            print("couldn't find this file \n")

    return choice, output, file

def __main__():
    print("""

                         __,,,,_
           _ __..-;''`--/'/ /.',-`-.
       (`/' ` |  \ \ \\ / / / / .-'/`,_
      /'`\ \   |  \ | \| // // / -.,/_,'-,
     /<7' ;  \ \  | ; ||/ /| | \/    |`-/,/-.,_,/')
    /  _.-, `,-\,__|  _-| / \ \/|_/  |    '-/.;.\'
    `-`  f/ ;      / __/ \__ `/ |__/ |
         `-'      |  -| =|\_  \  |-' |
               __/   /_..-' `  ),'  //
            ((__.-'((___..-'' \__.'

            Welcome to Tiger Universal Tool
        /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

    """)
    print('                         Under supervision of the one and the only ((   Kawkab  )) ')

    choice,output, file = print_list()
    if choice == 1:
        parse_logs.__main__(file)
    elif choice == 2:
        monitor.__main__(file)
    elif choice == 3:
        scan.__main__(file)
    elif choice == 4:
        watch_port.__main__(file)
    elif choice == 5:
        scrapper.__main__(file)
    else:
        print("please Enter a correct number \n")
        choice = print_list()

if __name__ == "__main__":
    __main__()
