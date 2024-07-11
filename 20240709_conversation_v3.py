def conversation (name) :
    print("hi {}" .format(name.capitalize()))
    print("welcome to my conversation programm!!!")
    print("glad to have you in hardware & software!!!")
    return name

def question(name) :
    print("we want to know if you like programming!")
    answer = input ("(), do you like programming!" .format(name.capitalize()))
    return name

def check_response(response) :
    if response.lower() == "yea":
        print("great! you said {}". format(response))
    else:
        print("sorry to hear that")
def main() :
    name = conversation(input("what is your name?"))
    your_answer =  queston(name)
    check_resonse(your_answer)
    print("nice talking with you {}".format(name)

    if __name__ == "__main__":
      main()
