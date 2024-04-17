import os

if os.path.exists("log.txt"):
    with open("log.txt", "w") as log_file:
        log_file.write("Everything done!!")

else:
    with open("log.txt", "a") as log_file:
        log_file.write("You need to start the program once again!")