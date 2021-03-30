
import os,sys,time





def bersih():
    os.system("clear")
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.05)
sp("Menjalankan Web Server Di Port 8080")
sp("Tunggu Sebentar")
os.system("python2 -m SimpleHTTPServer 8080")
