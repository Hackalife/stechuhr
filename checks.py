#!/usr/bin/python3
import datetime

nameOfLogFile = "daylogs.txt"
utcTime = True
timeFormat = ""
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
        theTime = datetime.datetime.now()
      if timeFormat:
        timeStamp = theTime.strftime ( timeFormat )
      else:
        timeStamp = "%sZ" % theTime.replace ( microsecond = 0 ).isoformat()
      logFile.write ( ( "[%s] %s\n" ) % ( timeStamp, newEntry ) )
except:
  print ( "Cannot open %s" % nameOfLogFile )
