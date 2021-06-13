# Coin Collector
Coin Collector is a website for people who collect coins that are in everyday circulation within the UK. These could be coins found from the change in your 
pocket to coins traded / purchased on online auction sites. The site maintains a database of coins currently in circulation within the UK and allows the user 
to record what coins they have in their collection. Users can be granted admin access if they would like to contribute / add coins to the database.

*NOTE: The initial release of the website will focus on the UK fifty pence piece and two pound coin as these are the most popular coins for collectors as 
they have had many variations on design over the years.*

The main aims of the website are:
* Allow users to record coins they have collected and coins on their wish list
* Maintain a database of coins currently in circulation within the UK
* Display statistics on a user’s collection
* Be responsive so the website works across all devices / screen sizes


## Table of Contents

[User Experience (UX)](#userexperience)

[Database Design](#database)

[Features](#features)

[Technologies Used](#technologies)

[Testing](#testing)

[Bugs/Issues](#bug)

[Deployment](#deployment)

[Credits](#credits)

<a name="userexperience"></a>
## User Experience (UX)

### User Stories
#### New Users
* As a user, I want a clear layout so I can easily navigate the site on all platforms.
* As a user, I would like the website to remember the coins in my collection so I don’t need to keep entering the data
* As a user, I want to see all the coins in my collection
* As a user, I want to see all the coins that are missing from my collection so I know what I need to find/buy
* As a user, I want to be able to add new coins to my collection as and when I find them
* As a user, when adding new coins to my collection I want the ability to select the coin from a pre-defined list
* As a user, I want to be able to edit a coin entry in my database
* As a user, I want to be able to remove a coin from my collection and for it to move into my ‘missing’ list
* As a user, I would like to view simple statistics about my collection such as percentage complete
* As a user, I would like to add custom notes to any of the coin entries in my collection
* As a user, I would like the ability to log the date when I found a coin
* As a user, I want to be able to follow the website on social media to keep up to date on any changes to the website
#### Returning Users
* As a returning user, I would like to be able to login to the site so I can easily see / update my collection
#### Website Owner
* As the owner, I want the ability to add new coins to the database
* As the owner, I want the ability to edit coins and users in the database
* As the owner, I want the ability to delete coins and users in the database
* As the owner, I want the ability to give other users administrator privileges to help with maintaining the site
* As the owner, I want to display data in a clear and informative way that works on any platform.
* As the owner, I want the ability to expand the website in the future to add more coins to the database.
* As the owner, I want the website to be responsive in design and work across all devices from desktops to mobile phones.

### Wireframe Mockups

The website is split into several pages allowing the user to manage/view their coin collection and allowing administrators to add/edit coins. 
Initial design ideas were captured using [Balsamiq](https://balsamiq.com/) - these are linked below:

* [Home Page - Logged Out](/assets/wireframes/001-HomePage-LoggedOut-v1.png)
* [Home Page - Logged In](/assets/wireframes/002-HomePage-LoggedIn-v2.png)
* [Want List Page](/assets/wireframes/003-WantList-v2.png)
* [Add/Edit Coin Page](/assets/wireframes/004-Add_EditCoinPage-v1.png)
* [Admin Page](/assets/wireframes/005-AdminPage-v2.png)
* [Admin Add/Edit Coin](/assets/wireframes/006-Admin-Add_EditCoin-v1.png)
* [Contact Us Page](/assets/wireframes/007-ContactPage-v1.png)

<a name="database"></a>
## Database Design

The website uses [MongoDB](https://www.mongodb.com/) as the backend database. The database for this site consists of five collections. The relationships between these collections
are documented in the tables below and also illustrated graphically in the pdf diagram linked below. The design of the database went through several itterations and these can be 
found in the /assets/documetation folder of the repository.

* [Database Diagram (pdf)](/assets/documentation/DatabaseStructurev4.pdf)

### Users Collection
The users collection is used to record the details of registered users and if they have been granted administrator privileges.
Key | Data Type | Description
----|-----------|------------
_id | ObjectId | ObjectID auto-generated by Mongo
fname | String | Users first name
lname | String | Users last name
email | String | Users email address
password | String | Users hashed password
admin | Boolean | Indicates if a user has administrator privileges

### Circulation Collection
Each document in the circulation collection contains the details of a unique coin that has been issed by the Royal Mint. This can be a coin in general circulation
of a coin issued for commemerative purposes only. 
Key | Data Type | Description
----|-----------|------------
_id | ObjectId | ObjectID auto-generated by Mongo
denomination | String | Coin denomination
year | String | Year the coin was issued
issue | String | Information of the coin issue (short description)
description | String | Detailed description of the coin
circulation | String | Is the coin in general circluation (Yes/No)
edge | String | Edge inscription text
mintage | String | Coin mintage figure (if known)
material | String | Coin composition
thickness | String | Coin thickness
weight | String | Coin weight
diameter | String | Coin diameter
obverse_designer | String | Designer of the obverse side of the coin
reverse_designer | String | Designer of the reverse side of the coin
obverse_image | String | URL to the obverse image of the coin
reverse_image | String | URL to the reverse image of the coin
date_added | String | Date coin was added to the database
date_edited | String | Date coin entry was last editted

### Coins Collection
The coins collection contains information for all coins that users have recorded as being in their collections. Each document references the ObjectId of the 
user and ObjectId of the coin and allows the user to store personal notes and log the date the coin was found.
Key | Data Type | Description
----|-----------|------------
_id | ObjectId | ObjectID auto-generated by Mongo
user_id | ObjectId | References an ObjectId in the Users Collection
coin_id | ObjectId | References an ObjectId in the Circulations Collection
date_found | String | Date the coin was found
notes | String | User notes

### Wishlists Collection
The wishlists collection stores infomration of all coins that users have added to their wish lists. Each document references the ObjectId of the 
user and ObjectId of the coin.
Key | Data Type | Description
----|-----------|------------
_id | ObjectId | ObjectID auto-generated by Mongo
user_id | ObjectId | References an ObjectId in the Users Collection
coin_id | ObjectId | References an ObjectId in the Circulations Collection

### Denominations Collection
This collection wa added during development of the website and is only used to store the arguments to populate the drop down menu used in the add_coin page. This
collection records the current coin denominations that the website supports (during development this is the Fifty Pence Piece and Two Pound Coin).
Key | Data Type | Description
----|-----------|------------
_id | ObjectId | ObjectID auto-generated by Mongo
name | String | Name of the coin denomination (eg. Fifty Pence)

<a name="features"></a>
## Features

### Common Features Across All pages
* Header
    * The header will be in a fixed position at the top of the screen and will not scroll with the page contents. This allows visitors easy access to navigate the site via the menu.
    * The header will include links to all the site pages. These will be aligned to the right hand side of the page.
    * On hovering over the navigation links with the mouse they will change colour indicating to the user that they are clickable (desktop only).
    * On mobile devices the navigation links will collapse into a burger menu.
    * The site logo will be positioned to the left of the page and when clicked will take the user back to the home page.
    * The navigation links will change when the user logs into the site. There will also be additional navigation items for users who have administrator privileges.
* Footer
    * The footer will be located at the bottom of each page and will scroll with the page contents.
    * A disclaimer will be positioned in the footer stating that this website is for educational purposes only.
    * Social media links and other contact information will be positioned to the right of the footer.
    * Social media links will be represented by icons for each site and will increase when the user hovers over them.
    * There will be a contact link at the bottom of the page that will take the user to the contact page/form.

### Individual Page Features
* Home Page - Logged Out
    * When visiting the website for the first time, or the user is logged out, the Home Page will display a welcome message informing the user of the purpose of the site and how to proceed
    * Under the welcome message will be two buttons: one for new users to register and one for existing users to login
    * The user can also login/register using the links in the navigation bar.
* Home Page - Logged In
    * When logged in the Home Page will display a list of coins that are currently in the users collection
    * The page will display a table for each denomination of coin
    * For each entry in the table the user will be able to edit or delete that entry using the buttons at the end of the row.
    * For more information on a particular coin the user can click on that entry - a modal window will display additional information for that coin.
    * The user can add coins to their collection by clicking on the 'Add Coin' button at the top of the page
* Want List Page
    * The Want List Page will display a list of all coins currently missing from the users collection. 
    * The page will display a table for each denomination of coin
    * For each entry there will be a button to add the coin to the users collection. 
    * For more information on a particular coin the user can click on that entry - a modal window will display additional information for that coin.
* Add/Edit Coin Page
    * The Add/Edit Page allows the user to add a coin to their collection
    * A series of drop down boxes allow the user to select the coin they wish to add from the database
    * A 'date found' can be added to the entry by the user if desired.
    * Custom Notes can also be added to the entry.
    * The form will be validated once the Save button has been clicked and if successful the data will be submitted to the database. The user will be returned to the Home Page on completeion.
    * To cancel the entry a Cancel button is provided. This will redirect the user back to the Home Page
* Admin Page (see note below)
    * The Admin Page will list all of the coins currently in the database
    * The page will display a table for each denomination of coin
    * For each entry in the table the admin user will be able to edit or delete that entry using the buttons at the end of the row.
    * The admin user can add coins to the database by clicking on the 'Add New Coin To Database' button at the top of the page
* Admin Add/Edit Coin Database Page
    * The Admin Add/Edit Page allows the admin user to add a coin to the database
    * The series of drop down boxes and text boxes are used to complete the entry for the coin
    * An image of the coin can be associated with the entry
    * The form will be validated once the Save button has been clicked and if successful the data will be submitted to the database. The user will be returned to the Admin Add/Edit Page on completeion.
    * To cancel the entry a Cancel button is provided. This will redirect the user back to the Admin Add/Edit Page
* Contact Page
    * At the top of the page will be some instructions of how to contact the website. This will be via the form displayed on the page or via the email link provided.
    * The contact form will be below the text and will ask for the users contact details and a description of their enquiry.
    * Below the form will be a submit button.
    * This page can be accessed by clicking on the 'Contact' link in the footer or header.

NOTE: It was decided to remove the dedicated admin page as other pages could be reused but with different buttons being rendered for when an administrator is logged in.

### Frontend Design
The [Materialize](https://materializecss.com/) framework was used to implement the frontend of the website to give a responsive design that provides a good UX across all
devices and screen sizes.

### User Registration/Authentication
To use the website users must register an account providing their name, email address and password. The password is hashed before being written to the database. To login the 
user must enter their email address and password.
NOTE: If a user requires administrator access this must be granted by the website owner.

### Database Interactions
* Regular users can view/search all the coins in the database.
* Regular users can select a coin to add to their collection with custom notes and a 'found' date.
* Regular users can edit any coin in their collection to modify the custom notes or 'found' date.
* Regular users can remove a coin from their collection.
* Regular users can select a coin to be added to their wish list.
* Regular usres can remove a coin from their wishlist.
* Admin users can view/search all the coins in the database.
* Admin users can add a new coin to the database.
* Admin users can edit a coin in the database.
* Admin users can delete a coin from the database.

### Colour Palette
A dark theme was chosen for the website to complement the bright silver/gold colours of the coins that will be displayed. All buttons on the site use the built-in colour
classes provided by Mterialize. The custom colours used to style the rest of the site are detailed below:

* ![#101E30](https://via.placeholder.com/15/101E30/000000?text=+) #101E30
    * Background
    * Modal Background
* ![#DDDDDD](https://via.placeholder.com/15/dddddd/000000?text=+) #DDDDDD
    * Paragraph Text
    * Nav Links
    * Table Text
* ![#4078C0](https://via.placeholder.com/15/4078C0/000000?text=+) #4078C0       
    * Headings
    * Nav Background
    * Footer Background
    * Card Reveal
* Buttons use the built in Materialize colours

<a name="technologies"></a>

## Technologies Used

* This website uses HTML, CSS, JavaScript & Python programming languages.
* [Materialize 1.0.0](https://materializecss.com/). Responsive front-end framework.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/). Lightweight web application framework.
* [Heroku](https://www.heroku.com/). Heroku is used as the deployment platform for the website.
* [MongoDB](https://www.mongodb.com/). Non-relational database.
* [GitPod](https://gitpod.io/) was use as the development environment.
* [GitHub](https://github.com/) was used for configuration control and to host the website.
* [Font Awesome](https://fontawesome.com/) provided the social media icons and the icons for the concerts and set list sections.
* [Googel Fonts](https://fonts.google.com/) provided the Roboto font that is used throughout this website.
* [jQuery](https://jquery.com/). JavaScript library.
* [Colorate](https://colorate.azurewebsites.net/). Colour scheme design website.
* [JS Lint](https://jslint.com/). Javascript code quality tool.
* Amazon AWS

<a name="testing"></a>
## Testing

See [testing.md](/assets/documentation/testing.md) for the testing documentation.


Setting up GitPod environment
Install Flask
pip3 install Flask

Install pymongo to allow Flask to communication with our Mongo database
pip3 install flask-pymongo

Install dnspython so the Mongo SRV connection string can be used
pip3 install dnspython

Heroku Deployment
Create a list of applications and dependencies required to run our website.
pip3 freeze --local > requirements.txt

Create Procfile so Heroku knows how to run the application
echo web: python app.py > Procfile

Install boto3 AWS SDK
pip3 install boto3



Bugs

Chrome autofill changes the background to a different colour on the coin add form. A solution implemented in the CSS file was found here.
https://stackoverflow.com/questions/2781549/removing-input-background-colour-for-chrome-autocomplete

Pagination links not working when searching for an item. 
In the app.py file was using 'query = request.form.get("query")' to get the search query retruned a null search string when the pagination link was pressed
to move to the next window. Fixed this by changing the line of code to 'query = request.args.get("query")' to get the value via the arguments. This passed 
in the correct search term.

<a name="credits"></a>
## Credits

* [Karim Cheurfi Blog - Amazon S3 File Upload](https://www.zabana.me/notes/flask-tutorial-upload-files-amazon-s3) - How to use Flask to upload files to Amazon S3
* [British Fifty Pence 2015 Obverse](https://en.wikipedia.org/w/index.php?curid=45261115)
* [Flask Pagination - Stackoverflow](https://stackoverflow.com/questions/66734992/flask-paginate-per-page-not-changing-the-amount-of-visible-items)
* [Flask Pagination - GitHub](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9)
* [Flask User Authentication](https://github.com/MiroslavSvec/DCD_lead/blob/user-auth/app.py) - Example code to register/authenticate a user using Flask.
* [Flask-Mail Setup](https://code-institute-room.slack.com/archives/C7JQY2RHC/p1611678109168400) - Slack post by Karina on how to setup Flask-Mail
* [Flask Referrer](https://code-institute-room.slack.com/archives/C7JQY2RHC/p1623169621486800) - BenKav_lead assistance in helping with redirecting users back to the page they came from