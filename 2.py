
import os,sys,time





def bersih():
    os.system("clear")
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.05)
sp("Menjalankan Web Server Di Port 4444")
sp("Tunggu Sebentar")
sp("Silahkan Buka Di Chrome (localhost:4444)")
os.system("python2 -m SimpleHTTPServer 4444")
