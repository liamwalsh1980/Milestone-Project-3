# FilmZone

## Code Institute - Milestone Project 3 (Testing)

![Image template](static/images/testing/iamresponsive-testing.png)

<a href="https://filmzone-project.herokuapp.com/" target="_blank">Click here to view FilmZone live</a>

## Table of contents

1. [Testing](#testing)
    * [Screen sizes](#screen-sizes)
        * [Large screens](#large-screens)
        * [Small screens](#small-screens)
    * [Navigation bar menu](#navigation-bar-menu)
        * [Full screen navigation bar](#full-screen-navigation-bar)
        * [Hamburger navigation bar](#hamburger-navigation-bar)
    * [User stories tested ](#user-stories-tested)
        * [Story 1](#story-1)
        * [Story 2](#story-2)
        * [Story 3](#story-3)
        * [Story 4](#story-4)
        * [Story 5](#story-5)
        * [Story 6](#story-6)
    * [W3C Markup Validation Service](#w3c-markup-validation-service)
        * [Base template tested](#base-template-tested)
        * [Homepage tested](#homepage-tested)
        * [Films page tested](#films-page-tested) 
        * [Signup page tested](#signup-page-tested)
        * [Login page tested](#login-page-tested)
        * [Profile page tested](#profile-page-tested)
        * [Add Film page tested](#add-film-page-tested)
        * [Edit Film page tested](#edit-film-page-tested)
        * [Genres page tested](#genres-page-tested)
        * [Add genre page tested](#add-genre-page-tested)
        * [Edit genre page tested](#edit-genre-page-tested)
        * [Contact Us page tested](#contact-us-page-tested)
    * [W3C CSS Validation Service](#w3c-css-validation-service)
        * [CSS coding tested](#css-coding-tested)
    * [JS Hint Javascript code validator](#js-hint-javascript-code-validator)
        * [Script.js](#script.js)
        * [sendEmail.js](#sendemail.js)
    * [PEP8 online validator](#pep8-online-validator)
        * [App file](#app-file)
        * [Env file](#env-file)
    * [Web Browsers](#web-browsers)
        * [Google Chrome](#google-chrome)
        * [Apple Safari](#apple-safari)
        * [Microsoft Edge](#microsoft-edge)
        * [Mozilla Firefox](#mozilla-firefox)
    * [Testing responsiveness](#testing-responsiveness)
        * [Mobile screenshots](#mobile-screenshots)
        * [Tablet screenshots](#tablet-screenshots)
        * [Desktop screenshots](#desktop-screenshots)
    * [Lighthouse testing](#lighthouse-testing)
        * [Desktop results](#desktop-results)
        * [Mobile results](#mobile-results)
    * [Issues fixed](#issues-fixed)
        * [Films page layout](#films-page-layout)
        * [Modal issues](#modal-issues)
    * [Further testing](#further-testing)
        * [EmailJS](#emailjs)
        * [Mobile first](#mobile-first)
    * [Bugs outstanding](#bugs-outstanding)

Return to my [README Doc](README.md) 

[Back to top ⇧](#filmzone)

## Testing

### Screen sizes
I decided to use the Materialize CSS grid (rows and columns) to structure the website offering good UX on all screen sizes. With this in mind the Laptop and Desktop screens (large) layout is different to tablet and mobile screens (small) on many pages. For example, on the Films page users can see 2 films side by side on bigger screens and 1 on smaller screen sizes.  

#### Large screens
![Image template](static/images/testing/screen_sizes/films-large-screen.png)

#### Small screens
![Image template](static/images/testing/screen_sizes/films-small-screen.png)

### Navigation bar menu
#### Full screen navigation bar
On big screens the navigation bar has page titles. Any page title that's hovered over changes color to indicate its a clickable link. I testing different styles for the Navbar however, i wanted to keep it clean and tidy. At one stage the 'Films' link was a dropdown menu giving users the option to click a film based on Genre. I decided to remove this feature for now to keep the navbar simple and easy to use. I added a search facility on the 'Films' page instead to make it easy for users to find a specific film based on Genre type. 

##### Logged out users
![Image template](static/images/testing/navbar/navbar-logged-out.png)

##### Logged in users
![Image template](static/images/testing/navbar/navbar-logged-in-user.png)

##### Logged in Admin user
![Image template](static/images/testing/navbar/navbar-logged-in-admin-user.png)

[Back to top ⇧](#filmzone)

#### Hamburger navigation bar
When testing the navigation bar I wanted to make sure that it collapses into a hamburger menu (3 horizontal bars) on smaller screens. This is common practice to have and offers the user the option to look and click onto another page within the website. I made sure that the FilmZone logo and icon was shown at the top of the hamburder menu when a user opens the navnar on a smaller screen like a mobile or tablet. 

##### Logged out users
![Image template](static/images/testing/navbar/mob-navbar-logged-out.png)

##### Logged in Admin user
![Image template](static/images/testing/navbar/mob-navbar-logged-in-user.png)

##### Logged in Admin user
![Image template](static/images/testing/navbar/mob-navbar-logged-in-admin-user.png)

[Back to top ⇧](#filmzone)

### User Stories tested
#### **Story 1**
A user that doesn’t have an account visits FilmZone and wants ideas on what film to watch for the evening. This user enjoys all types of Films and likes the Actor Al Pacino. 
- FilmZone: If the user navigates to the 'Films' page and use the Search Facility to look up films with Al Pacino staring by typing in the search facility 'Al Pacino'. 

![Image template](static/images/testing/user_stories/user-story-1.png)

#### **Story 2**
I'm a registered user to FilmZone and I've just watched a new Film and want to offer a review for others to consider watching it.
- FilmZone: This user can login to their account/profile and then click the 'Add Film' from the Navbar or 'Add New Film' link from the profile page to then enable the option to add the new Film they have just watched. 

![Image template](static/images/testing/user_stories/user-story-2-1.png)

![Image template](static/images/testing/user_stories/user-story-2-2.png)

![Image template](static/images/testing/user_stories/user-story-2-3.png)

[Back to top ⇧](#filmzone)

#### **Story 3**  
A registered user that just finished watching their favourite Film. After which they want to update the Film record on FilmZone to show all site visitors more information i.e. More actors, a different image, a favourite scene change. 
- FilmZone: This user can login to their account/profile and then within the profile page locate the film in question from the accordion and click the 'Edit' button to open up the Film details already added. The user can then make the changes they want and click 'Edit Film' to update the record.

![Image template](static/images/testing/user_stories/user-story-2-1.png)

![Image template](static/images/testing/user_stories/user-story-3-2.png)

![Image template](static/images/testing/user_stories/user-story-3-3.png)

#### **Story 4**
I’m a regular visitor to FilmZone and would be keen to gain access to my own profile to add my own favourite Films.  
- FilmZone: This user can register an account and obtain a profile at anytime free of charge. To do this click the 'signup' link on the navbar. Once signed up and logged in this user can then start adding films to their profile

![Image template](static/images/testing/user_stories/user-story-4-1.png)

![Image template](static/images/testing/user_stories/user-story-4-2.png)

![Image template](static/images/testing/user_stories/user-story-2-2.png)

#### **Story 5**
I've noticed that theres a particular Genre type not listed for me to add a film to. How can i arrange for a new Genre type to be added?
- FilmZone: All users can click the 'Contact Us' link found at the end of the navbar. On this page users can communicate with FilmZone by completed the form and adding a relevant message in reference to the Genre type request. 

![Image template](static/images/testing/user_stories/user-story-5.png)

[Back to top ⇧](#filmzone)

#### **Story 6**
I've just come out of the cinema after watching a great film. I'm keen to add this to my FilmZone profile but I'm not going to be at my computer until tomorrow morning now. 
- FilmZone can be accessed on any device. Therefore, this user can login to their FilmZone account profile and add a film on their smartphone just as easily as on desktop or laptop. They can then check the films page and profile page to see their new film thats just been added. 

![Image template](static/images/testing/user_stories/user-story-6-1.png)

![Image template](static/images/testing/user_stories/user-story-6-2.png)

![Image template](static/images/testing/user_stories/user-story-6-3.png)

![Image template](static/images/testing/user_stories/user-story-6-4.png)

![Image template](static/images/testing/user_stories/user-story-6-5.png)

![Image template](static/images/testing/user_stories/user-story-6-6.png)

![Image template](static/images/testing/user_stories/user-story-6-7.png)

![Image template](static/images/testing/user_stories/user-story-6-8.png)

![Image template](static/images/testing/user_stories/user-story-6-9.png)

[Back to top ⇧](#filmzone)

### W3C Markup Validation Service

#### Base template tested
#### Homepage tested
#### Films page tested
#### Signup page tested
#### Login page tested
#### Profile page tested
#### Add Film page tested
#### Edit Film page tested
#### Genres page tested
#### Add genre page tested
#### Edit genre page tested
#### Contact Us page tested

[Back to top ⇧](#filmzone)

### W3C CSS Validation Service

#### CSS coding tested
* 0 errors returned
* 1 warning returned
    - Imported style sheets are not checked in direct input and file upload modes (line 2)

![Image template](static/images/testing/validator/css-validator.png)

#### JS Hint JavaScript code validator

#### Script.js
* (0 errors found)
* (2 warnings found)
    - Line 12: let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz)
    - Line 13: let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz)

![Image template](static/images/testing/validator/js-validator-script.png)

#### sendEmail.js
* (0 errors found)
* (0 warnings found)

![Image template](static/images/testing/validator/js-validator-sendemail.png)

#### PEP8 online validator

#### App file
* No errors

![Image template](static/images/testing/validator/python-app.png)

#### Env file
* 1 Error (line 12: line too long (126 > 79 characters))

**Fixed by moving around half the code onto another line below.**

Note: No image applied for security of password

[Back to top ⇧](#filmzone)

### Web Browsers

I tested the website across four different web browsers making sure that links worked and pages loaded properly. 

#### Google Chrome
The site was developed using Chrome and therefore testing was being done daily on this browser.

**Homepage**

![Image template](static/images/testing/web_browser/chrome/chrome-homepage-top.png)

![Image template](static/images/testing/web_browser/chrome/chrome-homepage-bottom.png)

**Films page**

![Image template](static/images/testing/web_browser/chrome/chrome-films-page-top.png)

![Image template](static/images/testing/web_browser/chrome/chrome-films-page-bottom.png)

**Signup page**

![Image template](static/images/testing/web_browser/chrome/chrome-signup-page.png)

**Login page**

![Image template](static/images/testing/web_browser/chrome/chrome-login-page.png)

**Profile page**

![Image template](static/images/testing/web_browser/chrome/chrome-profile-page-top.png)

![Image template](static/images/testing/web_browser/chrome/chrome-profile-page-bottom.png)

**Add film page**

![Image template](static/images/testing/web_browser/chrome/chrome-add-film-page-top.png)

![Image template](static/images/testing/web_browser/chrome/chrome-add-film-page-bottom.png)

**Edit film page**

![Image template](static/images/testing/web_browser/chrome/chrome-edit-film-page-top.png)

![Image template](static/images/testing/web_browser/chrome/chrome-edit-film-page-bottom.png)

**Genres page**

![Image template](static/images/testing/web_browser/chrome/chrome-genre-page-top.png)

![Image template](static/images/testing/web_browser/chrome/chrome-genre-page-bottom.png)

**Add genre page**<br>
Note: Adjustment made to the color of the 'Cancel' button to keep the theme of the site consistant

![Image template](static/images/testing/web_browser/chrome/chrome-add-genre-page.png)

**Edit genre page**

![Image template](static/images/testing/web_browser/chrome/chrome-edit-genre-page.png)

**Contact us page**

![Image template](static/images/testing/web_browser/chrome/chrome-contact-us-page.png)

[Back to top ⇧](#filmzone)

#### Apple Safari

**Homepage**

![Image template](static/images/testing/web_browser/safari/safari-homepage-top.png)

![Image template](static/images/testing/web_browser/safari/safari-homepage-bottom.png)

**Films page**

![Image template](static/images/testing/web_browser/safari/safari-films-page-top.png)

![Image template](static/images/testing/web_browser/safari/safari-films-page-bottom.png)

**Signup page**

![Image template](static/images/testing/web_browser/safari/safari-signup-page.png)

**Login page**

![Image template](static/images/testing/web_browser/safari/safari-login-page.png)

**Profile page**

![Image template](static/images/testing/web_browser/safari/safari-profile-page-top.png)

![Image template](static/images/testing/web_browser/safari/safari-profile-page-bottom.png)

**Edit film page**

![Image template](static/images/testing/web_browser/safari/safari-edit-film-page-top.png)

![Image template](static/images/testing/web_browser/safari/safari-edit-film-page-bottom.png)

**Genres page**

![Image template](static/images/testing/web_browser/safari/safari-genre-page-top.png)

![Image template](static/images/testing/web_browser/safari/safari-genre-page-bottom.png)

**Add genre page**<br>
Note: Adjustment made to the color of the 'Cancel' button to keep the theme of the site consistant

![Image template](static/images/testing/web_browser/safari/safari-add-genre-page.png)

**Edit genre page**

![Image template](static/images/testing/web_browser/safari/safari-edit-genre-page.png)

**Contact us page**

![Image template](static/images/testing/web_browser/safari/safari-contact-us-page.png)

[Back to top ⇧](#filmzone)

#### Microsoft Edge

**Homepage**

![Image template](static/images/testing/web_browser/edge/edge-homepage-top.png)

![Image template](static/images/testing/web_browser/edge/edge-homepage-bottom.png)

**Films page**

![Image template](static/images/testing/web_browser/edge/edge-films-page-top.png)

![Image template](static/images/testing/web_browser/edge/edge-films-page-bottom.png)

**Signup page**

![Image template](static/images/testing/web_browser/edge/edge-signup-page.png)

**Login page**

![Image template](static/images/testing/web_browser/edge/edge-login-page.png)

**Profile page**

![Image template](static/images/testing/web_browser/edge/edge-profile-page-top.png)

![Image template](static/images/testing/web_browser/edge/edge-profile-page-bottom.png)

**Add film page**

![Image template](static/images/testing/web_browser/edge/edge-add-film-page-top.png)

![Image template](static/images/testing/web_browser/edge/edge-add-film-page-bottom.png)

**Edit film page**

![Image template](static/images/testing/web_browser/edge/edge-edit-film-page-top.png)

![Image template](static/images/testing/web_browser/edge/edge-edit-film-page-bottom.png)

**Genres page**

![Image template](static/images/testing/web_browser/edge/edge-genre-page-top.png)

![Image template](static/images/testing/web_browser/edge/edge-genre-page-bottom.png)

**Add genre page**
Note: Adjustment made to the color of the 'Cancel' button to keep the theme of the site consistant - **Adjustment made**

![Image template](static/images/testing/web_browser/edge/edge-add-genre-page.png)

**Edit genre page**

![Image template](static/images/testing/web_browser/edge/edge-edit-genre-page.png)

**Contact us page**

![Image template](static/images/testing/web_browser/edge/edge-contact-us-page.png)

[Back to top ⇧](#filmzone)

#### Mozilla Firefox

**Homepage**

![Image template](static/images/testing/web_browser/firefox/firefox-homepage-top.png)

![Image template](static/images/testing/web_browser/firefox/firefox-homepage-bottom.png)

**Films page**

![Image template](static/images/testing/web_browser/firefox/firefox-films-page-top.png)

![Image template](static/images/testing/web_browser/firefox/firefox-films-page-bottom.png)

**Signup page**

![Image template](static/images/testing/web_browser/firefox/firefox-signup-page.png)

**Login page**

![Image template](static/images/testing/web_browser/firefox/firefox-login-page.png)

**Profile page**

![Image template](static/images/testing/web_browser/firefox/firefox-profile-page-top.png)

![Image template](static/images/testing/web_browser/firefox/firefox-profile-page-bottom.png)

**Add film page**

![Image template](static/images/testing/web_browser/firefox/firefox-add-film-page-top.png)

![Image template](static/images/testing/web_browser/firefox/firefox-add-film-page-bottom.png)

**Edit film page**

![Image template](static/images/testing/web_browser/firefox/firefox-edit-film-page-top.png)

![Image template](static/images/testing/web_browser/firefox/firefox-edit-film-page-bottom.png)

**Genres page**

![Image template](static/images/testing/web_browser/firefox/firefox-genre-page-top.png)

![Image template](static/images/testing/web_browser/firefox/firefox-genre-page-bottom.png)

**Add genre page**<br>
Note: Adjustment made to the color of the 'Cancel' button to keep the theme of the site consistant - **Adjustment made**

![Image template](static/images/testing/web_browser/firefox/firefox-add-genre-page.png)

**Edit genre page**

![Image template](static/images/testing/web_browser/firefox/firefox-edit-genre-page.png)

**Contact us page**

![Image template](static/images/testing/web_browser/firefox/firefox-contact-us-page.png)

### Testing responsiveness

I tested the site using Chrome development tools on three different screen sizes to make sure that all features, content, images, links, search facility, card panels, accordion and buttons worked across all screen sizes.

#### Mobile screenshots

**Homepage**

![Image template](static/images/testing/responsiveness/mobile/mobile-homepage-top.png)

![Image template](static/images/testing/responsiveness/mobile/mobile-homepage-bottom.png)

![Image template](static/images/testing/responsiveness/mobile/mobile-homepage-navbar.png)

**Films page**

![Image template](static/images/testing/responsiveness/mobile/mobile-films-page.png)

**Signup page**

![Image template](static/images/testing/responsiveness/mobile/mobile-signup-page.png)

**Login page**

![Image template](static/images/testing/responsiveness/mobile/mobile-login-page.png)

**Profile page**

![Image template](static/images/testing/responsiveness/mobile/mobile-profile-page-top.png)

![Image template](static/images/testing/responsiveness/mobile/mobile-profile-page-middle.png)

![Image template](static/images/testing/responsiveness/mobile/mobile-profile-page-bottom.png)

**Add film page**

![Image template](static/images/testing/responsiveness/mobile/mobile-add-film-page-top.png)

![Image template](static/images/testing/responsiveness/mobile/mobile-add-film-page-bottom.png)

**Edit film page**

![Image template](static/images/testing/responsiveness/mobile/mobile-edit-film-page-top.png)

![Image template](static/images/testing/responsiveness/mobile/mobile-edit-film-page-bottom.png)

**Genres page**

![Image template](static/images/testing/responsiveness/mobile/mobile-genre-page.png)

**Add genre page**

![Image template](static/images/testing/responsiveness/mobile/mobile-add-genre-page.png)

**Edit genre page**

![Image template](static/images/testing/responsiveness/mobile/mobile-edit-genre-page.png)

**Contact us page**

![Image template](static/images/testing/responsiveness/mobile/mobile-contact-us-page.png)

[Back to top ⇧](#filmzone)

#### Tablet screenshots

**Homepage**

![Image template](static/images/testing/responsiveness/tablet/tablet-homepage-top.png)

![Image template](static/images/testing/responsiveness/tablet/tablet-homepage-bottom.png)

![Image template](static/images/testing/responsiveness/tablet/tablet-homepage-navbar.png)

**Films page**

![Image template](static/images/testing/responsiveness/tablet/tablet-films-page.png)

**Signup page**

![Image template](static/images/testing/responsiveness/tablet/tablet-signup-page.png)

**Login page**

![Image template](static/images/testing/responsiveness/tablet/tablet-login-page.png)

**Profile page**

![Image template](static/images/testing/responsiveness/tablet/tablet-profile-page-top.png)

![Image template](static/images/testing/responsiveness/tablet/tablet-profile-page-middle.png)

![Image template](static/images/testing/responsiveness/tablet/tablet-profile-page-bottom.png)

**Add film page**

![Image template](static/images/testing/responsiveness/tablet/tablet-add-film-page.png)

**Edit film page**

![Image template](static/images/testing/responsiveness/tablet/tablet-edit-film-page.png)

**Genres page**

![Image template](static/images/testing/responsiveness/tablet/tablet-genre-page.png)

**Add genre page**

![Image template](static/images/testing/responsiveness/tablet/tablet-add-genre-page.png)

**Edit genre page**

![Image template](static/images/testing/responsiveness/tablet/tablet-edit-genre-page.png)

**Contact us page**

![Image template](static/images/testing/responsiveness/tablet/tablet-contact-us-page.png)

[Back to top ⇧](#filmzone)

#### Desktop screenshots

**Homepage**

![Image template](static/images/testing/responsiveness/desktop/desktop-homepage-top.png)

![Image template](static/images/testing/responsiveness/desktop/desktop-homepage-bottom.png)

**Films page**

![Image template](static/images/testing/responsiveness/desktop/desktop-films-page-top.png)

![Image template](static/images/testing/responsiveness/desktop/desktop-films-page-bottom.png)

**Signup page**

![Image template](static/images/testing/responsiveness/desktop/desktop-signup-page.png)

**Login page**

![Image template](static/images/testing/responsiveness/desktop/desktop-login-page.png)

**Profile page**

![Image template](static/images/testing/responsiveness/desktop/desktop-profile-page-top.png)

![Image template](static/images/testing/responsiveness/desktop/desktop-profile-page-middle.png)

![Image template](static/images/testing/responsiveness/desktop/desktop-profile-page-bottom.png)

**Add film page**

![Image template](static/images/testing/responsiveness/desktop/desktop-add-film-page.png)

**Edit film page**

![Image template](static/images/testing/responsiveness/desktop/desktop-edit-film-page.png)

**Genres page**

![Image template](static/images/testing/responsiveness/desktop/desktop-genre-page-top.png)

![Image template](static/images/testing/responsiveness/desktop/desktop-genre-page-bottom.png)

**Add genre page**

![Image template](static/images/testing/responsiveness/desktop/desktop-add-genre-page.png)

**Edit genre page**

![Image template](static/images/testing/responsiveness/desktop/desktop-edit-genre-page.png)

**Contact us page**

![Image template](static/images/testing/responsiveness/desktop/desktop-contact-us-page.png)

[Back to top ⇧](#filmzone)

### Lighthouse testing

#### Desktop results

* Performance 85% (Issue: Largest Contentful Paint)
* Accessibility 90% 
* Best Practices 93%
* SEO 100%

![Image template](static/images/testing/lighthouse/lighthouse-desktop.png)


#### Mobile results

* Performance 64% (Issues: Largest Contentful Paint and Time to Interactive)
* Accessibility 90%
* Best Practices 93%
* SEO 91%

![Image template](static/images/testing/lighthouse/lighthouse-mobile.png)

Note: Unfortunately, I didn't have any time left on this project to look into the issues properly. With more time i would investigate why the Performance scores are lower than i would like and also why the Accessibility score is low compared to previous projects. 

[Back to top ⇧](#filmzone)

### Issues fixed

#### Films page layout

On the Films page. I had an issue with the layout as films were being added. Big gaps appeared making the page look untidy. I spoke with a couple of other students on slack and with the help of my Mentor i fixed the issue using media queries in my custom styling file. I also applied some maxlenth attributes to the fields within the HTML file to restrict content. Before and after images below.

**Before**

![Image template](static/images/testing/issues/films_page/issue-films-page-1.png)

![Image template](static/images/testing/issues/films_page/issue-films-page-2.png)

![Image template](static/images/testing/issues/films_page/issue-films-page-3.png)

![Image template](static/images/testing/issues/films_page/issue-films-page-4.png)

**After**

![Image template](static/images/testing/issues/films_page/issue-films-page-fixed1.png)

![Image template](static/images/testing/issues/films_page/issue-films-page-fixed2.png)

![Image template](static/images/testing/issues/films_page/issue-films-page-fixed3.png)

![Image template](static/images/testing/issues/films_page/issue-films-page-fixed4.png)

![Image template](static/images/testing/issues/films_page/issue-films-page-fixed5.png)

![Image template](static/images/testing/issues/films_page/issue-films-page-fixed6.png)

![Image template](static/images/testing/issues/films_page/issue-films-page-fixed7.png)

[Back to top ⇧](#filmzone)

#### Modal issues

On the profile page and genres page theres a remove/delete button to remove a film or delete a genre type. I added defensive code using a modal from Materialize. It didn't work at first because there was no index.loop supporting the href and the id in the modal structure was connected to the modal-trigger properly. After some research using the Materialize website i was able to successfully use a Modal. This now allows users to confirm whether they want to remove/delete a film or genre type or cancel the request to remove/delete. 

![Image template](static/images/testing/issues/modals/modal-profile-page.png)

![Image template](static/images/testing/issues/modals/modal-genres-page.png)

[Back to top ⇧](#filmzone)

### Further testing

#### EmailJS

Screenshots below showing that the Contact Us page is fully working

**Contact us page completed**

![Image template](static/images/testing/emailjs/contact-us-completed.png)

**Contact us page submitted/Modal message**

![Image template](static/images/testing/emailjs/contact-us-submitted.png)

**Auto message sent to user**

![Image template](static/images/testing/emailjs/user-auto-reply.png)

**Message from user to FilmZone**

![Image template](static/images/testing/emailjs/message-from-user.png)

#### Mobile first
* I know it's important to build a new site as a mobile first application, therefore, during the design process and building the site I made sure that extensive testing was done on all mobile screen sizes using <a href="https://developer.chrome.com/docs/devtools/" target="_blank">Chrome development tools</a>. I worked with the following screen sizes making sure that all users can enjoy the site using any type of smartphone device: - 

    - 320px (iPhone 5 size)
    - 360px (Moto G4 and Galaxy S5) 
    - 375px (iPhone 6/7/8/X size)
    - 411px (Pixel 2/XL and iPhone 6/7/8 plus) 
        
[Back to top ⇧](#filmzone)

Return to my [README.md](README.md) to continue reading

### End of TESTING Document