#file handleing

def create():
  print('Selcect file to write')
  file1 = input()
  f1 = open(file1, "x")
  print('pase your code here')
  code = input()
  f1.write(code)
  f1.close()


def write():
  print('what is the name of the file')
  file2 = input()
  f2 = open(file2, "a")
  print('paste code here')
  code1 = input()
  f2.write(code1)
  f2.close()

# new line function
def newLine():

  code = input()
  if code == ".write":
    write()
  elif code == ".create":
    create()
  else:
    newLine()



print('welcome to the editor,')
newLine()
