#TimeToCook
<h1 align="center">TimeToCook</h1>

[View the live project here](https://timetocook-7eed92e3f20e.herokuapp.com/)

TimeToCook is a place where you can find and add recipes. You can also save your favorite ones for easy access. Users can easily browse through list of recipes, each detailed with ingredients, step-by-step cooking instructions, preparation time, and user-submitted ratings to help you choose the best dish for any occasion.

![Mockup](documentation/responsive.png)

## Index – Table of Contents
- [Index – Table of Contents](#index--table-of-contents)
- [User Experience (UX)](#user-experience-ux)
- [Features](#features)
- [Design](#design)
- [Technologies Used](#technologies-used)

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
- ### Add Recipes
- ####
  The ‘Add Recipes’ page is accessible after the user has logged in. It features an easy-to-use form that guides you through entering details such as the recipe’s title, ingredients, instructions, rating, and photo link for the recipe
    ![Mockup](documentation/features/addrecipes.png)
- ### Manage User
  - #### 
    The ‘Manage Users’ page is only accessible to the website administrator. The admin can restrict access for users, and when a user tries to log in, a message is displayed that their account has been disabled.
    ![Mockup](documentation/features/adminuser.png)
## Design
  - ### Color scheme
    As part of designing the site I decided to use purple, yellow and red as main colours. The pallete has been generated using [coolors.co](https://coolors.co/)
    ![Mockup](documentation/design/colors.png)
  - ### Typography
    Google Fonts were used to import Roboto into style.css
- ## Wireframes 
   - ## Home Page <br>
     [Home page desktop](documentation/wireframes/IndexDesktop.png)<br>
     [Home page mobile](documentation//wireframes/IndexMobile.png)
   - ## Favourites
     [Favourite Desktop](documentation/wireframes/FavouritesDekstop.png)<br>
     [Favourite Mobile](documentation/wireframes/FavouritesMobile.png)
   - ## My Recipes
     [My Recipes Dekstop](documentation/wireframes/MyRecipesDekstop.png)<br>
     [My Recipes Mobile](documentation//wireframes/MyRecipesMobile.png)
   - ## Categories
     [Categories Desktop](documentation/wireframes/CategoriesDesktop.png)<br>
     [Categories Mobile](documentation//wireframes/CategoriesMobile.png)
   - ## Edit Categories
     [Edit Categories Desktop](documentation/wireframes/CategoriesDesktop.png)<br>
     [Edit Categories Mobile](documentation//wireframes/CategoriesMobile.png)
   - ## All Recipes
     [All Recipes Desktop](documentation/wireframes/AllrecipesDesktop.png)<br>
     [All Recipes Mobile](documentation//wireframes/AllRecipesMobile.png)
   - ## Add Recipes
     [Add Recipes Desktop](documentation/wireframes/AddRecipeDesktop.png)<br>
     [Add Recipes Mobile](documentation//wireframes/AddRecipeMobile.png)
   - ## Manage Users
     [Manage Users Desktop](documentation/wireframes/ManageUsersDesktop.png)<br>
     [Manage Users Mobile](documentation//wireframes/ManageUsersMobile.png)
   - ## Register
     [Register Desktop](documentation/wireframes/RegisterDekstop.png)<br>
     [Register Mobile](documentation//wireframes/RegisterMobile.png)
   - ## Log In
     [Log In Desktop](documentation/wireframes/LogInDesktop.png)<br>
     [Log In Mobile](documentation//wireframes/LogInMobile.png)
   - ## View Recipe
     [View Recipe Desktop](documentation/wireframes/ViewRecipeDekstop.png)<br>
     [View Recipe Mobile](documentation//wireframes/ViewRecipeMobile.png)
## Technologies Used
  - ### Languages Used
    -   [HTML5](https://en.wikipedia.org/wiki/HTML5)
    -   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    -   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    -   [Python](https://www.python.org/)
   
  - ### Frameworks, Libraries and Programs Used
    -   [Google Fonts:](https://fonts.google.com/) was used to import the 'Roboto' font into the style.css file 
    -   [Git:](https://git-scm.com/) was used for version control by utilising VSCode terminal to commit to Git and Push to GitHub.
    -   [GitHub:](https://github.com/) was used as the repository for the projects code after being pushed from Git.
    -   [Visual Studio Code](https://code.visualstudio.com/) was used as IDE editor.
    -   [Balsamiq:](https://balsamiq.com/) was used to create the wireframes.
    -   [Flask:](https://flask.palletsprojects.com/en/3.0.x/) Micro web framework written in Python.
    -   [ElephantSQL:](https://www.elephantsql.com/) PostgreSQL database hosting service for hosting website database.
    -   [Materializecss:](https://materializecss.com/) For making the website responsive.
  