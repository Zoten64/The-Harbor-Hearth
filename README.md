# The Harbor Hearth
### Set sail for sweetness

## Table of Contents:

* [Goals and target audience](#goals-and-target-audience)
* [User stories](#user-stories)
* [Design](#design)
* [Wireframes](#wireframes)
* [User Manual](#user-manual)
* [Features](#features)
* [Bugs and fixes](#bugs-and-fixes)
* [Technologies and tools](#technologies-and-tools)
* [Technical Design](#technical-design)
* [Validation and testing](#validation-and-testing)
* [Deployment](#deployment)
* [Credits](#credits)

# Goals and target audience

The goal of this project is to put my knowledge of HTML, CSS, JS, Python, Django and relational databases as well 
as push myself to learn more.

The Harbor Hearth is a fictional bistro nearby a vacation resort located at the west coast of England. They offer online ordering and a digital menu. Clients can
review the bakery, create an account to be recieve loyalty points with every order that can be exchanged for goods. Making an account will also let you take part of deals
and save your payment information for faster ordering. Though an account is not required for ordering as that may be frustrating for users.

The website also features a blog where the admins can post news, changes and other relevant information. Customers may comment and ask questions.

As an admin you can create special accounts for employees where they have access to a page with pending orders with the ability to cancel. They also have access to answer and approve questions as well as delete inappropriate ones. 


# User stories

## Customer

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

3.  As a customer I can order and pay online so I don't have to wait in line at the counter to do so
    - AC1: The website should have an option to order
    - AC2: The customer should be able to add listed items to the order
    - AC3: The customer should be able to pay directly on the website
    - AC4: The customer should be given a short and easy to remember order number

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

    Should have

16. As a logged in customer I can access deals to make my order cheaper or more beneficial
    - AC1: Logged in customer should be able to choose a deal when ordering

    Should have

17. As a logged in customer I can add delete my payment information for quicker ordering next time
    - AC1: Payment info MUST be stored in a secure and encrypted manner
    - AC2: Payment info should be able to be retrieved and work
    - AC3: Payment info should be able to be added
    - AC4: Payment info should be able to be deleted

    Should have

18. As a logged in customer I can ask a question so that an employee can answer it
    - AC1: Customer should be able to ask a question on a dedicated page
    - AC2: Customer should be notified when theyr question has been approved

19. As a customer I can look at previously asked questions so I can see if my question has been answered before:
    - AC1: Customer should be able to visit a page with questions and answers
    - AC2: Customer should be able to search for a question

 