# Testing 

## Table of Contents:
1. [**Bugs**](#bugs)
    * [***Fixed Bugs***](#fixed-bugs)
    * [***Unfixed Bugs***](#unfixed-bugs)

### Manual testing
I manually tested this site in multiple ways highlighted below:
* I tested every feature and its responsiveness through an extension of a live server in VScode.
* I deployed the site in an early stage on Heroku to make sure everything was working as intended. 
* I received invaluable feedback from my mentor David, students in my community, family members and friends working in the industry.
* I tested the site for cross-compatibility in the two most used browsers, Chrome and Safari.
* I used DevTools to easily move between different screen sizes, simulating sizes between 370px to 4000px (but it is also functional on even larger screens given the max-width setting on the Body element to keep the content compact instead of stretched).


expected -
testing -
result - 
fix -

### User stories
As a site user I can navigate the site content from the landing page so that I can access all the content easily and find what I'm looking for

- Acceptance Criteria
    * Have a navigation bar with links to the different pages

    * Have separate sections for each page on the landing page

    * Have buttons in each section to access the different pages


As a site user I can register an account so that I can make a table booking

- Acceptance Criteria
    * Have a page for users to register an account

    * They use their details to register

    * Details are authenticated


As a site user/admin I can log in and logout out of my account so that I can access the booking system

- Acceptance Criteria
    * Have a login page

    * They enter their login details

    * Login details are authenticated

    * They are taken to their account profile and can access the booking form


As a admin user I can log in to an admin account so that I can confirm/cancel requests and see all current/previous bookings

- Acceptance Criteria
    * Have an admin log in with an admin panel

    * See all booking requests, confirmed bookings and cancelled bookings

    * Ability to filter all bookings based on status and date


As a site user I can access my account so that I can edit my details or delete my account

- Acceptance Criteria
    * Have a profile dashboard

    * See my account details

    * Edit my account details

    * Delete my account


As a site user I can send a booking request with all my details so that I can book a table with all the necessary details

- Acceptance Criteria
    * Booking request form includes my personal details, time, date and guest options

    * Form is prepopulated with my account details

    * Special request section


As a site user I can book a table based on the requirements so that I properly book a table and have a high chance of having it approved

- Acceptance Criteria 

    * There is enough information on the page so I understand the form requirements

    * I get an error if I've chosen an incorrect date, time or guest amount

    * I get an error if I've already made an identical booking


As a site user I can edit/cancel my booking requests so that I can customize my requests and have control over my bookings

- Acceptance Criteria
    * See all my requests on my profile

    * Edit the requests

    * Cancel the requests


As a admin user I can access each booking so that I can cancel/confirm the requests and see special requests/contact details for the user

- Acceptance Criteria
    * Admin access to every booking

    * Cancel/confirm requests

    * Ability to see all customer details and booking request details in each booking


As a site user I can access the menu for the restaurant so that I can see what food they have

- Acceptance Criteria
    * Link to the menu from the landing page and navigation bar

    * A page with all menu items and prices

    * Clear headings and descriptive names of each menu item


As a site user/admin I can receive confirmations on my actions on the site so that I know the actions have been fulfilled

- Acceptance Criteria
    * Confirmation when I've sent a booking request

    * Confirmation when I've edited/deleted my account

    * Confirmation when I've edited/deleted my requests


### Validator Testing 
I tested all the pages in the validators to make sure they all passed.
- HTML
  - There were no errors present when passing through the official W3C validator ![W3C validator]()

- CSS
  - There were no errors present when passing through the official Jigsaw validator ![(Jigsaw) validator]()

### Lighthouse testing 

This testing was done in an incognito window in Chrome to make sure the results were not influenced by browser extensions.

The desktop testing was the same score for the home page and quiz page but the mobile testing differed by just a couple of points but both pages scored incredibly well.

At first, the mobile testing was in the high 80s score but after compressing the background image, the scores went up into the 90s range.

__Desktop version:__

![Desktop home page](docs/screenshots/lighthouse-desktop.png)

#### Home front page 
__Mobile version:__

![Mobile home page](docs/screenshots/home-mobile.png)

#### Quiz area

__Mobile version:__

![Mobile quiz page](docs/screenshots/quiz-mobile.png)

### Wave accessibility evaluation

I also used the Wave evaluation tool to make sure I covered all my bases. 

The evaluation is free from errors and below is taken from the Home page and quiz page.

#### Wave home page
![Wave evaluation](docs/screenshots/wave-home.png)

#### Wave quiz page
![Wave evaluation](docs/screenshots/wave-quiz.png)

### Bugs

- 

#### Unfixed Bugs
- When too many bookings on profile, there is no space between white box and footer (but the actual content is still visible) but I decided not to fix that since staff would be clearing all bookings weekly from the system that are not necessary and we dont expect users to have that many bookings 