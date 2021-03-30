
import os,sys,time





def bersih():
    os.system("clear")
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.05)
sp("Menjalankan Web Server Di Port 5000")
sp("Tunggu Sebentar")
sp("Silahkan Buka Di Chrome (localhost:5000)")
os.system("python2 -m SimpleHTTPServer 5000")
