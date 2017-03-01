# Food Philanthropy

According to the *National Geographic*, about 30% of the food we grow is wasted every year. However, with constant advent of new technology, newfound advances and innovations have begun to offer solutions.

This project utilizes the Google and Postmates APIs in conjunction to provide stores an easy manner in which food and other goods can be given to those in need. 

Google Maps API gives us the current location of the restaurant and gives the location information about the closes food pantries.

Postmates API allows us to request a driver to deliver based on the locations received from Google.

##Work In Progress

###To execute source code: 

1. Run python -m SimpleHTTPServer within the folder of these files. 
2. Navigate to http://localhost:8000/index.html
3. You will land on our home page from where you can sign up or sign into a portal. 
	a. You can also access our 'About' page from clicking on the 'Click here to learn more' section of our landing page.
4. To sign into the restaurant manager portal, simply click the 'Login' button. 
	a. Within the restaurant manager view, once you click 'Submit', you will see you order being processed in the top right corner 
	   of the navigation bar. Once it is confirmed by the food pantry, you will see a notification as well as a tab for confirmed orders.
5. To access the food pantry manager portal, click specifically on the image of the lock. 
	a. Within the food pantry view, you can click to accept or deny any of the requested orders. 
6. Within either view, you can access an edit profile tab from the navigation bar. 

