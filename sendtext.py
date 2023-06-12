import os

cmd = """osascript<<END

tell application "Messages"

send "TEXT from JD" to buddy "18606719963" of (service 1 whose service type is iMessage)

end tell

END"""

def send_Message():

    os.system(cmd)

send_Message()
print ("jd finished")

