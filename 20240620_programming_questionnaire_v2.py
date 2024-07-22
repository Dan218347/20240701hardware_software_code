import time

def main():
  name = "daniel.C"
  print("Welcome to the Python learning journey!")
  print()
  print("Hey, do you enjoy coding, " + name + "?")
  answer = input()

  if answer =="no":
    print("oh,to bad then why are you taking this course?")
    answer = input()
    print("oh well thats okey people usally hate what they don't undestand")
    time.sleep(2)
    print("come back when you changed your mind !")

  elif answer == "yes":
    print("nice")
    time.sleep(2)
    print(" OK "+ name + "")
    print("then let get started on codeing some python")

if __name__ == "__main__":
  main()
 
