from py_postmates import postmates as pm

from colorama import init
from colorama import Fore

import os
import sys

init()

def main(API_KEY, CUSTOMER_ID):

    postmate = pm.PostmatesAPI(API_KEY, CUSTOMER_ID)

    delivery = order(postmate)

    interact = True

    while(interact):

        command = raw_input("Status, Cancel, Done: ")

        if(command == "Status"): #check what button the user presses
            delivery.update_status()
            get_status(delivery)

        elif(command == "Cancel"):
            if(delivery.status != "pending"):
                delivery.cancel()
            else:
                print "Can only cancel deliveries not yet picked up."
                print "The current status is: " + get_status(delivery)
            interact = False

        elif(command == "Done"):
            interact = False

        else:
            print "Ya dun messed up. Put in a real command pls."

def get_status(delivery):
    if(delivery.status == "pending"):
        print "Processing the request."
    elif(delivery.status == "pickup"):
        print "Picked up the food."
    elif(delivery.status == "dropoff"):
        print "Dropped off the food."
    elif(delivery.status == "delivered"):
        print "Delivery is complete."
    else:
        print "Something is wrong PLS FIX STATUS"

def order(postmate):

    #pickup =  Get the location from Saketh's part.
    pickup = "77 Massachusetts Ave, Cambridge, MA 02139"

    #dropoff = Get array with name, address, number from Katyayni's part
    end = ["Bob", "Massachusetts Hall Cambridge, MA 02138", "415-777-9999"]    

    # This info should come in via parameters from the form on the website
    name = raw_input("Please enter your company's name: ")
    number = raw_input("Please enter your Phone number (i.e. 123-456-7890): ")
    manifest = raw_input("Please enter what you will be i (i.e. 50 bagels): ")

    pickup = pm.Location(name, pickup, number)

    dropoff = pm.Location(end[0], end[1], end[2])

    delivery = pm.Delivery(postmate, manifest, pickup, dropoff)
    delivery.create()

    return delivery


if __name__ == '__main__':

    try:
        os.environ["POSTMATES_KEY"] = "a254dd7a-a9ba-4e30-9adf-7e72781caba3" #TAKE OUT
        API_KEY = os.environ["POSTMATES_KEY"]
    except KeyError:
        print(Fore.RED + "Please set the Postmates API Key to the environment variable POSTMATES_KEY" + Fore.RESET)
        sys.exit(1)

    try:
        os.environ["POSTMATES_ID"] = "cus_KUqGApvB2kLJsF" #TAKE OUT
        CUSTOMER_ID = os.environ["POSTMATES_ID"]
    except KeyError:
        print(Fore.RED + "Please set the Postmates Customer ID environment variable POSTMATES_ID" + Fore.RESET)
        sys.exit(1)

    main(API_KEY, CUSTOMER_ID)
    #main(API_KEY, CUSTOMER_ID, sys.argv[1], sys.argv[2]) # argv[1] is name, argv[2] is phone number