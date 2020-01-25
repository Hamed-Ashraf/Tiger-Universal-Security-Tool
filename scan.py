import socket
import os
from datetime import datetime
import threading
import nmap
file = ""
class MyThread(threading.Thread):

   def __init__(self, ip, st_port, end_port):

      threading.Thread.__init__(self)
      self.list = []
      self.open_ports = {}
      self.st_port = st_port
      self.end_port = end_port
      self.ip = ip
      self.nm = nmap.PortScanner()
   def start_scan(self):
      for i in range(self.st_port, self.end_port):
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         conn = s.connect_ex((self.ip, i))
         if (conn == 0):
            self.list.append(i)
         else:
           s.close()
      if len(self.list) != 0:
         port_str=""
         for i in self.list:
            port_str += str(i) + ","
         port_str = port_str[:-1]
         x = self.nm.scan(self.ip, port_str, arguments='-sC -sV ')
         ports= x['scan'][str(self.ip)]['tcp']
         for i in ports.keys() :
            print( str(i) +  "  " + ports[i]['name'] + "  " + ports[i]['product'] + "  " + ports[i]['version'] )

   def run(self):
      self.start_scan()

def __main__(log):
   file = log
   ip = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]
   file.write("your ip is : " + ip + "\n")
   print ("your ip is : " + ip + "\n")
   start_ip = 2; end_ip = 254

   sub_ip = ip.split(".")[0] + "." + ip.split(".")[1] + "." + ip.split(".")[2]
   for i in range(start_ip, end_ip + 1):
      ip = sub_ip + "." + str(i)
      print("Scanning " + ip + "\n")
      file.write("Scanning " + ip + "\n")
      comm = "ping -c 1 " + ip
      response = os.popen(comm)
      for line in response.readlines():
         if line.count("ttl"):
            if not file:
               print(ip, "is Live")
               print("  Scanning ip : " + ip)
            else:
               file.write(ip + "is Live")
               file.write("  Scanning ip : " + ip)
            st_port = input("Enter start port : ")
            end_port = input("Enter end port : ")
            total_ports = int(end_port) - int(st_port) + 1
            pointer = int(st_port)
            threads = []
            needed_threads = (total_ports / 10000) + 1
            for i in range(int(needed_threads)):
               if  int(end_port)-pointer >= 10000:
                  thread = MyThread(ip, pointer, pointer + 10000)
                  thread.start()
                  threads.append(thread)
                  pointer += 10000
               else:
                  thread = MyThread(ip, pointer, int(end_port))
                  thread.start()
                  threads.append(thread)
                  break
            for t in threads:
               t.join()
      print("finished scanning " + ip + "\n")

if __name__ == "__main__":
   __main__()
