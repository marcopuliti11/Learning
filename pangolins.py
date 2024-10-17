knowledge = {"Does it live in the sea": "whale", "Does it eat Ants":"Pangolin","Is it scaly":"Snake"}

def ask_questions():
    found = False
    for item in knowledge:
        print("Answer Y/N")
        response = input(item)
        if (response.upper() == "Y"):
            found = True
            break

    if found:
        print("I thought so")
    else:
        print("I don't know this animal")
        new_animal = input("what animal was it?")
        new_item = input("Tell me a good question to distinguish it")
        knowledge[new_item] = new_animal
        
def play():
    key = input("Think of an animal, then press return")
    ask_questions()

def __main__():
    ok = True
    while(ok):
        play()
        response = input('Play again? Y/N')
        if response.upper() == "N":
            ok = False
        if response.upper() == "Y":
            ok = True

if (__name__) == "__main__":
    __main__()
        
