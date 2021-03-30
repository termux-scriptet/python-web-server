
import os,sys,time





def bersih():
    os.system("clear")
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.05)
sp("Menjalankan Web Server Di Port 3333")
sp("Tunggu Sebentar")
sp("Silahkan Buka Di Chrome (localhost:3333)")
os.system("python2 -m SimpleHTTPServer 3333")
