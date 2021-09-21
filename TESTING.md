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
        * [Homepage tested](#homepage-tested)
        * [Tournament page tested](#tournament-page-tested) 
        * [Quiz page tested](#quiz-page-tested)
        * [Feedback page tested](#feedback-page-tested)
        * [Answers page tested](#answers-page-tested)
    * [W3C CSS Validation Service](#w3c-css-validation-service)
        * [CSS coding tested](#css-coding-tested)
    * [JS Hint Javascript code validator](#js-hint-javascript-code-validator)
        * [Maps.js](#maps.js)
        * [Quiz.js](#quiz.js)
        * [sendEmail.js](#sendemail.js)
    * [Web Browsers](#web-browsers)
        * [Google Chrome](#google-chrome)
        * [Apple Safari](#apple-safari)
        * [Microsoft Edge](#microsoft-edge)
        * [Mozilla Firefox](#mozilla-firefox)
    * [Testing responsiveness](#testing-responsiveness)
        * [Mobile screenshots](#mobile-screenshots)
        * [Tablet screenshots](#tablet-screenshots)
        * [Desktop screenshots](#desktop-screenshots)
        * [Large Desktop screenshots](#large-desktop-screenshots)
    * [Lighthouse testing](#lighthouse-testing)
        * [Desktop results](#desktop-results)
        * [Mobile results](#mobile-results)
    * [Issues found](#issues-found)
        * [API key](#api-key)
        * [Quiz images](#quiz-images)
        * [Feedback form](#feedback-form)
        * [Modal issues](#modal-issues)
        * [EmailJS](#emailjs)
    * [Further testing](#further-testing)
        * [Mobile first](#mobile-first)
        * [External links](#external-links)
        * [Internal links](#internal-links)
    * [Bugs outstanding](#bugs-outstanding)

Return to my [README.md](README.md) 

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

#### **Story 6**
- Due to a News Report a Film Actor has been discredited and therefore all Films associated to this Actor needs to be removed from the Internet. 

#### **Story 7**
- I've just come out of the cinema after watching a great film. I'm keen to add this to my FilmZone profile but I'm not going to be at my computer until tomorrow morning now. 