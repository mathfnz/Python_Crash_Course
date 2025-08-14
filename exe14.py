# %%

message = ""
active = True
while active:
    message = input("Say something or quit to stop: ")
    quit = "quit"
    if message == quit:
        active = False
    else:
        print(message)