#!/usr/bin/python
import time
import os.path

def readTemp():

    dirname = '/sys/bus/w1/devices'
    listOfFiles = [f for f in os.listdir(dirname)]# if os.path.isdir(f)]
    print listOfFiles

    for file in listOfFiles:
       f = file
       print (f)
       f1 = os.path.join(os.path.join(dirname, f), "w1_slave")
       print (f1)

       if os.path.exists(f1):

          f2 = open(f1, 'r')
          text = f2.readlines()

          print(text)

          for s in text: 
             print "string : " + s


          temp = -1
          if 'YES' in text[0]:
             pos = text[1].find('t=') + 2
             temp = int(text[1][pos: ])
             print "temp for "+ f + "  = " + str(temp/1000.0)

          f2.close()

  
    return 0
 
def main():
 
  while True:
    readTemp()
    time.sleep(5)
   
if __name__=="__main__":
   main()