def isPhoneNumber(text):
    if text.startswith("05") and len(text) == 11:       
        for i in range(0,11):
            if not text[i].isdecimal():
                return False
            else:
                return True
     
    elif text.startswith("5") and len(text) == 11:
       
            for i in range(0,10):
                if not text[i].isdecimal():
                    return False
                else:
                    return True
    else:
        return False

message = "Merhabalar benim adım mahmut. bu da telefon numaram 05222788821 ya da bu numaraddan ulaşabilirsiniz 05322323232 teşekkürşer."
foundNumber = False
for i in range(len(message)):
    number = message[i:i+11]
    if(isPhoneNumber(number)):
        print(number)
        
