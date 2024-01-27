#TimeToCook
<h1 align="center">TimeToCook</h1>

[View the live project here](https://timetocook-7eed92e3f20e.herokuapp.com/)

TimeToCook is a place where you can find and add recipes. You can also save your favorite ones for easy access. Users can easily browse through list of recipes, each detailed with ingredients, step-by-step cooking instructions, preparation time, and user-submitted ratings to help you choose the best dish for any occasion.

![Mockup](documentation/responsive.png)

## Index – Table of Contents
- [Index – Table of Contents](#index--table-of-contents)
- [User Experience (UX)](#user-experience-ux)
- [Features](#features)

## User Experience (UX)

- ### User stories
  - #### A. First Time Visitor
    1. As a first time visitor, I want to see the most rated recipes.
    2. As a first time visitor, I want to be able to register on website.
    3. As a first time visitor, I want to be able to view recipe categories.
    4. As a first time visitor, I want to easily see website's features.
  - #### B. Returning Visitor 
    1. As a returning visitor, I want to be able to log in to the website.
    2. As a returning visitor, I want to be able to add a recipe.
    3. As a returning visitor, I want to be able to edit my recipes.
    4. As a returning visitor, I want to be able to search through all the recipes.
    5. As a returning visitor, I want to be able to change my password.
    6. As a returning visitor, I want to be able to add recipes to favourite.
  - #### C. Administrator
    1. As a administrator, I want to be able to manage categories.
    2. As a administrator, I want to be able to restric access to users.
   
## Features

 - ### NavBar
   - #### 
     The navigation bar allows users to quickly find recipes, save them to favorites, and access login and signup options. The account navigation button features a dropdown menu that displays certain pages only when the user is logged in.
    ![Mockup](documentation/features/navbar.png)
   - #### 
     When the user is not logged in
     ![Mockup](documentation/features/navbar-notloggedin.png)
   - ####
     Once the user is logged in, their username will be displayed in the dropdown menu. Pages such as ‘Profile’, ‘Add Recipes’, ‘My Recipes’, and ‘Log Out’ will be visible.
     ![Mockup](documentation/features/navbar-loggedin.png)
- ### Index Page
  - #### 
    The index page consists of three card panels, each simply explaining the main features of the website.
    ![Mockup](documentation/features/indexcardpanels.png)
  - ####
    The index page features the top-rated recipes submitted by users. Only recipes with a rating of 4 or higher are shown, the picture and a short description of the recipe are displayed, including who added the recipe, its rating, difficulty, and category.
    ![Mockup](documentation/features/indexmostrated.png)
- ### Footer
  - #### 
    This footer text gives a brief overview of what TimeToCook website offers, links to the social platform and invites users to engage with the content.
    ![Mockup](documentation/features/footer.png)
- ### Favourites page
  - #### 
    Users can save recipes by adding them to their favourites. They need to be logged in to be able to add recipes to their favourites.
    ![Mockup](documentation/features/favourites.png)
    ![Mockup](documentation/features/favouritelogin.png)
- ### Categories
  - #### 
    The website is intuitively organized into categories to ensure you can find the perfect recipe with ease. The categories can be only added, deleted or edited by admins.
    ![Mockup](documentation/features/categorieslogin.png)
    ![Mockup](documentation/features/categories.png)
- ### All recipes
  - #### 
    The 'All Recipes' page provides users with a comprehensive view of all the recipes published on the website. The search function is a tool provided to make the recipes on the website easily discoverable.
    ![Mockup](documentation/features/allrecipes.png)
- ### Register
  - ####  
    The registration feature on website is a simple and secure way for new users to create their own accounts, which enables them to add recipes, edit and save to favourite. Users are asked to confirm their password to avoid mistyping it.
    ![Mockup](documentation/features/registration.png)
- ### Log In
  - #### 
    When the user is logged in an  message is shown to confirm.
    ![Mockup](documentation/features/login.png)
    ![Mockup](documentation/features/loginmessage.png)
  - ####
    In case the username/password is incorrect or the user has been banned, a message is displayed.
    ![Mockup](documentation/features/loginbanned.png)
    ![Mockup](documentation/features/loginvalid.png)


- ### My Recipes
  - #### 
    My recipe page has been designed to help users keep a record of their own recipes that they have added.
    ![Mockup](documentation/features/myrecipes.png)
