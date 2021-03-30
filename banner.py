import os,sys,time

def judul():
    print(" Tools Web Server Mengunakan Python ")

def bersih():
    os.system("clear")
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.03)

def main():
    bersih()
    judul()
    sp("+------------------------------------+")
    sp("Author : Aditia")
    sp("Github : https://github.com/Hack4life")
    sp("+------------------------------------+")
main()
