import time
import pyttsx3

i = 0
history = []
engine = pyttsx3.init()
while True:  
    f = open('testfile.txt','r')
    buf = f.read()
    if buf not in history:
        history.append(str(buf))
        if buf == 'person':
            engine.say("I see motherfucker")
            engine.runAndWait() 
        else:
            engine.say("I see" + buf)
            engine.runAndWait()            
    i += 1
    print(str(len(history)))
    if i>2:
        history.clear()
        i = 0
        

