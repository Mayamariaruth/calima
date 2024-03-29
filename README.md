# Calima

## Introduction

Calima is a Caribbean-inspired restaurant nestled in the heart of Berawa, Bali, offering an authentic menu that pays homage to the diverse cuisines of the Caribbean.

Our site aims to bring the vibrant flavors and rich culinary traditions to your fingertips and allow you to book a table with us to create an unforgettable dining experience.

Link to the live site here - [Calima](https://calima-665aec414d74.herokuapp.com/)

![Responsive Mockup](docs/images/amiresp.png)

## Table of Contents:
1. [**Introduction**](#introduction)
1. [**Planning**](#planning)
    * [***User Stories***](#user-stories)
        * [***Dropped***](#dropped)
    * [***Site aims***](#site-aims)
    * [***Scope***](#scope)
        * [***Book table form***](#1-book-table-form)
        * [***User profile***](#2-user-profile)
        * [***Admin panel***](#3-admin-panel)
        * [***Navigation bar***](#4-navigation-bar)
        * [***Footer***](#5-footer)
        * [***Landing page***](#6-landing-page)
        * [***Menu***](#7-menu)
    * [***Wireframes***](#wireframes)
    * [***Database schema***](#database-schema)
    * [***Color scheme***](#color-scheme)
    * [***Typography***](#typography)
1. [**Agile**](#agile)
1. [**Features**](#Features)
    * [***Navigation***](#navigation)
        * [***Navigation - User***](#navigation---user)
        * [***Navigation - Admin***](#navigation---admin)
    * [***Landing page***](#landing-page)
        * [***Hero image***](#hero-image)
        * [***About***](#about)
        * [***Menu***](#menu)
        * [***Book a table***](#book-a-table)
    * [***Footer***](#footer)
    * [***AllAuth***](#allauth)
        * [***Register***](#register)
        * [***Login***](#login)
        * [***Logout***](#logout)
    * [***Menu***](#menu-1)
    * [***Booking form***](#booking-form)
    * [***User***](#user)
        * [***Booking success***](#booking-success)
        * [***Profile***](#profile)
        * [***Edit/delete account***](#editdelete-account)
        * [***Edit/Delete bookings***](#editdelete-bookings)
    * [***Admin***](#admin)
        * [***Admin panel***](#admin-panel)
    * [***Future features***](#future-features)
1. [**Deployment**](#deployment)
    * [***Cloning***](#cloning)
1. [**Testing**](#testing)
1. [**Credits**](#credits)
    * [***Technologies***](#technologies)
    * [***Code***](#code)
    * [***Content***](#content)
    * [***Media***](#media)
    * [***General reference***](#general-reference)

## Planning

### User stories
As a site user, I can navigate the site content from the landing page so that I can access all the content easily and find what I'm looking for

- Acceptance Criteria
    * Have a navigation bar with links to the different pages

    * Have separate sections for each page on the landing page

    * Have buttons in each section to access the different pages


As a site user, I can register an account so that I can make a table booking

- Acceptance Criteria
    * Have a page for users to register an account

    * They use their details to register

    * Details are authenticated


As a site user/admin, I can log in and log out of my account so that I can access the booking system

- Acceptance Criteria
    * Have a login page

    * They enter their login details

    * Login details are authenticated

    * They are taken to their account profile and can access the booking form


As a admin user, I can log in to an admin account so that I can confirm/cancel requests and see all current/previous bookings

- Acceptance Criteria
    * Have an admin login with an admin panel

    * See all booking requests, confirmed bookings and canceled bookings

    * Ability to filter all bookings based on status and date


As a site user, I can access my account so that I can edit my details or delete my account

- Acceptance Criteria
    * Have a profile dashboard

    * See my account details

    * Edit my account details

    * Delete my account


As a site user, I can send a booking request with all my details so that I can book a table with all the necessary details

- Acceptance Criteria
    * Booking request form includes my personal details, time, date and guest options

    * Form is prepopulated with my account details

    * Special request section


As a site user, I can book a table based on the requirements so that I properly book a table and have a high chance of having it approved

- Acceptance Criteria 

    * There is enough information on the page so I understand the form requirements

    * I get an error if I've chosen an incorrect date, time or guest amount

    * I get an error if I've already made an identical booking


As a site user, I can edit/cancel my booking requests so that I can customize my requests and have control over my bookings

- Acceptance Criteria
    * See all my requests on my profile

    * Edit the requests

    * Cancel the requests


As a admin user, I can access each booking so that I can cancel/confirm the requests and see special requests/contact details for the user

- Acceptance Criteria
    * Admin access to every booking

    * Cancel/confirm requests

    * Ability to see all customer details and booking request details in each booking


As a site user, I can access the menu for the restaurant so that I can see what food they have

- Acceptance Criteria
    * Link to the menu from the landing page and navigation bar

    * A page with all menu items and prices

    * Clear headings and descriptive names of each menu item


As a site user/admin, I can receive confirmations on my actions on the site so that I know the actions have been fulfilled

- Acceptance Criteria
    * Confirmation when I've sent a booking request

    * Confirmation when I've edited/deleted my account

    * Confirmation when I've edited/deleted my requests


#### Dropped
As an admin user, I can access the menu page so that I can edit/delete menu items

- Acceptance Criteria
    * Admin access to the menu page

    * Edit menu items

    * Delete menu items


As a site user, I can access an About page for the restaurant so that I can get more information about the restaurant

- Acceptance Criteria
    * Page accessible from the navigation bar and landing page

    * Displaying the restaurant's story and details about the staff and food

    * Images of the restaurant and the Caribbean


As an admin user, I can edit the About page so that I can control what information is displayed

- Acceptance Criteria
    * Admin access to the About page

    * Ability to edit content

    * Add/delete images


As a site user, I can contact the restaurant through the site so that I can easier get into contact with the restaurant

- Acceptance Criteria
    * A contact page accessible from the navigation bar

    * A form to fill out with my message and details

    * Pre-populated user details for logged in users


As a site user, I can access other people's reviews and add my own reviews on the site so that I can see what people think about the restaurant and add my own opinion to the mix

- Acceptance Criteria
    * Reviews section on the landing page

    * Other people's reviews are displayed

    * I can add my own reviews

    * I can edit/delete my own reviews


### Site aims 
The primary goal of the website is to increase the visibility of Calima online and to streamline online reservations. 

By having a strong online presence, we aim to attract more customers, especially tourists and locals searching for unique Caribbean dining experiences where they would never expect it!
By having a platform for engaging with customers beyond their dining experience and enabling efficient table bookings helps Calima better manage resources and provide a seamless experience for both staff and guests.

The website should reflect the ambiance of Calima and through high-quality visuals and user-friendly design, we aim to convey the restaurant's personality genuinely.

### Scope

The following is a prioritized list outlining the scope of the project. These priorities were determined considering the project's limited time frame and the key features essential for its aim (MVP).

#### 1. Book Table form

* Login functionality: Login authentication for users to access the booking system.
* Booking validation: Ensure no double bookings and restrict bookings to available times.

#### 2. User profile

* User registration: Allow users to create accounts with personal details.
* Profile management: Enable users to update their account information.
* User bookings management: View, modify, or cancel bookings.

#### 3. Admin Panel

* Admin authentication: Secure login for administrators with appropriate permissions.
* Booking management: Full control over bookings, including adding, editing, and canceling bookings.
* User management: Ability to view and manage user accounts.

#### 4. Navigation Bar

* Essential links: Home, Menu, Book, Register, Login.
* Essential links based on authentication: User Profile, Admin Panel.

#### 5. Footer

* Important information: Location, opening hours, contact email and social media links.

#### 6. Landing Page

* Inspiring look: Showcase the restaurant's ambiance through high-quality visuals and user-friendly design.
* Description of Restaurant: Brief description of the restaurant.
* Links: Sections with links to the menu and booking form.

#### 7. Menu

* Menu: Provide a comprehensive menu with categories and pricing.

### Wireframes

All pages on the site, except for the landing page, feature a consistent design style, characterized by a shared background image and a clean white text box containing the content. 
As a result, I'm only displaying the wireframes for the critical pages below. Despite minor differences, the overall appearance turned out pretty identical.

- **Landing page**
---
![Landing page desktop](docs/wireframes/land-desk.png)
![Landing page ipad](docs/wireframes/land-ipad.png)
![Landing page mobile](docs/wireframes/land-mob.png)


- **Booking form**
---
![Booking form desktop](docs/wireframes/form-desk.png)
![Booking form ipad](docs/wireframes/form-ipad.png)
![Booking form mobile](docs/wireframes/form-mob.png)

- **Profile**
---
![Profile desktop](docs/wireframes/prof-desk.png)
![Profile ipad](docs/wireframes/prof-ipad.png)
![Profile mobile](docs/wireframes/prof-mob.png)


- **Menu**
---
![Menu desktop](docs/wireframes/menu-desk.png)
![Menu ipad](docs/wireframes/menu-ipad.png)
![Menu mobile](docs/wireframes/menu-mob.png)


### Database schema
 I used Django's built-in User Model for the user accounts and I created a custom model for bookings. 
 The booking model and the user model were connected through a foreign key, allowing me to associate bookings with specific users.
 From this, I was able to enhance user experience by pre-populating the booking form with the user account details when making a booking request.

For future features, I plan on creating a model for the menu as well.

The time field was changed from a TimeField to a CharField in early production due to a bug as seen in [TESTING.md](TESTING.md).

![ERD](docs/images/erd.png)

### Color scheme
I adapted the colors on the site to my hero image so it would look more cohesive across the site and the colors are also very Caribbean-themed.
I generated the colors from the hero image on [Coolors](https://coolors.co/).

I utilized the Contrast grid by Eightshapes to test my color combos so the colors complied with the highest accessibility.

![Color](docs/images/eightshapes.png)

### Typography
I used three different fonts across the page:
 * Protest Riot, for the title and landing page headings.
 * Playfair Display, for most of the content on the site.
 * Dancing script, for the hero image quote.

The fonts were sourced from Google Fonts.

## Agile

Throughout the project, I followed the Agile methodology by using GitHub projects and issues. This allowed me to organize the project's tasks into epics and user stories, making it easy to manage them on the Kanban board. This helped break down the work into smaller parts, making development smoother and more efficient.
By utilizing issues in GitHub and MSCW (MoSCoW Prioritization), I was also able to label and categorize the tasks to stay focused on the MVP. The "Won't Have's" of this project are still present on the Kanban board for future development.

I decided not to use sprints in this project due to it being more of a team logic and it made more sense for me to work in a task-based manner.
Even though I worked on this project alone, using Agile principles helped me track progress effectively and ensure future maintenance.

## Features 

I went with one design for the landing page, to make it more unique and one design for all the rest of the pages, to keep it simple and cohesive site-wide.

### Navigation
- Navigation bar for users who are not logged in.
- Functional links to all pages.
- Hamburger icon with toggle function for smaller screens.

![Navigation bar](docs/images/features/nav.png)

#### Navigation - User
- Navigation bar for users who are logged in, authenticated with conditional statements in the base.html.
- Functional links to all pages.
- Visible indication of the logged in user.

![Navigation bar](docs/images/features/user-nav.png)

#### Navigation - Admin
- Navigation bar for admin users who are logged in, authenticated with conditional statements in the base.html.
- Functional links to all pages, including the Django admin panel that serves as the admin profile in this project.
- Visible indication of the logged in user.

![Navigation bar](docs/images/features/admin-nav.png)

### Landing page

#### Hero image
- Image of a Caribbean beach as the hero image and a fitting heading to showcase the theme of the site.
- A Trinidadian proverb as the heading, meaning: "It is better to overeat than to waste great food". Quoted from my own Uncle Errol to personalize the site.

![Hero image](docs/images/features/land.png)

#### About
- Brief introduction and description of the restaurant.

![About](docs/images/features/about.png)

#### Menu
- Brief explanation of the menu.
- A functioning button to the menu.

![Landing menu](docs/images/features/land-menu.png)

#### Book a table
- Brief explanation of the ambiance of the restaurant.
- A functioning button to the booking form.

![Landing book table](docs/images/features/land-book.png)

### Footer
- Three sections with Opening hours, Address and Contact details.
- Social links that lead to the home pages of each site.

![Footer](docs/images/features/footer.png)

### AllAuth

#### Register
![Register](docs/images/features/register.png)

#### Login
![Login](docs/images/features/login.png)

#### Logout
![Logout](docs/images/features/logout.png)

### Menu
- Static menu with Starters, Mains and Desserts sections.
- Clear names of each menu item and prices underneath.

![Menu](docs/images/features/menu.png)

### Booking form
- Only accessible to logged in users.
- Extensive booking form with pre-populated fields with the user details.
- Booking requirements are displayed to the user.
- Error messages under each field if the added booking details do not match the requirements.
- Error message under the navigation bar if the user tries to book a new booking with details that already exist in another booking on their profile.

![Booking form](docs/images/features/book.png)

### User

#### Booking success
- Page that comes up after a successful booking made by the user.
- A brief "thank you" text and information of what is next to come.
- A button to the user profile.
- Success message under the navigation bar.

![Booking success](docs/images/features/book-success.png)

#### Profile
- CRUD - User profile only accessible by the user (not admin).
- Highlights the user account details.
- Highlights the user's booking details.
- Buttons to edit/delete the account.
- Buttons to edit/delete the bookings (on smaller screens the buttons are removed to save space and one main action button is added with a dropdown list of the actions).
- Success messages under navigation bar after completed actions (edit/delete).

This is the CRUD operation of the site, where a user can view, edit and delete information.
For future features, I wanted to create a similar profile for the admin instead of just the admin panel built by Django.

![Profile](docs/images/features/profile.png)

#### Edit/delete account
- Edit user account details form.
- Error messages under each field if the new account details are already in use.
- Delete account confirmation page with buttons to delete or cancel.

![Edit/delete account](docs/images/features/edit-acc.png)

![Edit/delete bookings](docs/images/features/del-acc.png)

#### Edit/delete bookings
- Edit booking details form.
- Error messages under each field if the added booking details do not match the booking requirements.
- Error message under the navigation bar if the user tries to book a new booking with details that already exist in another booking on their profile.
- Delete booking confirmation page with buttons to delete or cancel.

![Edit/delete bookings](docs/images/features/edit-book.png)

![Edit/delete bookings](docs/images/features/del-book.png)

### Future features
- CRUD - Admin profile (not just the Django admin panel) displaying all bookings, ability to edit/delete bookings and edit/delete details.
- Dynamic menu page with a Model (add/delete items with admin access).
- Reviews section on the landing page with user ability to add their own reviews.
- An About page with more information about the restaurant (admin access to customize the page).
- A Contact page for users to easily contact the restaurant.
- 500 and 404 error templates.

## Deployment

To deploy the site to Heroku, I went through below steps: 
- Go to [Heroku](https://heroku.com/) and log into your account.
- Click "Create new app" on the front page.
- Give your app a name (every name has to be unique on Heroku so it's ok if you can't name your project the same as on GitHub).
- Choose your region (USA or Europe) and click "Create app".
- You're then taken to the dashboard of your app where you have a navigation bar. Click on the Settings tab and scroll down to "Config Vars".
- Click "Reveal Config Vars" and input any necessary environment variables (such as your database URL or secret key). **NOTE: This project utilized one secret key during development but it has since been updated.**
- Go back to the navigation bar and select "Deploy".
- Scroll down to the "Connect to GitHub" section and click on the Connect button.
- After allowing Heroku access to GitHub, the "Connect to GitHub" section will allow you to search for the repository you wish to connect.
- Find your repository and click "Connect".
- You can now choose automatic deploys (Heroku deploys your app after every GitHub push you make) or manual deploys.
- After choosing a deployment method, click the deploy button and make sure you deploy from the correct branch.

Live link to the site - [Calima](https://calima-665aec414d74.herokuapp.com/)

### Cloning

I used the cloning method to use the VSCode desktop IDE with GitHub, below are the steps I took:
- Generate a repository and click the Code button in the middle of the screen.
- Go to Local and under Clone, copy the Git repository URL on the HTTPS tab.
- Go to the VSCode IDE front page and click 'Clone Git Repository' under Start or go to the Source Control button on the left-hand side menu bar and click 'Clone Repository'.
- Input the URL in the URL tab at the top of the window and press Enter.
- Select the location/folder where you want to store your repository on your computer through the popup and click the 'Select Repository location' button.
- VSCode will now clone the repository and you can choose to open it in your current window or in a new window.

## Testing

All the testing for this project can be found in a separate document [here](TESTING.md).

## Credits 

### Technologies

- The packages installed for this project can be found in [the requirements.txt](requirements.txt).
- Django was used as the Python framework.
- Django AllAuth was used for the user authentication and register, sign-up and login tasks.
- ElephantSQL was used for the database during development and in deployment.
- Bootstrap 5.3.2 was used to style HTML, CSS and minor JavaScript.

### Code 

- I drew help from the walk-through of the Codestar project. There are similarities in some of the code but I adapted it to fit the aims of this project.

Below are links that helped me adapt/build certain features:
- [Context Processors](https://djangocentral.com/how-to-create-custom-context-processors-in-django/)
- [Removing ‘Sites’ from Django admin page](https://itecnote.com/tecnote/removing-sites-from-django-admin-page/)
- [Django admin page Removing 'Group'](https://stackoverflow.com/questions/13229235/django-admin-page-removing-group)
- [Django - Update User Profile](https://dev.to/earthcomfy/django-update-user-profile-33ho)
- [Django Username or Email Authenticate](https://forum.djangoproject.com/t/django-username-or-email-authenticate/2775/5)
- [Username validation and login in django](https://itecnote.com/tecnote/username-validation-and-login-in-django/)

### Content 

- The wireframes were created with Balsamiq.
- The text content on the landing page was generated with ChatGPT.
- The social media links directly to the home pages of each site.
- The ERD diagram was created with [Smartdraw](https://www.smartdraw.com/entity-relationship-diagram/er-diagram-tool.htm).
- Fonts were acquired from [Google Fonts](https://fonts.google.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).
- The menu items were taken from [Cane Rum Society](https://www.canerumsociety.com/) and [Island Hoppers]((https://islandhoppers.se/meny)).

### Media

- The hero image and background image were acquired from [Unsplash](https://unsplash.com/).
- The color palette was generated with the image on [Coolors](https://coolors.co/).
- [Am I Responsive](https://ui.dev/amiresponsive) was used to generate the initial image of the ReadME to showcase how the site looks on different screens.

### General references:
- [W3Schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [Geeks for Geeks](https://www.geeksforgeeks.org/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Django Documentation](https://docs.djangoproject.com/en/3.2/)