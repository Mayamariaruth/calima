# Testing 

## Table of Contents:
1. [**Manual testing**](#manual-testing)
    * [***User stories***](#user-stories)
1. [**Validator testing**](#validator-testing)
1. [**Lighthouse testing**](#lighthouse-testing)
    * [***Landing page***](#landing-page)
    * [***Menu***](#menu)
    * [***Booking form***](#booking-form)
    * [***Booking success***](#booking-success)
    * [***Profile***](#profile)
    * [***Edit account details***](#edit-account-details)
    * [***Delete account***](#delete-account)
    * [***Edit booking***](#edit-booking)
    * [***Delete booking***](#delete-booking)
1. [**Wave accessibility evaluation**](#wave-accessibility-evaluation)
1. [**Bugs**](#bugs)
    * [***Unfixed Bugs***](#unfixed-bugs)

## Manual testing
I manually tested this site in multiple ways highlighted below:
* I tested every feature and its functionality as highlighted below in the [user stories](#user-stories).
* I deployed the site in an early stage on Heroku to make sure everything was working as intended. 
* I received invaluable feedback from my mentor David, students in my community, family members and friends working in the industry.
* I tested the site for cross-compatibility in the two most used browsers, Chrome and Safari.
* I used DevTools to easily move between different screen sizes, simulating sizes between 370px to 4000px (but it is also functional on even larger screens given the max-width setting on the Body element to keep the content compact instead of stretched).

### User stories
**User Story:** As a site user/admin, I can navigate the site content from the landing page so that I can access all the content easily and find what I'm looking for.

* Expected:
    * The landing page should include a navigation bar with links to different pages.
    * Each section on the landing page should have buttons to access the corresponding pages.
    * Navigation bar pages should be adapted to the logged in user (profile page for users, admin panel for admin user).

* Testing:
    * Visit the landing page.
    * Look for a navigation bar at the top of the page.
    * Check that the navigation bar contains functioning links to all necessary pages (e.g., Home, Menu, Book, Register, Login).
    * Verify that each section on the landing page includes functioning buttons to access the relevant pages.
    * After logging in as both admin and user, verify that the authorized pages are showing up.

* Fix:
    * User profile page is displayed when admin is logged in.
        * Add a context processor for the Admin user and adjust the conditional statement in the base.html to not include authorization for the admin user.

* Result:
    * The landing page includes a navigation bar with functioning links and buttons to access all site content smoothly based on authorization.

**User Story:** As a site user, I can register an account so that I can make a table booking.

* Expected:
    * There should be a page for users to register an account.
    * Users should be able to enter their details and have them authenticated.
    * Password is validated.

* Testing:
    * Navigate to the registration page.
    * Fill out the registration form with valid details.
    * User is asked to choose a new password if their input is not valid.
    * Submit the form.
    * Check that the system registers the user and authenticates their details. 

* Fix:
    * There were no bugs for the pages created with AllAuth.

* Result:
    * Users can successfully register accounts, and their details are authenticated.

**User Story:** As a site user/admin, I can log in and log out of my account so that I can access the booking system.

* Expected:
    * There should be a login page where users/admins can enter their details.
    * After verification of details, users/admins should be directed to their account profile or received errors for incorrect details.
    * There should be a clear indication that you've logged in successfully.
    * Users/admins should be able to log out from their accounts.

* Testing:
    * Visit the login page.
    * Enter valid login details for both user/admin.
    * Submit the login form.
    * Verify that the system authenticates the user/admin.
    * Receive error message for incorrect details.
    * Check that the user/admin is redirected to their account profile.
    * Receive message for successfully logging in.
    * Display in the navigation bar that the user is logged in.
    * Log out from the account.
    * Verify that the user/admin is logged out and redirected to the login page.
    * Display message for successfully logging out.

* Fix:
    * There were no bugs for the pages created with AllAuth.

* Result:
    * Users/admins can successfully log in and out of their accounts, and authentication is functioning correctly.

**User Story:** As an admin user, I can log in to an admin account so that I can confirm/cancel requests and see all current/previous bookings.

* Expected:
    * Have a separate admin panel for authenticated admin users.
    * Admin is taken to admin panel upon logging in.
    * Admins should be able to view all booking requests.
    * Admins should have the ability to filter bookings based on status, date, name and time.
    * Admins should be able to approve/deny bookings.
    * Admins should be able to edit/delete bookings.

* Testing:
    * Login with admin details.
    * Check that the admin is redirected to the admin panel.
    * Navigate to the Bookings section.
    * Verify that all booking requests are displayed.
    * Test the filtering functionality by filtering bookings based on status, date, name and time.
    * Click on a booking and approve/deny it or edit/delete it.

* Fix:
    * Admin panel was created with Django and had no immediate bugs.

* Result:
    * Admins can successfully log in to the admin account, access the admin panel, view bookings, use the filtering functionality and approve/deny or edit/delete bookings.

**User Story:** As a site user, I can access my account so that I can edit my details or delete my account.

* Expected:
    * There should be a profile dashboard accessible to logged-in users.
    * Users should be able to view their account details.
    * Users should be able to edit their account details.
    * Account details are verified by checking that they are not already in use.
    * Users should be able to delete their account.

* Testing:
    * Log in to a user account.
    * Navigate to the profile page in the navigation bar.
    * Verify that the user's account details are displayed.
    * Test the edit functionality by modifying account details.
    * Receive error message if edited details are already in use.
    * Verify that changes are saved successfully and highlighted to the user.
    * Test the delete account functionality.
    * Confirm that the user account is deleted and highlighted to the user.

* Fix:
    * Edit details form didn’t update the details that were changed, but instead updated all fields even if they hadn't been changed. This raised the validation error for all fields with validation.
        * Created an instance model to check for the field that had changed and only validate those details.
    * The bookings associated to the old user details did not register to the new user details. 
        * Added the User model in the booking Model with a user field and a Foreignkey and connected the user bookings to the user ID (instead of email as I had done previously) and created a view (update_bookings) to validate the bookings to the new user details.
    * New user details are not validated for already existing user details.
        * Use clean method for username/email fields in the EditForm form.

* Result:
Users can successfully access their account, view, edit, and delete account details.

**User Story:** As a site user/admin, I can send a booking request with all my details so that I can book a table with all the necessary details.

* Expected:
    * There should be a booking request form accessible to logged-in users.
    * The booking request form should include fields for personal details, time, date, and guest options.
    * The form should be pre-populated with the user's account details.
    * There should be a section for special requests.

* Testing:
    * Log in to a user and admin account.
    * Navigate to the booking request form.
    * Verify that the form includes fields for personal details, time, date, and guest options.
    * Check that the form is pre-populated with the user's account details.
    * Test that the special request section is not a required field.
    * Submit the booking request form.

* Fix:
    * Booking form is not accessible ti any logged in user.
        * Use @login_required for the book_table view instead of user.is_authenticated.
    * Booking form not displaying with Crispy forms.
        * Change the form tag from {{ BookingForm| crispy }} to {{ form|crispy }}.

* Result:
    * Users can successfully send a booking request with all necessary details, including personal information and special requests.

**User Story:** As a site user, I can book a table based on the requirements so that I properly book a table and have a high chance of having it approved.

* Expected:
    * The booking page should provide sufficient information on form requirements.
    * Users should receive an error message if they choose an incorrect date, time, or guest amount.
    * Users should receive an error message if they attempt to make an identical booking.

* Testing:
    * Navigate to the booking form as a logged in user.
    * Verify that there is clear information on the page about the form requirements.
    * Test the form by selecting an incorrect date, time, or guest amount.
    * Confirm that an error message is displayed on the field.
    * Attempt to make a booking identical to an existing one.
    * Confirm that an error message is displayed.

* Fix:
    * The times field receives an error message with every selected time, "Select a valid choice. < time > is not one of the available choices".
        * Change available_times list to a tuple with the values as ('10:00', '10:00 AM') and change the TimeField model field to a Charfield instead.

* Result:
    * Users can successfully book a table based on requirements and receive appropriate error messages for incorrect selections.

**User Story:** As a site user, I can edit/cancel my booking requests so that I can customize my requests and have control over my bookings.

* Expected:
    * Users should be able to view all their booking requests on their profile.
    * Users should have the option to edit their booking requests.
    * Verify the new booking details by checking that the user doesn't already have an identical booking.
    * Users should have the option to cancel their booking requests.

* Testing:
    * Log in to the user account.
    * Navigate to the profile page.
    * Verify that all booking requests are displayed.
    * Test the edit functionality by modifying a booking request.
    * Receive error message if booking details already exist.
    * Confirm that changes are saved successfully and highlighted to the user.
    * Test the cancel functionality by canceling a booking request.
    * Confirm that the booking request is successfully canceled and highlighted to the user.

* Fix:
    * New booking details are not validated for already existing bookings.
        * Use clean method for date/time field in the EditBooking form and create existing_booking in the edit_booking view to filter the booking objects and match the new details to already existing bookings.

* Result:
    * Users can successfully edit and cancel their booking requests, providing them with control over their bookings.

**User Story:** As an admin user, I can access each booking so that I can cancel/confirm the requests and see special requests/contact details for the user.

* Expected:
    * Admin users should have access to every booking in the admin panel.
    * Admin users should be able to cancel or confirm booking requests.
    * Admin users should be able to view all customer details and booking request details for each booking.

* Testing:
    * Log in to the admin account.
    * Navigate to the admin panel.
    * Verify that all booking requests are listed under the Bookings section.
    * Test the cancel functionality by canceling a booking request.
    * Confirm that the booking request is successfully canceled and highlighted to the admin user.
    * Test the confirm functionality by confirming a booking request.
    * Confirm that the booking request is successfully confirmed and highlighted to the admin user.
    * Select a booking request and verify that all customer details and booking request details are visible.

* Fix:
    * Admin panel was created with Django and had no immediate bugs.

* Result:
    * Admin users can successfully access, cancel, and confirm booking requests, and view all relevant details for each booking.

**User Story:** As a site user, I can access the menu for the restaurant so that I can see what food they have.

* Expected:
    * There should be a link to the menu from the landing page and navigation bar.
    * A page with all menu items and prices should be available.
    * Clear headings and descriptive names of each menu item should be provided.

* Testing:
    * Navigate to the landing page and verify that there is a section and button to access the menu page.
    * Look for a link to the menu in the navigation bar.
    * Click on the menu link and verify that it directs to the menu page.
    * On the menu page, verify that all menu items and prices are displayed.
    * Check that each menu item has a clear heading and descriptive name.

* Fix:
    * This is a static menu and it had no immediate bugs.

* Result:
    * Users can successfully access the restaurant menu and view all menu items with clear descriptions and prices.

**User Story:** As a site user/admin, I can receive confirmations on my actions on the site so that I know the actions have been fulfilled.

* Expected:
    * Users should receive confirmation when they log in.
    * Users should receive confirmation when they log out.
    * Users should receive confirmation when they send a booking request.
    * Users should receive confirmation when they edit or delete their account.
    * Users should receive confirmation when they edit or delete their booking requests.

* Testing:
    * Login/logout as a user.
    * Send a booking request.
    * Verify that a confirmation message is displayed after each action.
    * Edit account details.
    * Delete account.
    * Edit a booking request.
    * Delete a booking request.
    * Verify that a confirmation message is displayed after each action.

* Fix:
    * Messages are not displayed with a background color.
        * Used DevTools to find what class and css styling was being used on the messages alerts and updated those to the stylesheet with green/red colors.

* Result:
    * Users/admins receive confirmation messages for various actions.

## Validator testing 

- HTML
  - There were no errors present when passing through the official W3C validator ![W3C validator](docs/images/w3html.png)

- CSS
  - There were no errors present when passing through the official Jigsaw validator with direct input ![(Jigsaw) validator](docs/images/w3css.png)

- PEP8
  - There were no errors present when passing through the PEP8 CI Python linter ![PEP8](docs/images/pep8.png)

## Lighthouse testing 

This testing was done in an incognito window in Chrome to make sure the results were not influenced by browser extensions.

The lower scores were for two main reasons:
- The cdn imports from bootstrap, Google fonts and Font Awesome.
- Hero image and background image, which were compressed and even resized multiple times without a change in score. It was not possible to edit them further without a bigger change in quality.

### **Landing page**
- Desktop version:

![Desktop landing page](docs/images/lighthouse/land-desk.png)

- Mobile version:

![Mobile landing page](docs/images/lighthouse/land-mob.png)

### **Menu**

- Desktop version:

![Desktop menu](docs/images/lighthouse/menu-desk.png)

- Mobile version:

![Mobile menu](docs/images/lighthouse/menu-mob.png)

### **Booking form**

- Desktop version:

![Desktop booking form](docs/images/lighthouse/form-desk.png)

- Mobile version:

![Mobile booking form](docs/images/lighthouse/form-mob.png)

### **Booking success**

- Desktop version:

![Desktop booking success](docs/images/lighthouse/success-desk.png)

- Mobile version:

![Mobile booking success](docs/images/lighthouse/success-mob.png)

### **Profile**

- Desktop version:

![Desktop profile](docs/images/lighthouse/prof-desk.png)

- Mobile version:

![Mobile profile](docs/images/lighthouse/prof-mob.png)

### **Edit account details**

- Desktop version:

![Desktop edit account details](docs/images/lighthouse/edit-acc-desk.png)

- Mobile version:

![Mobile edit account details](docs/images/lighthouse/edit-acc-mob.png)

### **Delete account**

- Desktop version:

![Desktop delete account](docs/images/lighthouse/del-acc-desk.png)

- Mobile version:

![Mobile delete account](docs/images/lighthouse/del-acc-mob.png)

### **Edit booking**

- Desktop version:

![Desktop edit booking](docs/images/lighthouse/edit-book-desk.png)

- Mobile version:

![Mobile edit booking](docs/images/lighthouse/edit-book-mob.png)

### **Delete booking**

- Desktop version:

![Desktop delete booking](docs/images/lighthouse/del-book-desk.png)

- Mobile version:

![Mobile delete booking](docs/images/lighthouse/del-book-mob.png)

## Wave accessibility evaluation

I also used the Wave evaluation tool to make sure I covered all my bases. 

The evaluation is free from errors on all pages.

![Wave evaluation](docs/images/wave.png)

## Bugs

See more feature related bugs in the [user story section](#user-stories).

- New CSS styling was not displaying properly in deployed project after changes.
    - Manually updated the staticfiles directory with "python3 manage.py collectstatic".
- Project deployment failed due to database error.
    - Added the elephantSQL instance link in project Config Vars section.

### Unfixed Bugs
- When there are too many bookings displayed on the user's profile, there is no space between the white box containing the bookings and the footer. However, the actual content remains visible. 
I chose not to address this issue because the staff will routinely clear all unnecessary bookings from the system on a weekly basis. Additionally, it's unlikely that users will have an excessive number of bookings simultaneously.