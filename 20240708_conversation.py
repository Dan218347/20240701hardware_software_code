def conversation (name) :
  print ("hi {}" .format (name.capitalize()))
  print ("wlcome to my conversation program!!!")
  print ("glad to have you in hardware & sofware!!!")
  return name
def main():
  name = conversation (input("what is your name?"))
  print("nice talking with {}" .format(name))


if __name__=="__main__":
 main()
