# The Harbor Hearth
### Set sail for deliciousness

<img src="documentation/readmecover.png">

[Deployed website](https://zoten64-the-harbour-hearth-cd54b5ce5a13.herokuapp.com/)

## Table of Contents:

* [Goals and target audience](#goals-and-target-audience)
* [User stories](#user-stories)
* [Epics](#epics)
* [Progress](#progress-documentation)
* [Design](#design)
* [Wireframes](#wireframes)
* [User Manual](#user-manual)
* [Features](#features)
* [Bugs and fixes](#bugs-and-fixes)
* [Technologies and tools](#technologies-and-tools)
* [Database Design](#database-design)
* [Validation and testing](#validation-and-testing)
* [Deployment](#deployment)
* [Credits](#credits)

# Goals and target audience

The goal of this project is to put my knowledge of HTML, CSS, JS, Python, Django and relational databases as well 
as push myself to learn more.

The Harbor Hearth is a fictional bistro nearby a vacation resort located at the west coast of England. They offer online ordering and a digital menu. Clients can
review the bistro and create an account. Though an account is not required for ordering as that may be frustrating for users.

The website also features a blog where the admins can post news, changes and other relevant information. 

As an admin you can create special accounts for employees where they have access to a page with pending orders with the ability to cancel. They also have access to answer questions


# User stories

### Customer

1. As a customer I can view the menu online so I can see what is available to order
    - AC1: There should be an easy way to access the menu online
    - AC2: Prices should be shown alongside items in a clear way
    - AC3: Items should be sorted into categories for easier navigation

    Must have

2. As a customer with dietary restrictions I can easily identify what I can and cannot eat so that I can avoid eating things I shouldn't
    - AC1: Common allergies should be clearly marked on the menu (Lactose, nuts, gluten, eggs)
    - AC2: Vegan items are clearly marked for easier identification
    - AC3: Ingredients should be listed

    Must have

3.  As a customer I can order online so I don't have to wait in line at the counter to do so
    - AC1: The website should have an option to order
    - AC2: The customer should be given a short and easy to remember order number

    Must have

4. As a customer I can choose to have my order be eat-in or take-out to suit my needs
    - AC1: The customer should be able to choose eat-in or take-out

    Must have

5. As an eat-in customer I can choose to have my order brought to my table or to pick it up myself at the counter to better suit my needs
    - AC1: Customers who choose the eat in option should have the option to pick up at the counter or brought to the table
    - AC2: The customer should have to enter their table number

    Must have

6. As a customer I can scan a QR code at my table to be instantly taken to the order page with my table number to make it more convenient to order
    - AC1: QR codes should take the customer to the order page
    - AC2: The table number associated with the QR code should be already filled in at the delivery method page
    - AC3: The customer should be able to change the table number and delivery method in case they change their mind or the number is wrong

    Could have

7. As a new customer I can see reviews so I can get a better idea of the experience at the bistro
    - AC1: A preview of reviews should be displayed on the home page with a link to a full page of all the reviews
    - AC2: Reviews should be able to be filtered

    Should have

8. As a customer I can create an account so I can access more features
    - AC1: Customer should be able to make an account
    - AC2: Customer should have to verify their email

    Must have

9. As a customer with an account I can log in so I can access more features
    - AC1: Customer should be able to log in

    Must have

10. As a logged in customer I can change account details so that I can keep using it:
    - AC1: Customer should be able to change email
    - AC2: A changed email should require verification of the new one
    - AC3: Customer should be able to change password
    - AC4: Customer should be able to change name

    Must have

11. As a logged in customer I can delete my account so that my info is no longer stored in The Harbor Hearths database
    - AC1: Customer should have access to a delete button on their account page
    - AC2: Customer should be informed that the account deletion is permanent
    - AC3: Customer should be prompted to confirm deletion

    Must have

12. As a customer who forgot their password I can request a password reset to be able to regain access to my account
    - AC1: The customer should recieve an email with instructions on how to reset their password
    - AC2: Password reset should be successful

    Should have

13. As a logged in customer I can write a review about my experience at the bistro so others can get a better idea of what it's like
    - AC1: The review should have a star rating (1-5)
    - AC2: The review should have a title and some text content (restructed to 3000 characters or less)
    - AC3: The review should offer the option to add up to 4 images

    Should have

14. As a logged in customer who has written a review I can change it to make it more accurate
    - AC1: Customer should be able to change the title of their review
    - AC2: Customer should be able to change the content of their review
    - AC3: Customer should be able to add/remove images from their review

    Should have

15. As a logged in customer I can earn points from each order so that I can be rewarded for coming back
    - AC1: Customer should be awarded points with each order that are stored in the account
    - AC2: Customer should be able to exchange a number of points for free items

    Won't have

16. As a logged in customer I can access deals to make my order cheaper or more beneficial
    - AC1: Logged in customer should be able to choose a deal when ordering

    Won't have

17. As a logged in customer I can add and delete my payment information for quicker ordering next time
    - AC1: Payment info MUST be stored in a secure and encrypted manner
    - AC2: Payment info should be able to be retrieved and work
    - AC3: Payment info should be able to be added
    - AC4: Payment info should be able to be deleted

    Won't have
    Note: Customers can pay at the counter before leaving until this can be implemented

18. As a customer I can contact the Harbor Hearth using a form on their website so I can have any inquires answered
    - AC1: The form should work 
    - AC2: A confirmation email should be sent to the customer upon submission

    Could have


### Employee

19. As an employee I can view orders made by customers so that I can serve them
    - AC1: Website should have a separate page, accessable only to employees and the owner, where a list of customer orders can be viewed
    - AC2: Orders should expire and be archived after a certain amount of time
    
    Must have

20. As an employee I can cancel inapporpriate orders so that I don't have to serve them
    - AC1: Employee's should be able to view an order and be able to delete it.
    - AC2: Employee should be prompted to confirm the deletion
    - AC3: An email should be sent to the person who ordered explaining why

    Should have

21. As an employee I can see a list of questions and messages submitted by customers through the contact form so that I may assist them
    - AC1: The employee only part of the website should feature a page where employees can answer questions
    - AC2: The answer should be sent to the customer via email

    Could have

### Admin

22. As an administrator I have access to an admin dashboard so I can manage the data on the site
    - AC1: The Django admin dashboard should have all models registered
    - AC2: The administrator should be able to delete and add data
    
    Must have

23. As an administrator I can create employee accounts so I can grant them access to specific features
    - AC1: The Django admin dashboard should have an option called "employee account" when creating/changing an account

    Must have

24. As an administrator I can create formatted blog posts of news and important information so I can keep my customers updated
    - AC1: The administratot creating a blog post should allow the use of HTML formatting

    Should have

25. As an administrator I can easily change the price of items on the menu so that I can keep it up to date
    - AC1: The administrator should be able to change the prices from the admin panel

    Must have

26. As an administrator I can easily add and remove items from the menu
    - AC1: The administrator should be able to add and remove items in the admin panel

    Must have

# Epics

1. Ordering and the home page (Core functionality)
    - Ordering and home page functionality, including the menu.
    - User Story Numbers: 1, 2, 3, 4, 5, 6

2. User accounts
    - Anything related to user accounts, from critical things like account details and small things like deals and points
    - User Story Numbers: 8, 9, 10, 11, 12

3. Employee access
    - Employee dashboard
    - User Story Numbers: 19, 20, 23

4. Admin panel
    - Things only the admin can do
    - User Story Numbers: 22, 25, 26

5. News, reviews and contact
    - Things that can give customers a better idea of the experience at The Harbour Hearth
    - User Story Numbers: 7, 13, 14, 18, 21, 24

# Progress Documentation

Here I will document the progress divided into specific dates. Please note that all workdays may not be documented

<details>
<summary> Progress 23/04/2024 </summary>

**Milestones/epics progress**

<img src="documentation/epics_progress_23_04_2024.png">

**Backlog**

<img src="documentation/backlog_progress_23_04_2024.png">

**Commentary:**

Milestones have been created in github. Some of the user stories were changed, added and deleted because of plan changes. The plans to create a forum like page for questions and answers were switched out in favor of a contact form to have less clutter.
</details>

<details>
<summary> Progress 7/05/2024 </summary>

**Milestones/epics progress**

<img src="documentation/epics_progress_07_05_2024.png">

**Backlog**

<img src="documentation/backlog_progress_07_05_2024.png">

**Commentary:**

Home page has been finished and the menu page has been made. I still need to add most of the links and then work on the employee side of the website as it is different from the admin site
</details>

</details>

<details>
<summary> Progress 10/05/2024 </summary>

**Milestones/epics progress**

<img src="documentation/epics_progress_10_05_2024.png">

**Backlog**

<img src="documentation/backlog_progress_10_05_2024.png">

**Commentary:**
Blog page has been finished and viewing reviews is now possible. Clicking on a review/blog preiew brings you to the full page with the details. Works on both the list pages and the home page. Account authentication has been set up and so has email verification and password reset.
</details>

<details>
<summary> Progress 24/05/2024 </summary>

**Milestones/epics progress**

<img src="documentation/epics_progress_24_05_2024.png">

**Backlog**

<img src="documentation/backlog_progress_24_05_2024.png">

**Commentary:**
A lot has been done since the last update. Users can now order and send contact forms, employees can now view orders and contact forms, change order status, cancel orders, delete cancelled orders and answer contact forms. Reviews still needs to be done and the order page needs javascript functionality added to it and card information needs to be stored and retrieved when needed. A lot of things still needs a bunch of styling. 

Summernote has been added to the admin page for blog posts. 
</details>

<details>
<summary> Progress 26/05/2024 </summary>

**Milestones/epics progress**

<img src="documentation/epics_progress_26_05_2024.png">

**Backlog**

<img src="documentation/backlog_progress_26_05_2024.png">

**Commentary:**
All the user stories have been completed
</details>


# Design

The harbor hearth is an ocean/shore themed bistro and therefor the accent colors of the website are a nice cyan color that contrasts well with both dark and light mode. Specifically I used cyan-400 from tailwindCSS which in hex code is the color #22d3ee. Below is a list of all the main colors in both tailwindCSS classes and hex code:

**Light mode**

- Background: cyan-50 | #ecfeff
- Text: slate-950 | #020617
- Heading text: Black
- Accent: cyan-400 | #22d3ee

**Dark mode**
- Background: gray-950 | #030712
- Text: slate-100 | #f1f5f9
- Heading text: White
- Accent: cyan-400 | #22d3ee

**Font**

- Roboto
- Font awesome for icons

**Logo**

The logo is a free vector file I found online and modified slightly to fit my color scheme. See credits

**Layout**

The header consists of:

- Header with dropdown menu
- logo/order now button on the right side of the header

The Footet consists of:

- Footer with links to social media
- Footer with location and contact information

The homepage layout consists of:
- Carousel items on the home page to get a preview of the reviews and news section
- Menu with toggleable tabs to display either meals, drinks or desserts


The menu page layout consists of:
- A menu with toggleable tabs
- An order now button at the bottom of the page
- Link to contact page

The reviews page consists of:
- Multiple cards spread out over the pages with a preview of the review
- Next and Previous buttons for pagination navigation
- A write review button if you're logged in, otherwise a "log in to write review" button

The contact page consists of:
- Contact form
- Small paragraph of alternative contact methods with links to email and phone number

The blog and news page consists of:
- Multiple cards spread out over the pages with a preview of the post
- Next and Previous buttons for pagination navigation

The employee pages consists of:
- Home page with buttons to the view orders and contact forms pages
- Page to view orders categorized into "not started", "in progress", "finished" and cancelled
- Order details page
- Contact forms page with cards of previews of contact forms categorized into "answered" and "not answered"
- Contact forms detail page with the option to respond to the form if it has not been answered yet

The account page consists of:
- Login page by default
- Sign up page via a link
- Account page where you can change your details and delete your account

# Wireframes

<details>
<summary> home </summary>
<img src="documentation/wireframes/the_harbour_hearth_home.png">
</details>

<details>
<summary> menu </summary>
<img src="documentation/wireframes/the_harbour_hearth_menu.png">
</details>

<details>
<summary> reviews </summary>
<img src="documentation/wireframes/the_harbour_hearth_reviews.png">
<img src="documentation/wireframes/the_harbour_hearth_review_detail.png">
</details>

<details>
<summary> blog </summary>
<img src="documentation/wireframes/the_harbour_hearth_blog.png">
<img src="documentation/wireframes/the_harbour_hearth_blog_detail.png">
</details>

<details>
<summary> menu </summary>
<img src="documentation/wireframes/the_harbour_hearth_contact.png">
</details>

# Features

**Dropdown menu**

The main navigation consist of a dropdown menu with all the pages (excluding the employee only page to keep out visitors).

<img src="documentation/features/features1.png">

**Footer with social media, contact info and location**

<img src="documentation/features/features2.png">

**Menu on the home page and menu page**

The menu features 3 clickable tabs. Meals, Drinks and Desserts

<img src="documentation/features/features3.png">

**Home page Carousels of previews of reviews and news**

<img src="documentation/features/features4.png">


**Order now button**

<img src="documentation/features/features5.png">

**Reviews page**

The website features a reviews page with both paginated reviews and review details. It also features a button for writing your own review if you're logged in. Otherwise it has a button for logging in if you want to write a review

<img src="documentation/features/features6.png">

<img src="documentation/features/features6-2.png">


**Contact form**

The contacts page features a form for contacting the Harbour Hearth team.

<img src="documentation/features/features7.png">

**Blog and news page**

The website features a blog and news page with both paginated reviews and post details. 

<img src="documentation/features/features8.png">

<img src="documentation/features/features8-2.png">

**Sign in page**

<img src="documentation/features/features9.png">

**Sign up page**

<img src="documentation/features/features10.png">

**Account page**

The account page features email confirmation, a link to "my reviews", "change email", "change password" and delete account

<img src="documentation/features/features11.png">

**Delete account**

To delete your account you need to check a box to confirm deletion

<img src="documentation/features/features12.png">

**Order online**

The website features a way to order online. This was originally meant to be more of a "select your items" type of ordering system, but because of a lack of time I opted for a text box for the time being. And well.. in the future as well. The table number field only shows up (and becomes required) once table delivery is choosen.
Upon ordering an email will be sent to the user.
If the user is logged in the email will be filled in automatically

<img src="documentation/features/features13.png">


**Table QR codes**

The user can scan a code on their table to automatically be sent to the order page with their table number. Try it!

<details>
<summary> QR codes </summary>
Table 1

<img src="documentation/qrcodes/table1.png" height=500px width=500px>

Table 2

<img src="documentation/qrcodes/table2.png" height=500px width=500px>

Table 3

<img src="documentation/qrcodes/table3.png" height=500px width=500px>

</details>

**Write Review**

If the user is logged in they can write a review, and only one review. This is to prevent spam

<img src="documentation/features/features14.png">

**Viewing your review**

By going to account and then clicking on "my review" you can see your review

<img src="documentation/features/features17.png"

**Delete Review**

If the user has written a review and wishes to delete it they can

<img src="documentation/features/features15.png">


**Edit review**

The user can edit their review by first going to "my review" and then clicking edit

<img src="documentation/features/features18.png">

**Employee home page**

The employee layout looks different to the user pages. The employee page can be accessed by logging in as an employee and going to [this page](https://zoten64-the-harbour-hearth-cd54b5ce5a13.herokuapp.com/employee/)

<img src="documentation/features/features16.png">

**Employee view orders**

Employees can view orders put into different categories. 

<img src="documentation/features/features20.png">

**Employee change status**

Employees can easilly change status of orders by clicking the dropdown, selecting an option and clicking "change"

<img src="documentation/features/features19.png">

**Employee cancel order**

Employees can cancel orders. Upon cancellation an email will be sent to the person who ordered explaining why. Once an order has been cancelled it can be deleted

<img src="documentation/features/features21.png">

The employee has to enter a cancellation reason

<img src="documentation/features/features22.png">

The order will now show up in the cancelled category

<img src="documentation/features/features23.png">

Email sent to the person who ordered

<img src="documentation/features/features24.png">

When the order is cancelled the employee can delete the order

<img src="documentation/features/features25.png">

<img src="documentation/features/features26.png">

**Employee contact forms**

The employee can view the forms

<img src="documentation/features/features27.png">

**Employee answer form**

Unanswered forms can be answered

<img src="documentation/features/features28.png">

Once the answer is submitted it looks like this

<img src="documentation/features/features29.png">

An email will be sent to the user upon answering

<img src="documentation/features/features30.png">

# Bugs and fixes

| Bug | Fix |
| ------------- | ------------- |
| "Cannot import name Menu from home.models" error after the menu model has been moved | Remove the Menu import in home/views.py and home/urls.py. Remove the home urls from the main urls file |
| Django looks for home index template in the wrong folder | Change views path to home/index.html |
| Template functions displaying as example { % block content % } instead of displaying the actual block content| Remove spaces between {} and % |
| The resource from “http://127.0.0.1:8000/css/style.css” was blocked due to MIME type (“text/html”) mismatch (X-Content-Type-Options: nosniff) | Wrong path specified as CSS stylesheet |
| "relation [model] does not exist" error | Make a new database as the last one stopped working properly and I couldn't figure out why. Not a big deal since it was all placeholder content|
| review model submits duplicate upon page reload | Create an extra check to make sure that the user has not sent a review before creating the object in the database and reload the page |
| Order not placing if the user is logged in | Change the way valid forms are checked. Email validity is only checked if the user is not logged in |
| Orders not showing up if the user places them | explicitly declare the order state as "not started" |

# Technologies and tools

### Languages
- HTML
- CSS
- JavaScript
- Python

### Tools
- Visual Studio Code
- Git
- Github
- Heroku
- Pip

### Pyton Libraries
**Built in:**

- OS
    - Used to make environmental variables and to import them
- Pathlib
    - For dynamic paths. 
- uuid
    - Used on blog and reviews

**3rd Party:**

- Django
    - Backend is built using Django
- django-allauth
    - Used for account handling
- django-appconf
    - dependency
- django-summernote
    - Used for formatted blog posts
- dj-database-url
    - Used to parse the database access url for use within the application
- gunicorn
    - HTTP Server for Heroku deployment
- asgiref
    - Django dependency
- packaging
    - Dependency for gunicorn
- psycopg2
    - Driver to connect to the database 
- sqlparse
    - Django dependency
- typing_extensions
    - Dependency for dj-database-url
- tzdata
    - Django dependency
- bleach
    - summernote dependency
- six
    - bleach dependency
- webencodings
    - bleach dependency
- pylint-django
    - pylint plugin
- pylint
    - PEP8 validation tool
- pylint-plugin-utils
    - pylint-django dependency
- astroid
    - pylint dependency
- colorama
    - pylint dependency
- dill
    - pylint dependency
- isort
    - pylint dependency
- mccabe
    - pylint dependency
- platformdirs
    - pylint dependency
- platformdirs
    - pylint dependency
- tomlkit
    - pylint dependency
- pytailwindcss
    - Used to compress TailwindCSS and remove unused classes for better performance

**Note:**

pipdeptree was used to get a better look at the relationship between libraries and therefor not used in the code itself

### Frontend libraries

- Tailwind
    - Used to quickly build the UI
- Flowbite
    - Open source components


# Database design
<img src="documentation/database diagram.png">

**Models**

Format: [name] [type]

Review 

- rating int

- title charfield

- author oneToOneField

- content text

- url uuid

- approved boolean

- featured boolean


Users
- id autofield [primary key]

- email email 

- first_name charfield

- last_name charfield

- username charfield

- password encrypted

- active bool

- staff bool

- superuser bool

- date_joined dateTime

- last_login dateTime


Order
- user foreignKey

- email email

- order_number autofield

- delivery_method choicefield

- table_number int

- order charfield

- state choiceField

- date dateField

- cancel_reason charfield


Employee
- user oneToOneField


Menu
- category choiceField

- name charfield

- description charfied

- ingridients charfield

- price float

- vegan bool

- nuts bool

- gluten bool

- eggs bool


Contact 

- name charfield

- email email

- phone_number charfield

- preferred_contact choicefield

- message charfield

- date datetime

- answered bool

- employee_response charfield

- employee foreignKey


Post

- title charfield

- content charfield

- date datetime

- url uuid

- update_date datetime

- home_page bool


# Validation and testing

## HTML (W3C Validator)
<details>
<summary> Home </summary>
<img src="documentation/html_validation/home.png">
</details>

<details>
<summary> Menu </summary>
<img src="documentation/html_validation/menu.png">
</details>

<details>
<summary> Reviews </summary>
<img src="documentation/html_validation/reviews.png">
<img src="documentation/html_validation/review_details.png">
</details>

<details>
<summary> Contact </summary>
<img src="documentation/html_validation/contact.png">
</details>

<details>
<summary> Blog </summary>
<img src="documentation/html_validation/blog.png">
<img src="documentation/html_validation/blog_details.png">
</details>

<details>
<summary> Log in </summary>
<img src="documentation/html_validation/login.png">
</details>

## CSS Jigsaw Validator

<details>
<summary> CSS Jigsaw </summary>
<img src="documentation/css_validation.png">
</details>

## JSHint

<details>
<summary> JSHint </summary>
<img src="documentation/javascript_validation.png">
</details>

## WAVE Accessibility

<details>
<summary> Home </summary>
<img src="documentation/wave_accessibility/home.png">
</details>

<details>
<summary> Home </summary>
<img src="documentation/wave_accessibility/menu.png">
</details>


<details>
<summary> Reviews </summary>
<img src="documentation/wave_accessibility/reviews.png">
<img src="documentation/wave_accessibility/review_details.png">
</details>

<details>
<summary> Contact </summary>
<img src="documentation/wave_accessibility/contact.png">
</details>

<details>
<summary> Contact </summary>
<img src="documentation/wave_accessibility/contact.png">
</details>

<details>
<summary> Blog </summary>
<img src="documentation/wave_accessibility/blog.png">
<img src="documentation/wave_accessibility/blog_details.png">
</details>

<details>
<summary> Log In </summary>
<img src="documentation/wave_accessibility/sign_in.png">
</details>

## Lighthouse

<details>
<summary> Home </summary>
<img src="documentation/lighthouse/home.png">
Note: I've done as much as I can to try and optimize the home page further, but it comes down to using flowbite with django which makes me unable to compress it in the way I would be able to with Node.JS, and that is on me for not realising earlier
</details>

<details>
<summary> Menu </summary>
<img src="documentation/lighthouse/menu.png">
Note: Performance suffers slightly for the same reason above
</details>

<details>
<summary> Reviews </summary>
<img src="documentation/lighthouse/reviews.png">
<img src="documentation/lighthouse/review_details.png">
</details>

<details>
<summary> Contact </summary>
<img src="documentation/lighthouse/contact.png">
</details>

<details>
<summary> Blog </summary>
<img src="documentation/lighthouse/blog.png">
<img src="documentation/lighthouse/blog_details.png">
</details>

<details>
<summary> login </summary>
<img src="documentation/lighthouse/login.png">
</details>

## PEP8

Pylint-django has been used here to easily validate directories
Django was not configured messages aren't important as it has not bearing on the project. This arises from pylint-django wanting to check foreign key relationships
User model imported from django messages aren't important either

<details>
<summary> home </summary>
<img src="documentation/pep8/home.png">
</details>

<details>
<summary> menu </summary>
<img src="documentation/pep8/menu.png">
</details>

<details>
<summary> order </summary>
<img src="documentation/pep8/order.png">
</details>

<details>
<summary> review </summary>
<img src="documentation/pep8/review.png">
</details>

<details>
<summary> blog </summary>
<img src="documentation/pep8/blog.png">
</details>

<details>
<summary> contact </summary>
<img src="documentation/pep8/contact.png">
</details>

<details>
<summary> contact </summary>
<img src="documentation/pep8/employee_page.png">
</details>


## Manual testing

Due to lack of time I did not have time to implement automatic testing

1. As a customer I can view the menu online so I can see what is available to order

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| A menu on the home page and menu page | Navigate to the home page or the menu page | Be able to view the menu | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory1.png">
</details>

2. As a customer with dietary restrictions I can easily identify what I can and cannot eat so that I can avoid eating things I shouldn't

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Clear color coded labels on the menu | Navigate to the menu and look at the item | Clear dietary restriction labels | works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory2.png">
</details>

3. As a customer I can order online so I don't have to wait in line at the counter to do so

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Order online feature | Navigate to home page and click the order now button in the top right. Fill in the fields and press order | Order should be placed | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory3.png">
</details>

4. As a customer I can choose to have my order be eat-in or take-out to suit my needs

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Delivery method selection | Navigate to the order page (like listed in user story 3) and select the delivery option | Delivery option will be selected | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory4.png">
</details>


5. As an eat-in customer I can choose to have my order brought to my table or to pick it up myself at the counter to better suit my needs

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Delivery method selection | Navigate to the order page (like listed in user story 3) and select the delivery option | Delivery option will be selected | Works as expected |
<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory4.png">
</details>

6. As a customer I can scan a QR code at my table to be instantly taken to the order page with my table number to make it more convenient to order

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| scannable qr codes that will automatically fill in the table number | Scan the qr code with your phone | Table number will be filled in | Works as expected |

Note: I can't show the process of scanning the code, but code for table 1 has been provided below
<details>
<summary>Screenshots</summary>
<img src="documentation/qrcodes/table1.png">
</details>

7. As a new customer I can see reviews so I can get a better idea of the experience at the bistro

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Reviews page | Navigate to reviews | A page with reviews | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory7.png">
</details>

8. As a customer I can create an account so I can access more features

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Account signup page | Navigate to account and press "sign up" | A signup page | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory8.png">
</details>

9. As a customer with an account I can log in so I can access more features

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Account sign in page | Navigate to account page | A sign in page | Works as expected |
<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory9.png">
</details>

10. As a logged in customer I can change account details so that I can keep using it:

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Account settings pages | Make sure you're logged in. Navigate to account page and look at the bottom| Links to change account details | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory10.png">
</details>

11. As a logged in customer I can delete my account so that my info is no longer stored in The Harbor Hearths database

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Delete account feature | Navigate to account, look at the bottom and click delete account. Follow the instructions | account deletion | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory11.png">
</details>

12. As a customer who forgot their password I can request a password reset to be able to regain access to my account

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Password reset feature | Navigate to account page, press "forgot password", follow the instructions | Password reset page | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory12.png">
</details>

13. As a logged in customer I can write a review about my experience at the bistro so others can get a better idea of what it's like

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Write review functionality | Navigate to the reviews page, click write a review (or log in if you aren't), fill in the fields and press submit | Being able to write review | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory13.png">
</details>

14. As a logged in customer who has written a review I can change it to make it more accurate

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Edit review functionality | navigate to account, log in if you have to, click "my review" and press edit | Ability to edit review | works as expected|

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory14.png">
</details>


15. As a customer I can contact the Harbor Hearth using a form on their website so I can have any inquires answered

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Contact form | Navigate to "contact" and  fill out the form | Contact form you can fill out | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory15.png">
</details>

16. As an employee I can view orders made by customers so that I can serve them

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| View orders page | Be logged in as an employee and navigate to the employee page by appending "/employee" to the end of the home url. Click orders | A page where you can view orders | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory16.png">
</details>

17. As an employee I can cancel inapporpriate orders so that I don't have to serve them

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Cancel orders feature | Navigate to orders page by following number 16. Click on the order you want to cancel. Press cancel and enter a reason. | The order will cancel | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory17.png">
</details>

18. As an employee I can see a list of questions and messages submitted by customers through the contact form so that I may assist them

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Contact forms employee view | Be logged in as an employee and navigate to the employee page by appending "/employee" to the end of the home url. Click "Contact Forms" | A page with contact forms | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory18.png">
</details>


19. As an administrator I have access to an admin dashboard so I can manage the data on the site

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Admin panel | Navigate to the admin panel by appending /admin to the end of the home url. Log in if prompted | Admin panel | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory19.png">
</details>

20. As an administrator I can create employee accounts so I can grant them access to specific features

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Employee accounts feature | Navigate to admin panel by following number 19. Press new on the "employees" row. Choose the user you want to make an employee and press save | A user account will be promoted to employee | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory20.png">
</details>

21. As an administrator I can create formatted blog posts of news and important information so I can keep my customers updated

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Create Blog posts function in the admin panel | Navigate to the admin panel by following number 19. Press new on thew "posts" row. Fill out the fields.| Page for making blogposts featuring summernote as a more advanced text editor | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory21.png">
</details>

22. As an administrator I can easily change the price of items on the menu so that I can keep it up to date

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Change menu items | Navigate to admin panel. Click menus. Click the item that you want to change and change the price | The price will be changed | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory22.png">
</details>

23. As an administrator I can easily add and remove items from the menu

| Feature  | Action | Expected results | Actual results |
| ------------- | ------------- | ------------- | ------------- |
| Modify menu | Navigate to the admin panel. Either press the plus button next to menu to add an item, or click the menu text iself, click the item to be deleted and press delete| Add and/or delete items | Works as expected |

<details>
<summary>Screenshots</summary>
<img src="documentation/testing_screenshots/userstory23.png">
</details>

## More testing

**Browsers tested**
- Google Chrome (Theoretically all chromium browsers should work)
- Firefox

**Devices tested**

The website has been tested on the following devices:
- Custom built desktop pc
- Nothing Phone 2

# Deployment

**Deploying and accessing the website**

Prerequisities:
- Have a Heroku account with billing information
- Having a project to deploy pushed to github

Steps:

Creating the app:


- From the dashboard (First page after logging in), click "new" button on the top right
- Click "Create new app"

<details>
<summary>Screenshots</summary>
<img src="documentation/heroku_deploy/step1.png" width="1000">
</details>

<br>

- Give it a name and a region (I chose Europe as I am in Europe)
- Click "Create App"

<details>
<summary>Screenshots</summary>
<img src="documentation/heroku_deploy/step2.png" width="1000">
</details>

<br>

- You will be taken to the "Deploy" tab in your project. From there, under "Deployment method", click "Github".

<details>
<summary>Screenshots</summary>
<img src="documentation/heroku_deploy/step3.png" width="1000">
</details>

<br>

- Enter the name of your repository and click "search"
- Click "connect" besides the repository you want to deploy

<details>
<summary>Screenshots</summary>
<img src="documentation/heroku_deploy/step4.png" width="1000">
</details>

<br>

- Now go to settings and scroll down to "buildpacks"
- Click "Add buildpacks"
- Select the buildpack you want to use. I will use Node.js
- You can now see what buildpacks are installed

<details>
<summary>Screenshots</summary>
<img src="documentation/heroku_deploy/step5.png" width="1000">
<img src="documentation/heroku_deploy/step6.png" width="1000">
</details>

<br>

(Optional) If you have any environment variables that needs to be added, such as credentials, you'll do that here:


- Scroll up slightly and click "Reveal config vars"
- There should be two fields, one with the placeholder "Key" and one with "Value"
- Enter your variable name and the value of that variable
- Click "Add"
- You should now see the variable in the list.

<details>
<summary>Screenshots</summary>
<img src="documentation/heroku_deploy/optional_env_var.png" width="1000">
</details>

<br>

Deploying: 

- At the very bottom, click "Deploy Branch"
- Wait for the project to be built
- When done a button at the bottom with the text "view" should appear

<details>
<summary>Screenshots</summary>
<img src="documentation/heroku_deploy/step7.png" width="1000">
</details>

<br>

To access your app at any time, there's a button on the top of the same page called "open app"

<details>
<summary>Screenshots</summary>
<img src="documentation/heroku_deploy/step8.png" width="1000">
</details>

<br>


**How to fork the project**

- Navigate to the github repository (You're probably here already)
- In the right corner click fork and choose a name

**How to clone the project**

Prerequisities:

- Have git downloaded and configured

steps:

- Go to the repository (You're probably here already)
- Click the code button
- Copy the url
- Open git and change the directory to the parent directory that you want the project to clone to
- Write "git clone [the link you just copied]", in this case "git clone https://github.com/Zoten64/The-Harbor-Hearth.git"

# Credits

**Code**

- [Codestar walkthrough project has been referenced in a lot of places](https://github.com/Code-Institute-Solutions/blog/tree/main/15_testing)
- [Love running project for social media link help](https://github.com/Code-Institute-Solutions/love-running-v3/blob/main/8.1-testing-and-validation/index.html)
- [Django documentation](https://docs.djangoproject.com/en/5.0/)
- [Tailwind documentation](https://tailwindcss.com/docs/installation)
- [Flowbite dropdown menu](https://flowbite.com/docs/components/dropdowns/)
- [Flowbite tabs menu](https://flowbite.com/docs/components/tabs/)
- [Flowbite carousel for reviews and news section](https://flowbite.com/docs/components/carousel/)
- [Success message after post](https://stackoverflow.com/questions/28723266/django-display-message-after-post-form-submit)
- [Login always throwing "wrong password or email" error issue fix](https://stackoverflow.com/questions/27967319/django-allauth-email-login-always-wrong)
- [Django summernote implementation tutorial](https://github.com/summernote/django-summernote)
- Various snippets from other personal projects to speed up the process

**Assets**

- [Logo, modified in inkscape](https://www.freepik.com/free-vector/hand-drawn-beach-logo-template_26252522.htm#query=ocean%20logo&position=16&from_view=keyword&track=ais_user&uuid=7f17a4dc-ae89-4548-95a0-02b50afd77e2)
- [Hero Image by StockSnap at StockVault](https://www.stockvault.net/photo/190026/dock#)

**Inspiration**

- [Landing page UI inspiration](https://www.behance.net/gallery/196798485/Restaurant-landing-page-UI-design?tracking_source=search_projects|restaurant+ui&l=37)