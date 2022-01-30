# Debug Log

**Explain how you used the the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what useful information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

_Example: I noticed that the program should show pizza orders once a new order is made, and that it wasn't showing any. So, I used the trace forward technique starting on line 13. I discovered the bug on line 27 was caused by a typo of 'pzza' instead of 'pizza'._

_Then I noticed another bug ..._

## Exercise 1
The program runs fine at first and I'm able to go to the orders page where I see a form to create my own pizza order. Once I submit the form, the app crashes and checking the error log from flask, it says that there is an issue with line 80 which is 'pizza.toppings.append(PizzaTopping(topping=topping_str))'. I am using the traceback method to see where these variables originate from to then make sure we're passing the right ones. After making some changes, I then got an error after creating the pizza from line 90 that said 'Could not build url for endpoint '/'.' I then changed it so that it can redirect to home after a pizza is created. I added a print statement to see if it even reached to the part after it adds the pizza to the database. I then checked to see if it was in the database and it wasn't and that's when I realized I was missing a db.session.commit() and now it adds it and displays it but theres an error in the logic of the topics for loop on line 79. I realized that I was trying to grab a list but that there was no array being created initially because we weren't grabbing it from the form the correct way, I changed line 71 'toppings_list = request.form.get('toppings')' to toppings_list = request.form.getlist('toppings') which adds every item checked in that part of the form into an array which I was then able to access in line 81 to then display only the checked toppings.
## Exercise 2
At first, the program runs fine in showing the form that's asking for the city name and the type of unit you want your data back in. Once you submit the form the app crashes and comes back with an error "KeyError: 'name'" The error comes from line 52 ''city': result_json['name']'. I began with the trace forward method from the beginning of the 'results' method. I realized that some of the data we were trying to get from the form wasn't being called correctly so I changed lines 39 and 40 to call their respected names like they are in the actual form in the html. I also added a print statement, to see the JSON result that comes out from the API. I kept getting a server error and after using the trace forward method, I realized that the API url was never using the actual city and unit parameters, so I went back to the API documentation to see the correct url format when passing a city name and metrics as well. I then commented out the context object just to see what I got as a result from the API call and I successfully got the citys weather with the correct unit. However, I was still getting errors within the context object because it was calling indexes from the JSON response the wrong way. I used the trial and error method to access certian indexes until I figured out which ones returned the exact data I was looking for to display on the results page. After I figured out the correct way to access the data, I changed the values in the context object to the correct ones and when I ran the program the correct data was displayed.
## Exercise 3

[[Your answer goes here!]]
