import pyttsx3

obj=pyttsx3.init()

print(">>>>Welcome To Text to Speech<<<<")
speed=int(input("Enter a Speech Speed (Eg:100-Low,200-Medium,300-High) :"))
valume=int(input("Enter a Speech Valume  (Eg:0.1-Low to 1-High) :"))

def texttospeech():
    sp=input("Enter Text You Want To Speach :")
    obj.setProperty("rate",speed)
    obj.setProperty("volume",valume)
    obj.say("Welcome To Text to Speech")

    print("Your Input In Speech......")
    obj.say(sp)
    obj.runAndWait()

    choice=input("Enter Y for Continue Or Enter N for Exit :").lower()
    if(choice=="y"):
        texttospeech()
    else:
        print("Thank You Come Again...")

    choice = input("Do You Want To Save The Audio File Enter Y for Save Or Enter N for Exit :").lower()
    if (choice == "y"):
        print("Saved")
        obj.save_to_file(sp,"C:\\Users\\Admin\\Desktop\\sam.mp3")
    else:
        print("Thank You Come Again...")
        exit()



texttospeech()