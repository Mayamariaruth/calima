# Testing 

### Manual testing
I manually tested this site in multiple ways highlighted below:
* Tested every feature and its responsiveness through an extension of a live server in VScode.
* Deployed the site in an early stage and received feedback from a professional developer (mentor), as well as students in my community.
* Tested the site for cross-compatibility in the two most used browsers, Chrome and Safari.
* I used DevTools to easily move between different screen sizes, simulating sizes between 320px to 4000px (but it is also functional on even larger screens given the max-width setting on the Body element to keep the content compact instead of stretched).

### Validator Testing 
I tested all the pages in the validators to make sure they all passed.
- HTML
  - There were no errors present when passing through the official W3C validator ![W3C validator](docs/screenshots/html-validator.png)

- CSS
  - There were no errors present when passing through the official Jigsaw validator ![(Jigsaw) validator](docs/screenshots/css-validator.png)

### JSHint testing
There were no warnings with the JSHint testing after successfully sorting out the bugs highlighted in the [Bugs section](#bugs).

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