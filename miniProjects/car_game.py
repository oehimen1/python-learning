response = ""
started = False

while True:
    response = input().lower()
    if response == "help":
        print(''' 
start - to star the car
stop - to stop the car
quit - to exit''')
    elif response == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...Ready to go!")
    elif response == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped.")
    elif response == "quit":
        break
    else:
        print("I dont understand that...")
