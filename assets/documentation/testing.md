## Test Strategy

To ensure the site is fit for purpose all user stories and features documented in the main README.md file are to be tested. The test procedures
and results are documented below.

The code (HTML/CSS/JS/Python) must also satisfy the requirements of the online validation tools. These are:
* [W3C Markup Validation Service](https://validator.w3.org/). Check the markup of web documents.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). Check Cascading Style Sheets
* [JS Lint](https://jslint.com/). Javascript code quality tool. 
* [PEP8 Online](http://pep8online.com/). Checks Python code for PEP8 compliance.

Google Lighthouse will be used to check the Peformance, Accessibility, Best Practices and Search Engine Optimisation of the website.

### User Story Testing
#### New Users
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