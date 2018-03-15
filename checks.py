from datetime import datetime

with open('daylogs.txt',mode='r') as logs:
    levent = logs.readline()
pass

timedate = "[" + datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z]"


def dialog():
    print("Log your events \n","last event: \n")
    print(levent)
pass

def addevent():

    with open('daylogs.txt') as logdata:
        data = logdata.read()


    logfile = open("daylogs.txt","w")
    finlog = ("%s %s")%(timedate, name)
    logfile.write(str(finlog))
    logfile.write('\n')
    logfile.write(data)
    logfile.close()

pass

dialog()

name = input("eventname ?")


if name =="j":
    name ="joylent gegessen"
    pass




addevent()
