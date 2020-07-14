import tkinter as tk
from random import choice
from json import dumps

details = dict()

#################################################
##Please enter in the API key provided by James##
#################################################
key = 'Enter Api code here must be a string'

#######random names list
names = [
    "Gerald",
    "Bobby",
    "James",
    "Steven",
    "Graham",
    "Amelia",
    "Grace",
    "Thomas",
    "Reuben"
    ]


#events

def submit(event):
    global details

    #making dictionary for customer details
    details = {
        "forname": ent_forname.get(),
        "surname": ent_surname.get(),
        "postcodeStart": ent_postcodeStart.get(),
        "street": ent_streetName.get(),
        "number": ent_number.get(),
        "destPostcode": ent_destPostcode.get(),
        #"numberOfPassengers": ent_numberOfPassangers.get(),
        "telNumber": ent_telNumber.get()
        }

    #checking expected intagers are intagers
    try:
        int(details["number"])
        #int(details["numberOfPassangers"]) ###some reason tkinters .get function playing up cant be bothered debugging yet
    except ValueError:
        makeError("Please ensure all data entered is correct")
        return

    #ensurring phone number is valid
    try:
        int(details["telNumber"])
    except ValueError:
        makeError("please enter a valid UK mobile phone number")
        return

    if len(details["telNumber"]) != 12:
        makeError("please enter a valid UK mobile phone number")

    else:
    ###sending text
        message = clockwork.SMS(to = str(details["telNumber"]), message = "{} will pcik you up in 20 minutes from {} {}".format(choice(names), details["number"], details["street"]), from_name="Jamz Cabz")
        response = api.send(message)


    output = dumps(details)

    file = open("orders.json", 'w')
    file.write(output)
    file.close()

    #exit()
    


#proceures to make error windows
def makeFatalError(errorType):
    def exitFatalError(event):
        error.destroy()
        exit()



    error = tk.Tk()
    error.title("Error")
    
    lbl_error = tk.Label(text=errorType, width=100, height=20)
    btn_error = tk.Button(text="Ok", height=2, width=5)

    lbl_error.pack()
    btn_error.pack()

    btn_error.bind("<Button-1>", exitFatalError)

    error.mainloop()


def exitError(event):
            error.destroy()
def makeError(errorType):

        

    error = tk.Tk()
    error.title("Error")

    lbl_error = tk.Label(text=errorType, width=100, height=20)
    btn_error = tk.Button(text="Ok", height=2, width=5)

    lbl_error.pack()
    btn_error.pack()

    btn_error.bind("<Button-1>", exitError)

    error.mainloop()
    


#import clockwork and test for install
try:
    from clockwork import clockwork
except:
    #error window
    makeFatalError("Error encountered. Python module clockwork is not installed. Please try pip install clockwork")
    

api = clockwork.API(key)

#creating window
window = tk.Tk()
window.title("Jamz Cabz")


space = tk.Label(text="", height=3, width=100)

###defining elements
#start
lbl_forname = tk.Label(text="Forname:")
lbl_surname = tk.Label(text="Surname:")
lbl_postcodeStart = tk.Label(text="Postcode:")
lbl_streetName = tk.Label(text="Street name:")
lbl_number = tk.Label(text="Building number:")

ent_forname = tk.Entry()
ent_surname = tk.Entry()
ent_postcodeStart = tk.Entry()
ent_streetName = tk.Entry()
ent_number = tk.Entry()

#ride info
lbl_destPostcode = tk.Label(text="Destination (Postcode):")
lbl_numberOfPassangers = tk.Label(text="Number of passangers:")
lbl_telNumber = tk.Label(text="Phone number (no spaces and in international format without +):")

ent_destPostcode = tk.Entry()
ent_numberOfPassangers = tk.Entry()
ent_telNumber = tk.Entry()

##submit button
btn_confirm = tk.Button(text="confirm")

###Rendering Elements
lbl_forname.pack()
ent_forname.pack()
lbl_surname.pack()
ent_surname.pack()
lbl_postcodeStart.pack()
ent_postcodeStart.pack()
lbl_streetName.pack()
ent_streetName.pack()
lbl_number.pack()
ent_number.pack()
space.pack()
lbl_destPostcode.pack()
ent_destPostcode.pack()
lbl_numberOfPassangers.pack()
ent_numberOfPassangers.pack()
lbl_telNumber.pack()
ent_telNumber.pack()
btn_confirm.pack()

##button handeling
btn_confirm.bind("<Button-1>", submit)






window.mainloop()
