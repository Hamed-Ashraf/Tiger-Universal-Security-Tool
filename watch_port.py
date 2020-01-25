import socket
import threading
import iptc
host = "127.0.0.1"

class MyThread(threading.Thread):

    def __init__(self, host, port, file):

        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.file = file
    def block(self, ip):
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
        rule = iptc.Rule()
        rule.in_interface = "lo"
        rule.src = ip
        target = iptc.Target(rule, "DROP")
        rule.target = target
        chain.insert_rule(rule)
    def listen(self):
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            serv.bind((host, self.port))
        except:
            print("Port " + str(self.port) + " is in use \n")
        serv.listen(5)
        while True:
            conn, addr = serv.accept()
            if (conn): print("client : " + str(addr[0]) + "  trying to connect to you on port " + str(self.port) + "\n")
            self.block(str(addr[0]))
            if not file:
                file.write("this address " + str(addr[0])+ " has been blocked \n")
            else:
                print("this address " + str(addr[0])+ " has been blocked \n")


    def run(self):
        self.listen()

def __main__(file):
    ports = []
    ports_number = int(raw_input("Enter the number of ports to listen to : "))
    for i in range (ports_number):
        ports.append(raw_input("Enter port number : "))
    threads = []
    for i in ports:
        thread = MyThread(host, i, file)
        thread.start()
        threads.append(thread)
    print("Now listenning on ports " + str(ports))
if __name__ =="__main__":
    __main__()
