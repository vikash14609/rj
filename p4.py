  #  def start_new_thread(function, args, kwargs={}):
     #def start_new_thread(function, args, kwargs={}):
    #"""Dummy implementation of _thread.start_new_thread().

    #Compatibility is maintained by making sure that ``args`` is a
    #tuple and ``kwargs`` is a dictionary.  If an exception is raised
    #and it is SystemExit (which can be done by _thread.exit()) it is
    #caught and nothing is done; all other exceptions are printed out
    #by using traceback.print_exc().

    #If the executed function calls interrupt_main the KeyboardInterrupt will be
    #raised when the function returns.

    #"""
    #if type(args) != type(tuple()):
    #    raise TypeError("2nd arg must be a tuple")
    #if type(kwargs) != type(dict()):
    #    raise TypeError("3rd arg must be a dict")
    #global _main
    #_main = False
    #try:
     #   function(*args, **kwargs)
    #except SystemExit:
     #   pass
    #except:
     #   import traceback
     #   traceback.print_exc()
  #  _main = True
   # global _interrupt
   # if _interrupt:
   #     _interrupt = False
   #     raise KeyboardInterrupt
   # def exit():
   # """Dummy implementation of _thread.exit()."""
   # raise SystemExit
def checkers() :
 from sys import stdin
 import requests
 import uuid
 import socket
 from urllib.request import urlopen, Request
 class color:
     PURPLE = '\033[95m'
     CYAN = '\033[96m'
     DARKCYAN = '\033[36m'
     BLUE = '\033[94m'
     GREEN = '\033[92m'
     YELLOW = '\033[93m'
     RED = '\033[91m'
     BOLD = '\033[1m'
     UNDERLINE = '\033[4m'
     END = '\033[0m'
 f = open("../downloads/i.txt")
 line = f.readline()
 totalLines = len(f.readlines())
 f.close()
 f = open("../downloads/i.txt")
 lines = f.readlines()
 url = "https://mailsac.com/inbox/" + lines[0].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
   print (color.RED + "SCRAPPING " + color.END)
 else:
   print (color.RED + "SCRAPPED" + color.GREEN + lines[0] + color.END)

 url = "https://mailsac.com/inbox/" + lines[1].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
     print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[1] + color.END)
  
 url = "https://mailsac.com/inbox/" + lines[2].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[2] + color.END)

 url = "https://mailsac.com/inbox/" + lines[3].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[3] + color.END)

 url = "https://mailsac.com/inbox/" + lines[4].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[4] + color.END)


 url = "https://mailsac.com/inbox/" + lines[5].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[5] + color.END)



 url = "https://mailsac.com/inbox/" + lines[6].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[6] + color.END)



 url = "https://mailsac.com/inbox/" + lines[7].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[7] + color.END)



 url = "https://mailsac.com/inbox/" + lines[8].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[8] + color.END)



 url = "https://mailsac.com/inbox/" + lines[9].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[9] + color.END)



 url = "https://mailsac.com/inbox/" + lines[10].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[10] + color.END)



 url = "https://mailsac.com/inbox/" + lines[11].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[11] + color.END)



 url = "https://mailsac.com/inbox/" + lines[12].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[12] + color.END)


 url = "https://mailsac.com/inbox/" + lines[13].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[13] + color.END)



 url = "https://mailsac.com/inbox/" + lines[14].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[14] + color.END)



 url = "https://mailsac.com/inbox/" + lines[15].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[15] + color.END)




 url = "https://mailsac.com/inbox/" + lines[16].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[16] + color.END)



 url = "https://mailsac.com/inbox/" + lines[17].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[17] + color.END)



 url = "https://mailsac.com/inbox/" + lines[18].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[18] + color.END)




 url = "https://mailsac.com/inbox/" + lines[19].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[19] + color.END)



 url = "https://mailsac.com/inbox/" + lines[20].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[20] + color.END)



 url = "https://mailsac.com/inbox/" + lines[21].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[21] + color.END)



 url = "https://mailsac.com/inbox/" + lines[22].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[22] + color.END)



 url = "https://mailsac.com/inbox/" + lines[23].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[23] + color.END)



 url = "https://mailsac.com/inbox/" + lines[24].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[24] + color.END)



 url = "https://mailsac.com/inbox/" + lines[25].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print ('done')
    
 url = "https://mailsac.com/inbox/" + lines[26].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[26] + color.END)    
    
 url = "https://mailsac.com/inbox/" + lines[27].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[27] + color.END)
        
 url = "https://mailsac.com/inbox/" + lines[28].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[28] + color.END)


 url = "https://mailsac.com/inbox/" + lines[29].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[29] + color.END)

 url = "https://mailsac.com/inbox/" + lines[30].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[30] + color.END)


 url = "https://mailsac.com/inbox/" + lines[31].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[31] + color.END)


 url = "https://mailsac.com/inbox/" + lines[32].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[32] + color.END)



 url = "https://mailsac.com/inbox/" + lines[33].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[33] + color.END)



 url = "https://mailsac.com/inbox/" + lines[34].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[34] + color.END)



 url = "https://mailsac.com/inbox/" + lines[35].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[35] + color.END)


 url = "https://mailsac.com/inbox/" + lines[36].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[36] + color.END)


 url = "https://mailsac.com/inbox/" + lines[37].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[37] + color.END)

 url = "https://mailsac.com/inbox/" + lines[38].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[38] + color.END)


 url = "https://mailsac.com/inbox/" + lines[39].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[39] + color.END)


 url = "https://mailsac.com/inbox/" + lines[40].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[40] + color.END)


 url = "https://mailsac.com/inbox/" + lines[41].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[41] + color.END)

 url = "https://mailsac.com/inbox/" + lines[42].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[42] + color.END)


 url = "https://mailsac.com/inbox/" + lines[43].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[43] + color.END)


 url = "https://mailsac.com/inbox/" + lines[44].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[44] + color.END)


 url = "https://mailsac.com/inbox/" + lines[45].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[45] + color.END)


 url = "https://mailsac.com/inbox/" + lines[46].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[46] + color.END)

 url = "https://mailsac.com/inbox/" + lines[47].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[47] + color.END)


 url = "https://mailsac.com/inbox/" + lines[48].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[48] + color.END)


 url = "https://mailsac.com/inbox/" + lines[49].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[49] + color.END)


 url = "https://mailsac.com/inbox/" + lines[50].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[50] + color.END)


 url = "https://mailsac.com/inbox/" + lines[51].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[51] + color.END)


 url = "https://mailsac.com/inbox/" + lines[52].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[52] + color.END)


 url = "https://mailsac.com/inbox/" + lines[53].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[53] + color.END)


 url = "https://mailsac.com/inbox/" + lines[54].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[54] + color.END)


 url = "https://mailsac.com/inbox/" + lines[55].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[55] + color.END)


 url = "https://mailsac.com/inbox/" + lines[56].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[56] + color.END)


 url = "https://mailsac.com/inbox/" + lines[57].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[57] + color.END)


 url = "https://mailsac.com/inbox/" + lines[58].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[58] + color.END)


 url = "https://mailsac.com/inbox/" + lines[59].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[59] + color.END)


 url = "https://mailsac.com/inbox/" + lines[60].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[60] + color.END)


 url = "https://mailsac.com/inbox/" + lines[61].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[61] + color.END)


 url = "https://mailsac.com/inbox/" + lines[62].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[62] + color.END)

 url = "https://mailsac.com/inbox/" + lines[63].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[63] + color.END)

 url = "https://mailsac.com/inbox/" + lines[64].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[64] + color.END)


 url = "https://mailsac.com/inbox/" + lines[65].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[65] + color.END)


 url = "https://mailsac.com/inbox/" + lines[66].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[66] + color.END)


 url = "https://mailsac.com/inbox/" + lines[67].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[67] + color.END)

 url = "https://mailsac.com/inbox/" + lines[68].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[68] + color.END)


 url = "https://mailsac.com/inbox/" + lines[69].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[69] + color.END)

 url = "https://mailsac.com/inbox/" + lines[70].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[70] + color.END)


 url = "https://mailsac.com/inbox/" + lines[71].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[71] + color.END)


 url = "https://mailsac.com/inbox/" + lines[72].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[72] + color.END)


 url = "https://mailsac.com/inbox/" + lines[73].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[73] + color.END)


 url = "https://mailsac.com/inbox/" + lines[74].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[74] + color.END)


 url = "https://mailsac.com/inbox/" + lines[75].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[75] + color.END)

 url = "https://mailsac.com/inbox/" + lines[76].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[76] + color.END)


 url = "https://mailsac.com/inbox/" + lines[77].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[77] + color.END)


 url = "https://mailsac.com/inbox/" + lines[78].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[78] + color.END)


 url = "https://mailsac.com/inbox/" + lines[79].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[79] + color.END)

 url = "https://mailsac.com/inbox/" + lines[80].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[80] + color.END)

 url = "https://mailsac.com/inbox/" + lines[81].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[81] + color.END)

 url = "https://mailsac.com/inbox/" + lines[82].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[82] + color.END)

 url = "https://mailsac.com/inbox/" + lines[83].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[83] + color.END)

 url = "https://mailsac.com/inbox/" + lines[84].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[84] + color.END)


 url = "https://mailsac.com/inbox/" + lines[85].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[85] + color.END)


 url = "https://mailsac.com/inbox/" + lines[86].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[86] + color.END)


 url = "https://mailsac.com/inbox/" + lines[87].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[87] + color.END)


 url = "https://mailsac.com/inbox/" + lines[88].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[88] + color.END)

 url = "https://mailsac.com/inbox/" + lines[89].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[89] + color.END)

 url = "https://mailsac.com/inbox/" + lines[90].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[90] + color.END)

 url = "https://mailsac.com/inbox/" + lines[91].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[91] + color.END)

 url = "https://mailsac.com/inbox/" + lines[92].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[92] + color.END)


 url = "https://mailsac.com/inbox/" + lines[93].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[93] + color.END)


 url = "https://mailsac.com/inbox/" + lines[94].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[94] + color.END)


 url = "https://mailsac.com/inbox/" + lines[95].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[95] + color.END)


 url = "https://mailsac.com/inbox/" + lines[96].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[96] + color.END)


 url = "https://mailsac.com/inbox/" + lines[97].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[97] + color.END)


 url = "https://mailsac.com/inbox/" + lines[98].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[98] + color.END)


 url = "https://mailsac.com/inbox/" + lines[99].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[99] + color.END)


 url = "https://mailsac.com/inbox/" + lines[100].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
  print (color.YELLOW + "SCRAPPING")
  print ('''
  ++++++++++++++++++++++++++++
  100 Checks Completed / 500
  +++++++++++++++++++++++++++	
  ''')
  print ("" + color.END)	
 else:
  print (color.YELLOW + "SCRAPPED" + color.GREEN + lines[100])
  print ('''
	        ++++++++++++++++++++++++++++
			 100 Checks Completed / 500
            ++++++++++++++++++++++++++++	
    ''')
  print ("" + color.END)
   

 url = "https://mailsac.com/inbox/" + lines[101].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[101] + color.END)


 url = "https://mailsac.com/inbox/" + lines[102].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[102] + color.END)


 url = "https://mailsac.com/inbox/" + lines[103].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[103] + color.END)


 url = "https://mailsac.com/inbox/" + lines[104].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[104] + color.END)


 url = "https://mailsac.com/inbox/" + lines[105].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[105] + color.END)


 url = "https://mailsac.com/inbox/" + lines[106].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[106] + color.END)


 url = "https://mailsac.com/inbox/" + lines[107].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[107] + color.END)


 url = "https://mailsac.com/inbox/" + lines[108].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[108] + color.END)


 url = "https://mailsac.com/inbox/" + lines[109].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[109] + color.END)


 url = "https://mailsac.com/inbox/" + lines[110].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[110] + color.END)


 url = "https://mailsac.com/inbox/" + lines[111].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[111] + color.END)


 url = "https://mailsac.com/inbox/" + lines[112].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[112] + color.END)


 url = "https://mailsac.com/inbox/" + lines[113].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[113] + color.END)


 url = "https://mailsac.com/inbox/" + lines[114].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[114] + color.END)


 url = "https://mailsac.com/inbox/" + lines[115].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[115] + color.END)


 url = "https://mailsac.com/inbox/" + lines[116].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[116] + color.END)


 url = "https://mailsac.com/inbox/" + lines[117].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[117] + color.END)

 url = "https://mailsac.com/inbox/" + lines[118].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[118] + color.END)

 url = "https://mailsac.com/inbox/" + lines[119].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[119] + color.END)

 url = "https://mailsac.com/inbox/" + lines[120].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[120] + color.END)

 url = "https://mailsac.com/inbox/" + lines[121].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[121] + color.END)

 url = "https://mailsac.com/inbox/" + lines[122].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[122] + color.END)


 url = "https://mailsac.com/inbox/" + lines[123].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[123] + color.END)

 url = "https://mailsac.com/inbox/" + lines[124].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[124] + color.END)


 url = "https://mailsac.com/inbox/" + lines[125].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[125] + color.END)

 url = "https://mailsac.com/inbox/" + lines[126].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[126] + color.END)


 url = "https://mailsac.com/inbox/" + lines[127].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[127] + color.END)


 url = "https://mailsac.com/inbox/" + lines[128].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[128] + color.END)

 url = "https://mailsac.com/inbox/" + lines[129].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[129] + color.END)

 url = "https://mailsac.com/inbox/" + lines[130].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[130] + color.END)

 url = "https://mailsac.com/inbox/" + lines[131].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[131] + color.END)


 url = "https://mailsac.com/inbox/" + lines[132].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[132] + color.END)


 url = "https://mailsac.com/inbox/" + lines[133].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[133] + color.END)


 url = "https://mailsac.com/inbox/" + lines[134].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[134] + color.END)

 url = "https://mailsac.com/inbox/" + lines[135].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[135] + color.END)


 url = "https://mailsac.com/inbox/" + lines[136].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[136] + color.END)


 url = "https://mailsac.com/inbox/" + lines[137].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[137] + color.END)

 url = "https://mailsac.com/inbox/" + lines[138].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[138] + color.END)

 url = "https://mailsac.com/inbox/" + lines[139].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[139] + color.END)

 url = "https://mailsac.com/inbox/" + lines[140].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[140] + color.END)


 url = "https://mailsac.com/inbox/" + lines[141].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[141] + color.END)


 url = "https://mailsac.com/inbox/" + lines[142].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[142] + color.END)


 url = "https://mailsac.com/inbox/" + lines[143].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[143] + color.END)


 url = "https://mailsac.com/inbox/" + lines[144].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[144] + color.END)


 url = "https://mailsac.com/inbox/" + lines[145].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[145] + color.END)

 url = "https://mailsac.com/inbox/" + lines[146].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[146] + color.END)

 url = "https://mailsac.com/inbox/" + lines[147].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[147] + color.END)

 url = "https://mailsac.com/inbox/" + lines[148].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[148] + color.END)

 url = "https://mailsac.com/inbox/" + lines[149].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[149] + color.END)

 url = "https://mailsac.com/inbox/" + lines[150].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[150] + color.END)

 url = "https://mailsac.com/inbox/" + lines[151].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[151] + color.END)

 url = "https://mailsac.com/inbox/" + lines[152].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[152] + color.END)

 url = "https://mailsac.com/inbox/" + lines[153].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[153] + color.END)

 url = "https://mailsac.com/inbox/" + lines[154].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[154] + color.END)

 url = "https://mailsac.com/inbox/" + lines[155].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[155] + color.END)

 url = "https://mailsac.com/inbox/" + lines[156].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[156] + color.END)

 url = "https://mailsac.com/inbox/" + lines[157].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[157] + color.END)


 url = "https://mailsac.com/inbox/" + lines[158].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[158] + color.END)


 url = "https://mailsac.com/inbox/" + lines[159].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[159] + color.END)


 url = "https://mailsac.com/inbox/" + lines[160].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[160] + color.END)


 url = "https://mailsac.com/inbox/" + lines[161].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[161] + color.END)


 url = "https://mailsac.com/inbox/" + lines[162].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[162] + color.END)

 url = "https://mailsac.com/inbox/" + lines[163].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[163] + color.END)


 url = "https://mailsac.com/inbox/" + lines[164].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[164] + color.END)


 url = "https://mailsac.com/inbox/" + lines[165].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[165] + color.END)


 url = "https://mailsac.com/inbox/" + lines[166].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[166] + color.END)


 url = "https://mailsac.com/inbox/" + lines[167].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[167] + color.END)


 url = "https://mailsac.com/inbox/" + lines[168].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[168] + color.END)


 url = "https://mailsac.com/inbox/" + lines[169].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[169] + color.END)


 url = "https://mailsac.com/inbox/" + lines[170].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[170] + color.END)



 url = "https://mailsac.com/inbox/" + lines[171].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[171] + color.END)


 url = "https://mailsac.com/inbox/" + lines[172].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[172] + color.END)



 url = "https://mailsac.com/inbox/" + lines[173].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[173] + color.END)



 url = "https://mailsac.com/inbox/" + lines[174].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[174] + color.END)



 url = "https://mailsac.com/inbox/" + lines[175].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[175] + color.END)



 url = "https://mailsac.com/inbox/" + lines[176].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[176] + color.END)


 url = "https://mailsac.com/inbox/" + lines[177].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[177] + color.END)


 url = "https://mailsac.com/inbox/" + lines[178].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[178] + color.END)


 url = "https://mailsac.com/inbox/" + lines[179].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[179] + color.END)


 url = "https://mailsac.com/inbox/" + lines[180].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[180] + color.END)


 url = "https://mailsac.com/inbox/" + lines[181].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[181] + color.END)


 url = "https://mailsac.com/inbox/" + lines[182].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[182] + color.END)


 url = "https://mailsac.com/inbox/" + lines[183].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[183] + color.END)


 url = "https://mailsac.com/inbox/" + lines[184].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[184] + color.END)


 url = "https://mailsac.com/inbox/" + lines[185].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[185] + color.END)

 url = "https://mailsac.com/inbox/" + lines[186].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[186] + color.END)


 url = "https://mailsac.com/inbox/" + lines[187].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[187] + color.END)


 url = "https://mailsac.com/inbox/" + lines[188].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[188] + color.END)



 url = "https://mailsac.com/inbox/" + lines[189].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[189] + color.END)



 url = "https://mailsac.com/inbox/" + lines[190].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[190] + color.END)

 url = "https://mailsac.com/inbox/" + lines[191].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[191] + color.END)


 url = "https://mailsac.com/inbox/" + lines[192].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[192] + color.END)

 url = "https://mailsac.com/inbox/" + lines[193].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[193] + color.END)

 url = "https://mailsac.com/inbox/" + lines[194].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[194] + color.END)


 url = "https://mailsac.com/inbox/" + lines[195].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[195] + color.END)

 url = "https://mailsac.com/inbox/" + lines[196].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[196] + color.END)


 url = "https://mailsac.com/inbox/" + lines[197].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[197] + color.END)


 url = "https://mailsac.com/inbox/" + lines[198].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[198] + color.END)


 url = "https://mailsac.com/inbox/" + lines[199].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[199] + color.END)


 url = "https://mailsac.com/inbox/" + lines[200].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[200] + color.END)
	
 url = "https://mailsac.com/inbox/" + lines[201].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
  print (color.YELLOW + "SCRAPPING")
  print ('''
	        ++++++++++++++++++++++++++++
			 201 Checks Completed / 500
            ++++++++++++++++++++++++++++	
         ''')
  print ("" + color.END)	
 else:
  print (color.YELLOW + "SCRAPPED" + color.GREEN + lines[100])
  print ('''
	        ++++++++++++++++++++++++++++
			 201 Checks Completed / 500
            ++++++++++++++++++++++++++++	
    ''')
  print ("" + color.END)
 url = "https://mailsac.com/inbox/" + lines[202].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[202] + color.END)
 url = "https://mailsac.com/inbox/" + lines[203].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[203] + color.END)
 url = "https://mailsac.com/inbox/" + lines[204].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[204] + color.END)
 url = "https://mailsac.com/inbox/" + lines[205].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[205] + color.END)
 url = "https://mailsac.com/inbox/" + lines[206].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[206] + color.END)
 url = "https://mailsac.com/inbox/" + lines[207].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[207] + color.END)
 url = "https://mailsac.com/inbox/" + lines[208].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[208] + color.END)
 url = "https://mailsac.com/inbox/" + lines[209].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[209] + color.END)
 url = "https://mailsac.com/inbox/" + lines[210].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[210] + color.END)
 url = "https://mailsac.com/inbox/" + lines[211].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[211] + color.END)
 url = "https://mailsac.com/inbox/" + lines[212].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[212] + color.END)
 url = "https://mailsac.com/inbox/" + lines[213].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[213] + color.END)
 url = "https://mailsac.com/inbox/" + lines[214].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[214] + color.END)
 url = "https://mailsac.com/inbox/" + lines[215].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[215] + color.END)
 url = "https://mailsac.com/inbox/" + lines[216].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[216] + color.END)
 url = "https://mailsac.com/inbox/" + lines[217].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[217] + color.END)
 url = "https://mailsac.com/inbox/" + lines[218].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[218] + color.END)
 url = "https://mailsac.com/inbox/" + lines[219].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[219] + color.END)
 url = "https://mailsac.com/inbox/" + lines[220].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[220] + color.END)
 url = "https://mailsac.com/inbox/" + lines[221].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[221] + color.END)
 url = "https://mailsac.com/inbox/" + lines[222].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[222] + color.END)
 url = "https://mailsac.com/inbox/" + lines[223].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[223] + color.END)
 url = "https://mailsac.com/inbox/" + lines[224].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[224] + color.END)
 url = "https://mailsac.com/inbox/" + lines[225].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[225] + color.END)
 url = "https://mailsac.com/inbox/" + lines[226].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[226] + color.END)
 url = "https://mailsac.com/inbox/" + lines[227].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[227] + color.END)
 url = "https://mailsac.com/inbox/" + lines[228].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[229] + color.END)
 url = "https://mailsac.com/inbox/" + lines[230].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[230] + color.END)
 url = "https://mailsac.com/inbox/" + lines[231].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[231] + color.END)
 url = "https://mailsac.com/inbox/" + lines[232].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[232] + color.END)
 url = "https://mailsac.com/inbox/" + lines[233].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[233] + color.END)
 url = "https://mailsac.com/inbox/" + lines[234].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[234] + color.END)
 url = "https://mailsac.com/inbox/" + lines[235].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[235] + color.END)
 url = "https://mailsac.com/inbox/" + lines[236].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[236] + color.END)
 url = "https://mailsac.com/inbox/" + lines[237].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[237] + color.END)
 url = "https://mailsac.com/inbox/" + lines[237].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[237] + color.END)
 url = "https://mailsac.com/inbox/" + lines[238].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[238] + color.END)
 url = "https://mailsac.com/inbox/" + lines[239].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[239] + color.END)
 url = "https://mailsac.com/inbox/" + lines[240].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[240] + color.END)
 url = "https://mailsac.com/inbox/" + lines[241].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[241] + color.END)
 url = "https://mailsac.com/inbox/" + lines[242].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[242] + color.END)
 url = "https://mailsac.com/inbox/" + lines[243].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[243] + color.END)
 url = "https://mailsac.com/inbox/" + lines[244].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[244] + color.END)
 url = "https://mailsac.com/inbox/" + lines[245].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[245] + color.END)
 url = "https://mailsac.com/inbox/" + lines[246].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[246] + color.END)
 url = "https://mailsac.com/inbox/" + lines[247].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[247] + color.END)
 url = "https://mailsac.com/inbox/" + lines[248].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[248] + color.END)
 url = "https://mailsac.com/inbox/" + lines[249].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[249] + color.END)
 url = "https://mailsac.com/inbox/" + lines[250].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[250] + color.END)
 url = "https://mailsac.com/inbox/" + lines[251].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[251] + color.END)	
 url = "https://mailsac.com/inbox/" + lines[252].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[252] + color.END)
 url = "https://mailsac.com/inbox/" + lines[253].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[253] + color.END)
 url = "https://mailsac.com/inbox/" + lines[254].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[254] + color.END)
 url = "https://mailsac.com/inbox/" + lines[255].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[255] + color.END)
 url = "https://mailsac.com/inbox/" + lines[256].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[257] + color.END)
 url = "https://mailsac.com/inbox/" + lines[258].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[258] + color.END)
 url = "https://mailsac.com/inbox/" + lines[259].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[259] + color.END)
 url = "https://mailsac.com/inbox/" + lines[260].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[260] + color.END)
 url = "https://mailsac.com/inbox/" + lines[261].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[261] + color.END)
 url = "https://mailsac.com/inbox/" + lines[262].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[262] + color.END)
 url = "https://mailsac.com/inbox/" + lines[263].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[263] + color.END)
 url = "https://mailsac.com/inbox/" + lines[264].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[264] + color.END)
 url = "https://mailsac.com/inbox/" + lines[265].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[265] + color.END)
 url = "https://mailsac.com/inbox/" + lines[266].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[266] + color.END)
 url = "https://mailsac.com/inbox/" + lines[267].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[267] + color.END)
 url = "https://mailsac.com/inbox/" + lines[268].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[268] + color.END)
 url = "https://mailsac.com/inbox/" + lines[269].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[269] + color.END)
 url = "https://mailsac.com/inbox/" + lines[270].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[270] + color.END)
 url = "https://mailsac.com/inbox/" + lines[271].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[271] + color.END)
 url = "https://mailsac.com/inbox/" + lines[272].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print(color.RED + "SCRAPPED" + color.GREEN + lines[272] + color.END)	
 url = "https://mailsac.com/inbox/" + lines[273].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[273] + color.END)
 url = "https://mailsac.com/inbox/" + lines[274].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[274] + color.END)
 url = "https://mailsac.com/inbox/" + lines[275].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[275] + color.END)
 url = "https://mailsac.com/inbox/" + lines[276].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[276] + color.END)
 url = "https://mailsac.com/inbox/" + lines[277].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[277] + color.END)
 url = "https://mailsac.com/inbox/" + lines[278].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[278] + color.END)
 url = "https://mailsac.com/inbox/" + lines[279].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[279] + color.END)
 url = "https://mailsac.com/inbox/" + lines[280].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[280] + color.END)
 url = "https://mailsac.com/inbox/" + lines[281].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[281] + color.END)
 url = "https://mailsac.com/inbox/" + lines[282].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[282] + color.END)
 url = "https://mailsac.com/inbox/" + lines[283].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[283] + color.END)
 url = "https://mailsac.com/inbox/" + lines[284].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[284] + color.END)
 url = "https://mailsac.com/inbox/" + lines[285].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[285] + color.END)
 url = "https://mailsac.com/inbox/" + lines[286].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[286] + color.END)
 url = "https://mailsac.com/inbox/" + lines[287].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[287] + color.END)
 url = "https://mailsac.com/inbox/" + lines[288].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[288] + color.END)
 url = "https://mailsac.com/inbox/" + lines[289].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[289] + color.END)
 url = "https://mailsac.com/inbox/" + lines[290].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[290] + color.END)
 url = "https://mailsac.com/inbox/" + lines[291].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[291] + color.END)
 url = "https://mailsac.com/inbox/" + lines[292].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[292] + color.END)
 url = "https://mailsac.com/inbox/" + lines[293].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[293] + color.END)
 url = "https://mailsac.com/inbox/" + lines[294].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[294] + color.END)
 url = "https://mailsac.com/inbox/" + lines[295].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[295] + color.END)
 url = "https://mailsac.com/inbox/" + lines[296].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[296] + color.END)
 url = "https://mailsac.com/inbox/" + lines[297].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[297] + color.END)
 url = "https://mailsac.com/inbox/" + lines[298].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[298] + color.END)
 url = "https://mailsac.com/inbox/" + lines[299].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[299] + color.END)
 url = "https://mailsac.com/inbox/" + lines[300].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
  print (color.YELLOW + "SCRAPPING")
  print ('''
             +++++++++++++++++++++++++++
             300 Checks Completed / 500
             ++++++++++++++++++++++++++++	
  ''')
  print ("" + color.END)	
 else:
  print (color.YELLOW + "SCRAPPED" + color.GREEN + lines[300])
  print ('''
	        ++++++++++++++++++++++++++++
			 300 Checks Completed / 500
            ++++++++++++++++++++++++++++	
    ''')
  print ("" + color.END)
   
 url = "https://mailsac.com/inbox/" + lines[301].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[301] + color.END)
 url = "https://mailsac.com/inbox/" + lines[302].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[302] + color.END)
 url = "https://mailsac.com/inbox/" + lines[303].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[303] + color.END)
 url = "https://mailsac.com/inbox/" + lines[304].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[304] + color.END)
 url = "https://mailsac.com/inbox/" + lines[305].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[305] + color.END)
 url = "https://mailsac.com/inbox/" + lines[305].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[305] + color.END)
 url = "https://mailsac.com/inbox/" + lines[306].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[306] + color.END)
 url = "https://mailsac.com/inbox/" + lines[307].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[307] + color.END)
 url = "https://mailsac.com/inbox/" + lines[308].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[308] + color.END)
 url = "https://mailsac.com/inbox/" + lines[309].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[309] + color.END)
 url = "https://mailsac.com/inbox/" + lines[310].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[310] + color.END)
 url = "https://mailsac.com/inbox/" + lines[311].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[311] + color.END)
 url = "https://mailsac.com/inbox/" + lines[312].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[312] + color.END)
 url = "https://mailsac.com/inbox/" + lines[313].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[313] + color.END)
 url = "https://mailsac.com/inbox/" + lines[314].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[314] + color.END)
 url = "https://mailsac.com/inbox/" + lines[315].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[315] + color.END)
 url = "https://mailsac.com/inbox/" + lines[316].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[316] + color.END)
 url = "https://mailsac.com/inbox/" + lines[317].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[317] + color.END)
 url = "https://mailsac.com/inbox/" + lines[318].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[318] + color.END)
 url = "https://mailsac.com/inbox/" + lines[319].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[319] + color.END)
 url = "https://mailsac.com/inbox/" + lines[320].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[320] + color.END)
 url = "https://mailsac.com/inbox/" + lines[321].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[322] + color.END)
 url = "https://mailsac.com/inbox/" + lines[323].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[323] + color.END)
 url = "https://mailsac.com/inbox/" + lines[324].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[324] + color.END)
 url = "https://mailsac.com/inbox/" + lines[325].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[325] + color.END)
 url = "https://mailsac.com/inbox/" + lines[326].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[326] + color.END)
 url = "https://mailsac.com/inbox/" + lines[327].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[327] + color.END)
 url = "https://mailsac.com/inbox/" + lines[328].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[328] + color.END)
 url = "https://mailsac.com/inbox/" + lines[329].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[329] + color.END)
 url = "https://mailsac.com/inbox/" + lines[330].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[330] + color.END)
 url = "https://mailsac.com/inbox/" + lines[331].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[331] + color.END)
 url = "https://mailsac.com/inbox/" + lines[332].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[332] + color.END)
 url = "https://mailsac.com/inbox/" + lines[333].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[333] + color.END)
 url = "https://mailsac.com/inbox/" + lines[334].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[334] + color.END)
 url = "https://mailsac.com/inbox/" + lines[335].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[335] + color.END)
 url = "https://mailsac.com/inbox/" + lines[336].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[336] + color.END)
 url = "https://mailsac.com/inbox/" + lines[337].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[337] + color.END)
 url = "https://mailsac.com/inbox/" + lines[338].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[338] + color.END)
 url = "https://mailsac.com/inbox/" + lines[339].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[339] + color.END)
 url = "https://mailsac.com/inbox/" + lines[340].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[340] + color.END)
 url = "https://mailsac.com/inbox/" + lines[341].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[341] + color.END)
 url = "https://mailsac.com/inbox/" + lines[342].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[342] + color.END)
 url = "https://mailsac.com/inbox/" + lines[343].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[343] + color.END)
 url = "https://mailsac.com/inbox/" + lines[344].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[344] + color.END)
 url = "https://mailsac.com/inbox/" + lines[345].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[345] + color.END)
 url = "https://mailsac.com/inbox/" + lines[346].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[346] + color.END)
 url = "https://mailsac.com/inbox/" + lines[347].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[347] + color.END)
 url = "https://mailsac.com/inbox/" + lines[348].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[348] + color.END)
 url = "https://mailsac.com/inbox/" + lines[349].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[349] + color.END)
 url = "https://mailsac.com/inbox/" + lines[350].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[350] + color.END)
 url = "https://mailsac.com/inbox/" + lines[351].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[351] + color.END)
 url = "https://mailsac.com/inbox/" + lines[352].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[352] + color.END)

 url = "https://mailsac.com/inbox/" + lines[353].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[353] + color.END)
 url = "https://mailsac.com/inbox/" + lines[354].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[354] + color.END)
 url = "https://mailsac.com/inbox/" + lines[355].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[355] + color.END)
 url = "https://mailsac.com/inbox/" + lines[356].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[356] + color.END)
 url = "https://mailsac.com/inbox/" + lines[357].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[357] + color.END)
 url = "https://mailsac.com/inbox/" + lines[358].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[358] + color.END)
 url = "https://mailsac.com/inbox/" + lines[359].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[359] + color.END)
 url = "https://mailsac.com/inbox/" + lines[360].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[360] + color.END)
 url = "https://mailsac.com/inbox/" + lines[361].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[361] + color.END)
 url = "https://mailsac.com/inbox/" + lines[362].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[362] + color.END)
 url = "https://mailsac.com/inbox/" + lines[363].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[363] + color.END)
 url = "https://mailsac.com/inbox/" + lines[364].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[364] + color.END)
 url = "https://mailsac.com/inbox/" + lines[365].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[365] + color.END)
 url = "https://mailsac.com/inbox/" + lines[366].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[366] + color.END)
 url = "https://mailsac.com/inbox/" + lines[367].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[367] + color.END)
 url = "https://mailsac.com/inbox/" + lines[368].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[368] + color.END)
 url = "https://mailsac.com/inbox/" + lines[369].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[369] + color.END)
 url = "https://mailsac.com/inbox/" + lines[370].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[371] + color.END)
 url = "https://mailsac.com/inbox/" + lines[372].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[372] + color.END)
 url = "https://mailsac.com/inbox/" + lines[373].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[373] + color.END)
 url = "https://mailsac.com/inbox/" + lines[374].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[374] + color.END)
 url = "https://mailsac.com/inbox/" + lines[375].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[375] + color.END)
 url = "https://mailsac.com/inbox/" + lines[376].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[376] + color.END)
 url = "https://mailsac.com/inbox/" + lines[377].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[377] + color.END)
 url = "https://mailsac.com/inbox/" + lines[378].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[378] + color.END)
 url = "https://mailsac.com/inbox/" + lines[379].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[379] + color.END)
 url = "https://mailsac.com/inbox/" + lines[380].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[380] + color.END)
 url = "https://mailsac.com/inbox/" + lines[381].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[381] + color.END)
 url = "https://mailsac.com/inbox/" + lines[382].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[382] + color.END)
 url = "https://mailsac.com/inbox/" + lines[383].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[383] + color.END)
 url = "https://mailsac.com/inbox/" + lines[384].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[384] + color.END)
 url = "https://mailsac.com/inbox/" + lines[385].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[385] + color.END)
 url = "https://mailsac.com/inbox/" + lines[386].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[386] + color.END)
 url = "https://mailsac.com/inbox/" + lines[387].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[387] + color.END)
 url = "https://mailsac.com/inbox/" + lines[388].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[388] + color.END)
 url = "https://mailsac.com/inbox/" + lines[389].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[389] + color.END)
 url = "https://mailsac.com/inbox/" + lines[390].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[390] + color.END)
 url = "https://mailsac.com/inbox/" + lines[391].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[391] + color.END)
 url = "https://mailsac.com/inbox/" + lines[392].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[392] + color.END)
 url = "https://mailsac.com/inbox/" + lines[393].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[393] + color.END)
 url = "https://mailsac.com/inbox/" + lines[394].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[394] + color.END)
 url = "https://mailsac.com/inbox/" + lines[395].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[395] + color.END)
 url = "https://mailsac.com/inbox/" + lines[396].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[396] + color.END)
 url = "https://mailsac.com/inbox/" + lines[397].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[397] + color.END)
 url = "https://mailsac.com/inbox/" + lines[398].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[398] + color.END)
 url = "https://mailsac.com/inbox/" + lines[399].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[399] + color.END)
 url = "https://mailsac.com/inbox/" + lines[400].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
  print (color.YELLOW + "SCRAPPING")
  print ('''
           ++++++++++++++++++++++++++++
           400 Checks Completed / 500
           +++++++++++++++++++++++++++	
  ''')
  print ("" + color.END)	
 else:
  print (color.YELLOW + "SCRAPPED" + color.GREEN + lines[400])
  print ('''
	        ++++++++++++++++++++++++++++
			 400 Checks Completed / 500
            ++++++++++++++++++++++++++++	
    ''')
  print ("" + color.END)
   
 url = "https://mailsac.com/inbox/" + lines[401].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[401] + color.END)
 url = "https://mailsac.com/inbox/" + lines[402].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[402] + color.END)
 url = "https://mailsac.com/inbox/" + lines[403].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[403] + color.END)
 url = "https://mailsac.com/inbox/" + lines[404].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[404] + color.END)
 url = "https://mailsac.com/inbox/" + lines[405].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[405] + color.END)
 url = "https://mailsac.com/inbox/" + lines[406].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[406] + color.END)
 url = "https://mailsac.com/inbox/" + lines[407].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[407] + color.END)
 url = "https://mailsac.com/inbox/" + lines[408].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[408] + color.END)
 url = "https://mailsac.com/inbox/" + lines[409].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[409] + color.END)
 url = "https://mailsac.com/inbox/" + lines[410].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[410] + color.END)
 url = "https://mailsac.com/inbox/" + lines[411].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[411] + color.END)
 url = "https://mailsac.com/inbox/" + lines[412].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[412] + color.END)
 url = "https://mailsac.com/inbox/" + lines[413].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[413] + color.END)
 url = "https://mailsac.com/inbox/" + lines[414].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[414] + color.END)
 url = "https://mailsac.com/inbox/" + lines[415].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[415] + color.END)
 url = "https://mailsac.com/inbox/" + lines[416].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[416] + color.END)
 url = "https://mailsac.com/inbox/" + lines[417].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[417] + color.END)
 url = "https://mailsac.com/inbox/" + lines[418].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[418] + color.END)
 url = "https://mailsac.com/inbox/" + lines[419].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[419] + color.END)
 url = "https://mailsac.com/inbox/" + lines[420].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[420] + color.END)
 url = "https://mailsac.com/inbox/" + lines[421].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print(color.RED + "SCRAPPED" + color.GREEN + lines[421] + color.END)	
 url = "https://mailsac.com/inbox/" + lines[422].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[422] + color.END)
 url = "https://mailsac.com/inbox/" + lines[423].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[423] + color.END)
 url = "https://mailsac.com/inbox/" + lines[424].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[424] + color.END)
 url = "https://mailsac.com/inbox/" + lines[425].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[425] + color.END)
 url = "https://mailsac.com/inbox/" + lines[426].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[426] + color.END)
 url = "https://mailsac.com/inbox/" + lines[427].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[427] + color.END)
 url = "https://mailsac.com/inbox/" + lines[428].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[428] + color.END)
 url = "https://mailsac.com/inbox/" + lines[429].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[429] + color.END)
 url = "https://mailsac.com/inbox/" + lines[430].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[430] + color.END)
 url = "https://mailsac.com/inbox/" + lines[431].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[432] + color.END)
 url = "https://mailsac.com/inbox/" + lines[433].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[433] + color.END)
 url = "https://mailsac.com/inbox/" + lines[434].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[434] + color.END)
 url = "https://mailsac.com/inbox/" + lines[435].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[435] + color.END)
 url = "https://mailsac.com/inbox/" + lines[436].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[436] + color.END)
 url = "https://mailsac.com/inbox/" + lines[437].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[437] + color.END)
 url = "https://mailsac.com/inbox/" + lines[438].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[438] + color.END)
 url = "https://mailsac.com/inbox/" + lines[439].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[439] + color.END)
 url = "https://mailsac.com/inbox/" + lines[440].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[440] + color.END)
 url = "https://mailsac.com/inbox/" + lines[441].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[441] + color.END)
 url = "https://mailsac.com/inbox/" + lines[442].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[442] + color.END)
 url = "https://mailsac.com/inbox/" + lines[443].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[443] + color.END)
 url = "https://mailsac.com/inbox/" + lines[444].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[444] + color.END)
 url = "https://mailsac.com/inbox/" + lines[445].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[445] + color.END)
 url = "https://mailsac.com/inbox/" + lines[446].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[446] + color.END)
 url = "https://mailsac.com/inbox/" + lines[447].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[447] + color.END)
 url = "https://mailsac.com/inbox/" + lines[448].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[448] + color.END)
 url = "https://mailsac.com/inbox/" + lines[449].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[449] + color.END)
 url = "https://mailsac.com/inbox/" + lines[450].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[450] + color.END)
 url = "https://mailsac.com/inbox/" + lines[451].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[451] + color.END)
 url = "https://mailsac.com/inbox/" + lines[452].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[452] + color.END)
 url = "https://mailsac.com/inbox/" + lines[453].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[453] + color.END)
 url = "https://mailsac.com/inbox/" + lines[454].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[454] + color.END)
 url = "https://mailsac.com/inbox/" + lines[454].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[454] + color.END)
 url = "https://mailsac.com/inbox/" + lines[455].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[455] + color.END)
 url = "https://mailsac.com/inbox/" + lines[456].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[456] + color.END)
 url = "https://mailsac.com/inbox/" + lines[457].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[457] + color.END)
 url = "https://mailsac.com/inbox/" + lines[458].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[458] + color.END)
 url = "https://mailsac.com/inbox/" + lines[459].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[460] + color.END)
 url = "https://mailsac.com/inbox/" + lines[461].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[461] + color.END)
 url = "https://mailsac.com/inbox/" + lines[462].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[462] + color.END)
 url = "https://mailsac.com/inbox/" + lines[463].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[463] + color.END)
 url = "https://mailsac.com/inbox/" + lines[464].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[464] + color.END)
 url = "https://mailsac.com/inbox/" + lines[465].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[465] + color.END)
 url = "https://mailsac.com/inbox/" + lines[466].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[466] + color.END)
 url = "https://mailsac.com/inbox/" + lines[467].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[467] + color.END)
 url = "https://mailsac.com/inbox/" + lines[468].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[468] + color.END)
 url = "https://mailsac.com/inbox/" + lines[469].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[469] + color.END)
 url = "https://mailsac.com/inbox/" + lines[470].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[470] + color.END)
 url = "https://mailsac.com/inbox/" + lines[471].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[471] + color.END)
 url = "https://mailsac.com/inbox/" + lines[472].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[472] + color.END)
 url = "https://mailsac.com/inbox/" + lines[473].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[473] + color.END)
 url = "https://mailsac.com/inbox/" + lines[474].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[474] + color.END)
 url = "https://mailsac.com/inbox/" + lines[475].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[475] + color.END)
 url = "https://mailsac.com/inbox/" + lines[476].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[476] + color.END)
 url = "https://mailsac.com/inbox/" + lines[477].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[477] + color.END)
 url = "https://mailsac.com/inbox/" + lines[478].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[478] + color.END)
 url = "https://mailsac.com/inbox/" + lines[479].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[479] + color.END)
 url = "https://mailsac.com/inbox/" + lines[480].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[480] + color.END)
 url = "https://mailsac.com/inbox/" + lines[481].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[481] + color.END)
 url = "https://mailsac.com/inbox/" + lines[482].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[482] + color.END)
 url = "https://mailsac.com/inbox/" + lines[483].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[483] + color.END)
 url = "https://mailsac.com/inbox/" + lines[484].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[484] + color.END)
 url = "https://mailsac.com/inbox/" + lines[485].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[485] + color.END)
 url = "https://mailsac.com/inbox/" + lines[486].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[486] + color.END)
 url = "https://mailsac.com/inbox/" + lines[487].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[487] + color.END)
 url = "https://mailsac.com/inbox/" + lines[488].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[488] + color.END)
 url = "https://mailsac.com/inbox/" + lines[489].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[489] + color.END)
 url = "https://mailsac.com/inbox/" + lines[490].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[490] + color.END)
 url = "https://mailsac.com/inbox/" + lines[491].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[491] + color.END)
 url = "https://mailsac.com/inbox/" + lines[492].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[492] + color.END)
 url = "https://mailsac.com/inbox/" + lines[493].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[493] + color.END)
 url = "https://mailsac.com/inbox/" + lines[494].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[494] + color.END)
 url = "https://mailsac.com/inbox/" + lines[495].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[495] + color.END)
 url = "https://mailsac.com/inbox/" + lines[496].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[496] + color.END)
 url = "https://mailsac.com/inbox/" + lines[497].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[498] + color.END)
 url = "https://mailsac.com/inbox/" + lines[499].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[499] + color.END)
 url = "https://mailsac.com/inbox/" + lines[500].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[500] + color.END)
 		
    

def checkersamz() :
 from sys import stdin
 import requests
 import uuid
 import socket
 from urllib.request import urlopen, Request
 class color:
     PURPLE = '\033[95m'
     CYAN = '\033[96m'
     DARKCYAN = '\033[36m'
     BLUE = '\033[94m'
     GREEN = '\033[92m'
     YELLOW = '\033[93m'
     RED = '\033[91m'
     BOLD = '\033[1m'
     UNDERLINE = '\033[4m'
     END = '\033[0m'
 f = open("../downloads/i.txt")
 line = f.readline()
 totalLines = len(f.readlines())
 f.close()
 f = open("../downloads/i.txt")
 lines = f.readlines()
 url = "https://mailsac.com/inbox/" + lines[0].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
   print (color.RED + "SCRAPPING " + color.END)
 else:
   print (color.RED + "SCRAPPED" + color.GREEN + lines[0] + color.END)

 url = "https://mailsac.com/inbox/" + lines[1].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
     print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[1] + color.END)
  
 url = "https://mailsac.com/inbox/" + lines[2].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[2] + color.END)

 url = "https://mailsac.com/inbox/" + lines[3].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[3] + color.END)

 url = "https://mailsac.com/inbox/" + lines[4].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[4] + color.END)


 url = "https://mailsac.com/inbox/" + lines[5].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[5] + color.END)



 url = "https://mailsac.com/inbox/" + lines[6].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[6] + color.END)



 url = "https://mailsac.com/inbox/" + lines[7].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[7] + color.END)



 url = "https://mailsac.com/inbox/" + lines[8].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[8] + color.END)



 url = "https://mailsac.com/inbox/" + lines[9].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[9] + color.END)



 url = "https://mailsac.com/inbox/" + lines[10].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[10] + color.END)



 url = "https://mailsac.com/inbox/" + lines[11].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[11] + color.END)



 url = "https://mailsac.com/inbox/" + lines[12].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[12] + color.END)


 url = "https://mailsac.com/inbox/" + lines[13].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[13] + color.END)



 url = "https://mailsac.com/inbox/" + lines[14].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[14] + color.END)



 url = "https://mailsac.com/inbox/" + lines[15].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[15] + color.END)




 url = "https://mailsac.com/inbox/" + lines[16].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[16] + color.END)



 url = "https://mailsac.com/inbox/" + lines[17].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[17] + color.END)



 url = "https://mailsac.com/inbox/" + lines[18].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[18] + color.END)




 url = "https://mailsac.com/inbox/" + lines[19].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[19] + color.END)



 url = "https://mailsac.com/inbox/" + lines[20].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[20] + color.END)



 url = "https://mailsac.com/inbox/" + lines[21].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[21] + color.END)



 url = "https://mailsac.com/inbox/" + lines[22].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[22] + color.END)



 url = "https://mailsac.com/inbox/" + lines[23].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[23] + color.END)



 url = "https://mailsac.com/inbox/" + lines[24].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[24] + color.END)



 url = "https://mailsac.com/inbox/" + lines[25].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print ('done')