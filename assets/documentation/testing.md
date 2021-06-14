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

Test-001
Responsive Design - Test responsiveness of website on different browsers

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

    * **Test Results (Chrome Browser): PASS**
    * **Test Results (Firefox Browser): PASS**
    * **Test Results (Opera Browser): PASS**
    * **Test Results (Edge Browser): PASS**
    * **Test Results (Safari Browser): PASS**

All the forms / cards displayed correctly on all the browser listed above and at all screen sizes. The tests were also perofrmed on a Samsung Galaxy S8
using the Chrome and Opera browsers with no issues found. No testing has been performed on Apple mobiles or tablets due to lack of access to the devices.