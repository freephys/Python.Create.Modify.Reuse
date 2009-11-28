import winsound

print "Play Windows exit sound."
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

print "Probably play Windows default sound"
winsound.PlaySound("*", winsound.SND_ALIAS)

print "Play a message beep"
winsound.MessageBeep()

print "Play an evil laugh"
winsound.PlaySound('evil_laugh.wav',winsound.SND_FILENAME)