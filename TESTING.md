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