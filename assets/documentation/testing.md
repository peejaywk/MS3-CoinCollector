## Test Strategy

To ensure the site is fit for purpose all user stories and features documented in the main README.md file are to be tested. The test procedures
and results are documented below.

The code (HTML/CSS/JS/Python) must also satisfy the requirements of the online validation tools. These are:
* [W3C Markup Validation Service](https://validator.w3.org/). Check the markup of web documents.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). Check Cascading Style Sheets
* [JS Lint](https://jslint.com/). Javascript code quality tool. 
* [PEP8 Online](http://pep8online.com/). Checks Python code for PEP8 compliance.

Google Lighthouse will be used to check the Peformance, Accessibility, Best Practices and Search Engine Optimisation of the website.

## User Story Testing
### New Users
* *"As a user, I want a clear layout so I can easily navigate the site on all platforms."*
    * The frontend of the website has been implemented using the [Materialize](https://materializecss.com/) framework. This provides all the tools
    required to implement a website that is responsive and works across all different platforms. All coins are presented to the user using Materialize
    cards which display a clear image of the coin and also allow the user the view more detailed information by using the card-reveal propertiy of the card.
* *"As a user, I would like the website to remember the coins in my collection so I don’t need to keep entering the data"*
    * The user must create an account on the website before they can start adding coins to their collection. This allows the website
    so store information about the users collection in the database so they can access it at any time and on any platform.
* *"As a user, I want to see all the coins in my collection"*
    * When a user logs in they are presented with a page showing all the coins in their collection. These are arranged using Materialize cards
    allowing the user to click each card to view information on each coin.
* *"As a user, I want to see all the coins that are missing from my collection so I know what I need to find/buy"*
    * This has been implemented using the wish list feature of the website. Users can add coins to their wish list to keep track of coins missing
    from their collections.
* *"As a user, I want to be able to add new coins to my collection as and when I find them"*
    * The user can add any coin from the 'coin_list' page to their collection by clicking on the 'Copy' button inside the card for that coin.
    See [image](images/add_coin.png) for details.
* *"As a user, when adding new coins to my collection I want the ability to select the coin from a pre-defined list"*
    * All the coins available in the database are available to the user via the 'coin_list' page. These are displayed 6 per page inside Materialize
    cards with pagination links at the bottom of the screen allowing the user to move between different pages. The caon list is also searchable using
    the search bar at the top of the screen.
* *"As a user, I want to be able to edit a coin entry in my database"*
    * Users can edit any coin in their collection by clicking on the 'Edit' button when viwing coins on the 'My Collection' page. This will open
    a modal window allowing the user to edit the details and to save the changes. These are shown in the following images ([Edit](images/user_edit_remove.png)
    & [Edit Modal](images/user_edit_modal.png))
* *"As a user, I want to be able to remove a coin from my collection and for it to move into my ‘missing’ list"*
    * Users can remove any coin from their collection by clicking on the 'Remove' button on the 'My Collection' page. However, the feature to have ability
    'missing list' has not been implemented as there is now a wish list for users to use. On clicking the 'Remove' button the user is prompted to confirm
    removal. These are shown in the following images ([Remove](images/user_edit_remove.png) & [Confirm](images/user_confirm_remove.png))
* *"As a user, I would like to view simple statistics about my collection such as percentage complete"*
    * This feature hasn't been implemented - will be added at a later date.
* *"As a user, I would like to add custom notes to any of the coin entries in my collection"*
    * When adding any coin to their collection users are prompted to enter a found date and any custom notes they would like associating with the coin.
    See [image](images/user_custom_notes.png) for details.
* *"As a user, I would like the ability to log the date when I found a coin"*
    * When adding any coin to their collection users are prompted to enter a found date and any custom notes they would like associating with the coin.
    See [image](images/user_custom_notes.png) for details.
* *"As a user, I want to be able to follow the website on social media to keep up to date on any changes to the website"*
    * Social media links are listed in the footer - these are visible on all pages.

### Returning Users
* *"As a returning user, I would like to be able to login to the site so I can easily see / update my collection"*
    * All coin user coin collections are stored in the backend database allowing users to log back into the site using the details they
    provided during registration.

### Website Owner
* *"As the owner, I want the ability to add new coins to the database"*
    * The owner/admin can add coins via the 'Add Coin' page. This page is only visible to users who have been granted administrator privileges. Navigating
    to the 'Add Coin' page displays a form for the admin to complete. See [image](images/admin_add_coin.png) for details.
* *"As the owner, I want the ability to edit coins and users in the database"*
    * The owner/admin can edit any coin via the 'Coin List' page by clicking on the 'Edit' button inside the card. This will take the admin/owner to
    a similar form used for adding coins but with all the data pre-populated ready for editting. 
    These are shown in the following images. ([Edit Button](images/admin_edit_delete.png) & [Edit Form](images/admin_edit_coin.png)).
* *"As the owner, I want the ability to delete coins and users in the database"*
    * The owner/admin can delete any coin via the 'Coin List' page by clicking on the 'Delete' button inside the card. This will open up a modal
    window prompting the user to confirm deletion of the coin from the database.
    These are shown in the following images. ([Delete Button](images/admin_edit_delete.png) & [Delete Modal](images/admin_delete_modal.png)).
* *"As the owner, I want the ability to give other users administrator privileges to help with maintaining the site"*
    * Currently the only way to give administrator privileges is to set *admin=True* in MongoDB for any users who need administrator access. 
* *"As the owner, I want to display data in a clear and informative way that works on any platform."*
    * The frontend of the website has been implemented using the [Materialize](https://materializecss.com/) framework. This provides all the tools
    required to implement a website that is responsive and works across all different platforms. All coins are presented to the user using Materialize
    cards which display a clear image of the coin and also allow the user the view more detailed information by using the card-reveal propertiy of the card.
* *"As the owner, I want the ability to expand the website in the future to add more coins to the database."*
    * The website uses [MongoDB](https://www.mongodb.com/) as the backend database which can manage large data structures far beyond the requirements of this project.
* *"As the owner, I want the website to be responsive in design and work across all devices from desktops to mobile phones."*
    * The frontend of the website has been implemented using the [Materialize](https://materializecss.com/) framework. This provides all the tools
    required to implement a website that is responsive and works across all different platforms from desktops to mobiles.

## Functional/Features Testing

### Test-001 : Responsive Design
Test responsiveness of website on different browsers.

1. Open Chrome browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/
2. Open the developer tools for the browser being used for these tests.
3. Navigate to the Register page using the nav bar or the button on the home page.
3. For screen sizes >992 pixels check that the form is rendered correctly (see [Register Form](images/Test001_register_form.png)) and that it scales correctly as the screen size increases.
4. For screen sizes <=992 pixels check that the form is rendered correctly (see [Register Form Mob](images/Test001_register_form_mob.png)).
5. Navigate to the Login page using the nav bar of the button on the home page.
6. Check that the form is rendered correctly across all screen sizes (see [Login Form](images/Test001_login_form.png)).
7. Navigate to the Contact Us page using the nav bar or the link in the footer.
8. For screen sizes >992 pixels check that the form is rendered correctly (see [Contact Form](images/Test001_contact_form.png)) and that it scales correctly as the screen size increases.
10. For screen sizes <=992 pixels check that the form is rendered correctly (see [Contact Form Mob](images/Test001_contact_form_mob.png)).
11. Login to the website with administrator privileges.
12. Navigate to the Coin List page using the link in the nav bar.
13. For screen sizes >1200 pixels check that the coin cards are rendered correctly (see [Coin List XL](images/Test001_coinlist_xl.png)).
14. For screen sizes >992 AND <=1200 pixels check that the coin cards are rendered correctly (see [Coin List L](images/Test001_coinlist_l.png)).
15. For screen sizes <=992 pixels check that the coin cards are rendered correctly (see [Coin List S](images/Test001_coinlist_s.png)).
16. Navigate to the Add Coin page using the link in the nav bar.
17. For screen sizes >992 pixels check that the form is rendered correctly (see [Add Coin Form](images/Test001_addcoin_form.png)).
18. For screen sizes <=992 pixels check that the form is rendered correctly (see [Add Coin Form Mob](images/Test001_addcoin_form_mob.png)).
19. Navigate to the Edit Coin page by clicking the Edit button on any coin displayed on the Coin List page.
20. For screen sizes >992 pixels check that the form is rendered correctly (see [Edit Coin Form](images/Test001_editcoin_form.png)).
21. For screen sizes <=992 pixels check that the form is rendered correctly (see [Edit Coin Form Mob](images/Test001_editcoin_form_mob.png)).
22. Logout of the website and log back in using a non administrator account.
23. Navigate to the My Collection page using the link in the nav bar.
24. For screen sizes >1200 pixels check that the coin cards are rendered correctly (see [My Collection XL](images/Test001_mycollection_xl.png)).
25. For screen sizes >992 AND <=1200 pixels check that the coin cards are rendered correctly (see [My Collection L](images/Test001_mycollection_l.png)).
26. For screen sizes <=992 pixels check that the coin cards are rendered correctly (see [My Collection S](images/Test001_mycollection_s.png)).
27. Navigate to the My Wishlist page using the link in the nav bar.
28. For screen sizes >1200 pixels check that the coin cards are rendered correctly (see [My Wishlist XL](images/Test001_mywishlist_xl.png)).
25. For screen sizes >992 AND <=1200 pixels check that the coin cards are rendered correctly (see [My Wishlist L](images/Test001_mywishlist_l.png)).
26. For screen sizes <=992 pixels check that the coin cards are rendered correctly (see [My Wishlist S](images/Test001_mywishlist_s.png)).
27. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.

#### Test Notes
All the forms / cards displayed correctly on all the browser listed above and at all screen sizes. The tests were also perofrmed on a Samsung Galaxy S8
using the Chrome and Opera browsers with no issues found. No testing has been performed on Apple mobiles or tablets due to lack of access to the devices.

#### Test Results
* **Chrome Browser: PASS**
* **Firefox Browser: PASS**
* **Opera Browser: PASS**
* **Edge Browser: PASS**
* **Safari Browser: PASS**

### Test-002 : Navigation Bar
Test navigation bar links function correctly and that the correct links are displayed for admin and non admin users.

1. Open Chrome browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/. Logout of the site if logged in.
2. Check that the nav bar is fixed to the top of the browser window when scrolling down.
3. With the user logged out check that the following menu options appear in the nav bar:
    * Coin Collector, Home, Login, Register & Contact Us
4. Click each menu option in turn and check that you are taken to the correct page.
5. Login as a regular non admin user and check that the following menu options appear in the nav bar:
    * Coin Collector, My Collection, My Wishlist, Coin List, Logout & Contact Us
6. Click each menu option in turn and check that you are taken to the correct page. Clicking the Logout option should log you out of the website.
7. Login in using an administrator account and check that the following options appear in the nav bar:
    * Coin Collector, Coin List, Add Coin, Logout & Contact Us
8. Click each menu option in turn and check that you are taken to the correct page. Clicking the Logout option should log you out of the website.
9. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
10. Repeat the above steps using a mobile device if possible.
11. Repeat the above tests with a screen size of <=992 pixles and check that all the menu options collapse into the hamburger icon. NOTE: The 
Coin Collector menu item should not form part of the hamburger menu and should remain located at the top left of the screen.

#### Test Notes
All the navigation links function correctly and link to the correct pages. For screen sizes <=992 pixels the navigation links
collapse into the hamburger menu and function correclty. The nav bar also remains fixed to the top of the page. 
    
Tests performed using  Chrome, Firefox, Opera, Edge & Safari desktop browsers.
Repeated tests using a Samsung Galaxy S8 mobile device with no issues.

#### Test Results
* **PASS**

### Test-003 : Footer
Test footer links function correctly and that the Materialize sticky footer is also functioning.

1. Open Chrome browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/.
2. Check that the footer remains at the bottom of the screen even when very little content is present.
3. Check that the footer scrolls down when more content is added to the page. May need to navigate to the Add Coin page to test this.
4. Click on the Contact Us link and conform that the Contact Us page is loaded.
5. Click on each social media link and verify it opens up the correct page in a new browser tab.
6. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
7. Repeat the above steps using a mobile device if possible.

#### Test Notes
The footer is located at the bottom of the screen when little content is present and scrolls down when more content is added. The Contact Us option
links to the correct page and all social media links are working and link to the correct pages, opening in a new tab.

Tests performed using  Chrome, Firefox, Opera, Edge & Safari desktop browsers.
Repeated tests using a Samsung Galaxy S8 mobile device with no issues.

#### Test Results
* **PASS**

### Test-004 : User Registration
Test the form validation functions correctly and that duplicate users are detected and reported back. Also check that the user is correctly added to 
the database.

1. Open browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/.
2. Click on the Register button or the Register option in the nav bar.
3. Check that the form validation is functioning correctly by entering a first name, last name, email and password that are invalid. Confirm that
the issue with a particular filed is reported back to the user.
4. Check that submitting an email that has been previously registered reloads the register page with the flash message "Email already registered.".
5. On successful registration confirm that the user is redirected back to their coin list page with the flash message "Registration successful!".
6. On successful registration confirm that the user entry has been added to the Users collection in MongoDB and that the admin flag has been set to the default of 'False'.

#### Test Notes

During testing of the form validation an error was found with the helper text over laying each other (see [image](images/Test004_register_error.png)).
To reslove this the helper text underneath the password input was moved into the input field (see [image](images/Test004_register_error_fix.png)).
    
[Change](https://github.com/peejaywk/MS3-CoinCollector/commit/5e90278460d7094a165d7048edf6f510e238e2a8) commited and all tests repeated on deployed site.

#### Test Result
* **PASS**

All the form validation functions correclty and reports back to the user any issues when invalid information is entered. On entering a duplicate email
address the correct flash message is displayed and the the user is redirected back to the registration page. On successful registration the correct flash
message is displayed on blank user coin page and the correct entry appears in the Users collection in MongoDB.

Tested using Google Chrome on Windows desktop.

### Test-005 : User Login
Test the form validation functions correctly and that any invalid data is reported back to the user. Check user is logged in and redirected to the 
correct page.

1. Open browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/.
2. Click on the Login button or the Login option in the nav bar.
3. Confirm that entering an invalid email or password is reported back to the user by the form validation.
4. Confirm that logging in with incorrect details results in a flash messaage being displayed at the top of the screen stating "Incorrect Username and/or Password".
5. On successful login confirm the user is redirected to their coin list page and that a welcome flash message is displayed.

#### Test Notes

All the form validation functions correclty and reports back to the user and issues with the email address or password. Entering invalid credentials
results in the correct flash message being displayed and the user returned to the login page. On successful login the user is redirected to their home
page listing the coins in their collection (if any) and with the welcome flash message at the top of the sceen.

#### Test Result
* **PASS**

### Test-006 : User Logout
Tests that a user is logged out of the site and cannot brute force their way to any pages by directly typing an a URL.

1. Open browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/.
2. Login to the website.
3. Logout of the website and confirm that the user is returned to the page displaying the welcome message.
4. Visit each of the URLs below and confirm that the user is redirected back to the login page:
    * http://coin-collector-ci-ms3.herokuapp.com/coin_list
    * http://coin-collector-ci-ms3.herokuapp.com/add_coin
    * http://coin-collector-ci-ms3.herokuapp.com/wishlist

#### Test Notes

On clicking the logout button the user is redirected to the page displaying the welcome message. On entering the URLs listed above directly into the
browsers address bar the user is redirected back to the login page with a flash message being displayed asking the user to login/register to access the site.

#### Test Result
* **PASS**

### Test-007: Copy Coin to User Collection
Test to confirm that a coin from the Coin List can be copied to a users collection with custom notes attached.

1. Open browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/.
2. Login to the website using a non admin account.
3. Navigate to the Coin List page using the link in the nav bar.
4. Select any coin from the list and click the Copy button - confrim that the copy modal appears with the correct coin information displayed.
5. Click on the date field and confirm the date selector modal appears. Select a date from the date selector.
6. Enter some custom notes in the notes field.
7. Click the Copy button to copy the coin entry with custom notes into your collection. Confirm flash message "Coin added to your collection" appears at the top of the screen.
8. Return to your collection by clicking on the My Collection link in the nav bar and confirm that the coin has been added the collection with the correct date and notes appearing in the card reveal.

#### Test Notes
Clicking on the Copy button opened up the modal window with the correct coin information displayed. The date selector functioned as expected allowing any date
from the past to be selected. All future dates are grayed out. Click the Copy button in the modal closed the window and the correct flash message was displayed at the top of the screen.
Confirmed that the coin had been added to the collection by visiting the My Collection page and checking the date and custom notes were correct.

#### Test Result
* **PASS**

### Test-008: Edit Coin in User Collection
Test to confirm that found date and custom notes can be editted for a coin in a users collection.

1. Open browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/.
2. Login to the website using a non admin account.
3. From 'Your Coin Collection' page click the Edit button to edit a coin entry in the collection.
4. Confirmm that the correct coin information is displayed in the modal window.
5. Confirm that clicking the Cancel button closes the modal without editting the coin in the collection.
6. Click the Edit button again and edit the Date Found and Notes, clicking Save when finished.
7. Confirm that the coin entry has been changed in the collection and that the flash message "Entry Successfully Updated" is diaplayed at the top of the page.

#### Test Notes
Clicking the Edit button opened up a modal window displaying the correct information for the coin. Clicking Cancel closed the modal window without editting
the coin in the collection. Clicking the Save button in the modal window closed the modal and changed the fields for that coin entry. The correct
flash message was displayed at the top of the screen.

#### Test Result
* **PASS**

### Test-009: Remove Coin from User Collection
Test to confirm that a coin can be removed from a users collection.

1. Open browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/.
2. Login to the website using a non admin account.
3. From 'Your Coin Collection' page click the Remove button to remove a coin from the collection.
4. Confirmm that the correct coin information is displayed in the modal window.
5. Confirm that clicking the Cancel button closes the modal without removing the coin from the collection.
6. Click Remove again to open the modal window and click the Confirm button in the modal window to remove the coin from the collection.
7. Confirm that the coin has been removed from the collection and that the flash message "Coin Deleted From Collection" is diaplayed at the top of the page.

#### Test Notes
Clicking the Remove button opened up a modal window displaying the correct information for the coin. Clicking Cancel closed the modal window without deleting
the coin from the collection. Clicking the Confirm button in the modal window closed the modal and deleted the coin from the collection. The correct
flash message was displayed at the top of the screen.

#### Test Result
* **PASS**

### Test-010:  Add Coin to Wishlist
Test to confirm that a coin from the Coin List can be added to a users wishlist.

1. Open browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/.
2. Login to the website using a non admin account.
3. Navigate to the Coin List page using the link in the nav bar.
4. Select any coin from the list and click the +Wishlist button. Confirm that the flash message "Coin added to your wishlist" is displayed at the top of the screen.
5. Navigate to the Wishlist page using the link in the nav bar.
6. Confirm that the coin appears in the wishlist.

#### Test Notes
Clicking the +Wishlist button for any coin results in the correct flash message being displayed at the top of the screen. The corresponding coin
is also added to the users wishlist.

#### Test Result
* **PASS**

### Test-011: Copy Coin from Wishlist to User Collection
Test to confirm that a coin can be copied from a users wishlist to their collection.

1. Open browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/.
2. Login to the website using a non admin account.
3. Navigate to the Wishlist page using the link in the nav bar.
4. Select any coin from the wishlist and click the Copy button - confrim that the copy modal appears with the correct coin information displayed.
5. Click on the date field and confirm the date selector modal appears. Select a date from the date selector.
6. Enter some custom notes in the notes field.
7. Click the Copy button to copy the coin entry with custom notes into your collection. Confirm flash message "Coin added to your collection" appears at the top of the screen.
8. Return to your collection by clicking on the My Collection link in the nav bar and confirm that the coin has been added the collection with the correct date and notes appearing in the card reveal.

#### Test Notes
Clicking on the Copy button opened up the modal window with the correct coin information displayed. The date selector functioned as expected allowing any date
from the past to be selected. All future dates are grayed out. Click the Copy button in the modal closed the window and the correct flash message was displayed at the top of the screen.
Confirmed that the coin had been added to the collection by visiting the My Collection page and checking the date and custom notes were correct.

#### Test Result
* **PASS**

### Test-012: Remove Coin from Wishlist
Test to confirm that a coin can be removed from a users wishlist.

1. Open browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/.
2. Login to the website using a non admin account.
3. Navigate to the Wishlist page using the link in the nav bar.
4. Click the Remove button to remove a coin from the wishlist.
5. Confirmm that the correct coin information is displayed in the modal window.
6. Confirm that clicking the Cancel button closes the modal without removing the coin from the wishlist.
7. Click Remove again to open the modal window and click the Confirm button in the modal window to remove the coin from the wishlist.
8. Confirm that the coin has been removed from the wishlist and that the flash message "Coin Removed From Wishlist" is diaplayed at the top of the page.

#### Test Notes
Clicking the Remove button opened up a modal window displaying the correct information for the coin. Clicking Cancel closed the modal window without deleting
the coin from the wishlist. Clicking the Confirm button in the modal window closed the modal and removed the coin from the wishlist. The correct
flash message was displayed at the top of the screen.

#### Test Result
* **PASS**

### Test-013: Add New Coin to Database
Test to confirm that a new coin can be added to the database.

1. Open browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/.
2. Login to the website using an administrator account.
3. Navigate to the Add Coin page using the link in the nav bar.
4. Complete all field on the form adding images for the obverse and reverse of the coin.
5. Confirm that the form validation is working for the required fileds (Denomination, Year, Issue, Description and Circulation).
6. On completion of the form click the Upload button. This will upload the text to Mongo and the images to an Amazon Bucket.
7. Confirm that the flash message "Coin added to database" is displayed at the top of the screen.
8. Navigate to the Coin List page using the link in the nav bar.
9. Confirm that the coin is visible in the list and that all the infomration and images are correct.

#### Test Notes
All form validation is working prompting the user to complete all required fields. On clicking the Upload button the correct flash message
is displayed at the top of the screen. The coin was successfully added to the Coin List page and all the text was correct. The images were
successfully downloaded from the Amazon Bucket and clearly rendered in the card.

#### Test Result
* **PASS**

### Test-014: Edit Coin in Database
Test to confirm that an existing coin in the database can be editted.

1. Open browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/.
2. Login to the website using an administrator account.
3. Navigate to the Coin List page using the link in the nav bar.
4. Click the Edit button for a coin and confirm the correct details are loaded into the edit coin form.
5. Edit the details for the coin and click upload when complete. Confirm that the flash messge "Coin Successfully Updated" is displayed at the top of the screen.
6. Return to the Coin List page and confirm that the details for the coin have been changed.

#### Test Notes
Clicking on the Edit button opened up a new page displaying the correct information for the coin selected for edit. The correct message was displayed at
the top of the screen after clicking the Upload button. The details of the coin had been updated when viewing the entry on the Coin List page.

#### Test Result
* **PASS**

### Test-015: Delete Coin from Database
Test to confirm that a coin can be deleted from the database and that it is also removed from a users collection and wishlist.

**NOTE:** Before starting this test please ensure the coin that is to be deleted from the database is part of a users collection & wishlist.

1. Open browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/.
2. Login to the website using an administrator account.
3. Navigate to the Coin List page using the link in the nav bar.
4. Click the Delete button on the coin you would like to delete from the database.
5. Confirm that the modal window contains the correct information for the coin selected for deletion.
6. Click the Cancel button and confirm that the window closes and that the coin has not been deleted from the database.
7. Click the Delete button again and this time click Confirm to delete the coin from the database.
8. Confirm that the coin has been deleted from the Coin List and that the flash message "Deleted, 1 instance(s) of the coin" is displayed at the top of the screen.
9. Logout of the administrator account and log back in using a non admin account.
10. Confirm that the deleted coin has been removed from users collection and wishlist.

#### Test Notes
Clicking the delete button opened up a modal window containing the correct information for the coin. Clicking the Cancel button closed the window
without deleting the coin from the database. Clicking the Confirm button in the modal window closed the window and the correct message appeared at the
top of the screen. Checking the Coin List page it was confirmed that the coin had been deleted from the database and was no longer displayed in the list.

Logged back in as a non-admin user and confirmed that the coin had been removed from the users collection. However, the coin had not been removed from the
wishlist as can be seen in this [image](images/Test015_coindelete_err.png). The page is displaying an empty card were the deleted coin was peviously.

Modified the app.py file to find all instances of the deleted coin in the wishlists collection and delete them. 
[Change](https://github.com/peejaywk/MS3-CoinCollector/commit/918b560490d1366ea1360ade4dcc858c1202b9aa) commited and all tests repeated on deployed site.

#### Test Results
* **PASS (after modification to app.py)**

### Test-016: Contact Us Form
Test to confirm the form validation is functioning correctly and that on completion of the form an email is sent to the websites email address containing
the details of the query.

1. Open browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/.
2. Login to the website using a non admin account.
3. Navigate to the Contact Us page using the link in the nav bar or footer.
4. Check the form validation is functioning correclty and it prompts you to complete all the required fields and enter a valid email address. The required fields are:
    * Name
    * Email Address
    * Subject
    * Message
5. Confirm that the flash message "Message Sent Successfully!" is displayed at the top of the screen after clicking the Send button and that the form is cleared.
6. Confirm that an email is sent to the websites email address containing the details of the contact form.

#### Test Notes
The form validation functioned correclty and prompted the user to complete all required fields with a valid email address. Clicking the Send button
cleared the form and displayed the correct message at the top of the screen.

The email was sent successfully to the websites email account. The submitted form can be seen [here](images/Test016_completed_form.png) and the received
email [here](images/Test016_email.png).

**NOTE:** The website does not send an acknowledgement email back to the user confirming receipt of the message. This could be added in the future.

#### Test Result
* **PASS**

### Test-017: 404 Error Page
Test to confirm that Flask captures and handles the 404 error (page not found).

1. Open browser and navigate to: http://coin-collector-ci-ms3.herokuapp.com/.
2. Enter invalid URL (https://coin-collector-ci-ms3.herokuapp.com/invalid_url) into the address bar.
3. Confirm that the 'Page Not Found' page is displayed as shown in [here](images/Test017_404).
4. Confimr tha clicking the link in the paragraph text returns the user to the Welcome screen if logged out and the user coin list if logged in.

#### Test Notes
On entering the invalid URL to correct page is displayed. Clicking the link in the paragraph text returns the user to the correct page when they are logged
in and logged out.

#### Test Result
* **PASS**

## Code Validation

### [PEP8 Online Check](http://pep8online.com/)
* One error reported with a line being too long. See report [here](images/PEP8-Online-Check.png).
    * This is a comment containing a URL so it was decided to leave it as a long line.

### [JS Hint](https://jshint.com/)
* Two warnings reported by JS Hint. See report [here](images/JSHint-Warnings.png).

### [Nu HTML Checker](https://validator.w3.org/nu/)
* Coin List Page
    * Errors reported for Duplicate IDs on the inputs 'date-found' and 'notes' in the Add Coin modal (see [here](images/HTML-DuplicateError.png)). 
    Modified the HTML and associated route in the app.py file to use unique IDs. Repeated the test and no errors found.
