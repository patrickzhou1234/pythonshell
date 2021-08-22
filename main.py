import os
import os.path
import socket

print("\x1b[37m", "pzrepl's™ shell started!")
while True:
  inp = input(">")
  for i in range(10):
    if str(i) in inp:
      print("\x1b[31m", "Numbers are invalid", "\x1b[37m")
      break

  if "list" in inp:
    if os.path.exists("./"+inp[5:]+"/"):
      print(os.listdir("./"+inp[5:]+"/"))
    else:
      print("\x1b[31m", "This directory does not exist.", "\x1b[37m")

  if "delete " in inp:
    if os.path.exists("./"+inp[7:]):
      os.remove("./"+inp[7:])
      print("\x1b[32m", "Successfully deleted file.", "\x1b[37m")
    else:
      print("\x1b[31m", "This file does not exist.", "\x1b[37m")

  if inp == "clear":
    clear = lambda: os.system("clear")
    clear()

  if "deletefolder " in inp:
    if os.path.exists("./"+inp[13:]):
      os.rmdir("./"+inp[13:])
      print("\x1b[32m", "Successfully deleted folder.", "\x1b[37m")
    else:
      print("\x1b[31m", "This folder does not exist.", "\x1b[37m")

  if inp == "getip":
    print(socket.gethostbyname(socket.gethostname()))

  if "make " in inp:
    if os.path.exists("./"+inp[5:]):
      print("\x1b[31m", "This file already exists.", "\x1b[37m")
    else:
      os.mknod("./"+inp[5:])
      print("\x1b[32m", "Successfully created file.", "\x1b[37m")

  if "makefolder " in inp:
    if os.path.exists("./"+inp[11:]):
      print("\x1b[31m", "This folder already exists.", "\x1b[37m")
    else:
      os.mkdir("./"+inp[11:])
      print("\x1b[32m", "Successfully created folder.", "\x1b[37m")
