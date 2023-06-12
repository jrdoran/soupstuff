
import os
print("start")
cmd = """osascript<<END
tell application "Mail"
	
	set theFrom to "jimdoran64@gmail.com"
	set theTos to {"jimdoran64@gmail.com"}
	set theCcs to {}
	set theBccs to {}
	
	set theSubject to " python test "
	set theContent to " aa bb cc dd "
	set theSignature to " hi there signature"
	set theAttachments to {}

	
	set theMessage to make new outgoing message with properties {sender:theFrom, subject:theSubject, content:theContent, visible:false}
	tell theMessage
		repeat with theTo in theTos
			make new recipient at end of to recipients with properties {address:theTo}
		end repeat
		repeat with theCc in theCcs
			make new cc recipient at end of cc recipients with properties {address:theCc}
		end repeat
		repeat with theBcc in theBccs
			make new bcc recipient at end of bcc recipients with properties {address:theBcc}
		end repeat
		repeat with theAttachment in theAttachments
			make new attachment with properties {file name:theAttachment as alias} at after last paragraph
			set theDelay to 1
			delay theDelay
		end repeat
	end tell
	
	# macOS 10.12+ know bug
	# https://stackoverflow.com/questions/39860859/setting-message-signature-of-outgoing-message-using-applescript
	# set message signature of theMessage to signature theSignature
	
	send theMessage
	
end tell
END"""

# 	set theDelay to 1
# quit

def send_Message():

    os.system(cmd)

send_Message()
print ("done")

exit()



#import os

#cmd = """osascript<<END

#tell application "Messages"

#send "TEXT from JD" to buddy "18606719963" of (service 1 whose service type is iMessage)

#end tell

#END"""

#def send_Message():

#    os.system(cmd)

#send_Message()








