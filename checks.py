#!/usr/bin/python3
import datetime

nameOfLogFile = "daylogs.txt"
utcTime = True
timeFormat = "%Y-%m-%d_%H:%M:%SZ%z"
shortcuts = {
  "j": "joylent gegessen",
}

try:
  with open ( nameOfLogFile, mode="a+" ) as logFile:
    logFile.seek ( 0 )
    oldLogs = logFile.readlines()
    print ( "Log your events")
    if oldLogs:
      print ( " last event:\n", oldLogs [ -1 ])
    newEntry = input("add new event: ")
    newEntry = shortcuts.get ( newEntry, newEntry )
    print( "event: »%s«" % newEntry )
    if newEntry:
      if utcTime:
        theTime = datetime.datetime.utcnow()
      else:
        utcOffset = round((datetime.datetime.now()-datetime.datetime.utcnow()).seconds / 60 )
        timeZone = datetime.timezone(datetime.timedelta(0, 60 * utcOffset))
        theTime = datetime.datetime.now().replace(tzinfo=timeZone)
      timeStamp = theTime.strftime ( timeFormat )
      logFile.write ( ( "[%s] %s\n" ) % ( timeStamp, newEntry ) )
except:
  print ( "Cannot open %s" % nameOfLogFile )
