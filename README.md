# drf-api-project5

Portfolio 5 project as part of the Diploma in Full Stack Software Development by Code Institute. This part of the project uses:
- Python+Django

___

This is the backend project for the Plan-et Continentally app, gives users the ability to leave reviews and has a link for them to purchase the book.



[Link to live site](https://drf-api-project-5-47dcc9e35444.herokuapp.com/)

[Link to front end site](https://plan-et-continentally-d407d6f9ae7a.herokuapp.com/)

## CONTENTS
- [drf-api-project5](#gauravs-book-reviews)
  - [CONTENTS](#contents)
  - [Site Objectives](#site-objectives)
- [User Stories](#user-stories)
  - [Visitor Goals](#visitor-goals)
- [Features](#features)
  - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Programming Languages, Frameworks and Libraries Used](#programming-languages-frameworks-and-libraries-used)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Github Deployment](#github-deployment)
  - [Cloning and Forking](#cloning-and-forking)
  - [Repository deployment via Heroku](#repository-deployment-via-heroku)
  - [Deployment of the app](#deployment-of-the-app)
- [Credits](#credits)
- [Acknowledgments and Thanks](#acknowledgments-and-thanks)

# Site Objectives
The goal of this site is to create a stable database structure, which will then be used in the front project. The site needs to allow a user to login, interact with other users and post their own trips.

My two main objectives were:

- ### Make use of available backend functionality

  The use of the backend framework allows users to create a profile, leave a review and/or edit any of the books on the site (with authorisation), as well as deleting their own comments should they wish to.

- ### Store data on an external cloud database

  I used a PostgreSQL database for this project.

# User Stories
The user stories are documented in the front end repository, [Link Here](https://github.com/users/gauravjagpal/projects/3)

## Visitor Goals

- When not logged in, view all posts/filter down
- When logged in, visit all posts/filter down.
- Create Posts
- Create a trip
- View own trips
- Favourite a post
- Comment on a post
___

# Features

## Future Features
- Add functionality for users to plan trips with each other
- Add more data options, such as Continent or City.

# Technologies Used

Here are the technologies used to build this project:

- [Github](https://github.com) To host and store the data for the site.
- [Gitpod](https://gitpod.io/workspaces), the IDE where the site was built.
- [PEP8 Validator](https://pep8ci.herokuapp.com/) Used to check python code for errors
- [PostgresSQL](https://dbs.ci-dbs.net/) Used to store PostgreSQL database.
- [Cloudinary](https://cloudinary.com/) Used as cloud storage for images uploaded as part of the blog posts
- [Heroku](https://id.heroku.com/) Used to deploy the project

# Programming Languages, Frameworks and Libraries Used
## Programming Languages
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Django](https://www.djangoproject.com/)

## Libraries
- Addtional libraries that were used are the django-countries library

# Testing

- [Testing file](TESTING.md)

# Deployment

## Github Deployment

The website was stored using GitHub for storage of data and version control. To do this I did the following;

After each addition, change or removal of code, in the terminal within your IDE (I used Gitpod for this project) type:

- git add .
- git commit -m "meaningful commit message"
- git push

The files are now available to view within my github repository.

To bring all models up to date I regularly needed to run:
- python3 manage.py makemigrations
- python3 manage.py migrate

Whenever I made changes to my CSS or JavaScript files I needed to run:
- python3 manage.py collectstatic

## Cloning and Forking
### How to Clone

To clone the repository:

1. Login (or signup) to Github.
2. Go to my repository for the project, [drf-api-project5](https://github.com/gauravjagpal/drf-api-project5).
3. Click on the green 'Code' button. Choose whether you would like to clone with HTTPS, SSH, or GitHub CLI, and copy the link shown.
4. Launch the terminal within your code editor and set the current working directory to the desired location for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

### How to Fork

To fork the repository:

1. Login (or signup) to Github.
2. Go to my repository for the project, [drf-api-project5](https://github.com/gauravjagpal/drf-api-project5).
3. Click the Fork button in the top right corner.


### Repository deployment via Heroku

- On the [Heroku Dashboard](https://dashboard.heroku.com) page, click New and then select Create New App from the drop-down menu.
- When the next page loads insert the App name and Choose a region. Then click 'Create app'
- In the settings tab click on Reveal Config Vars and add the key Port and the value 8000. The credentials for this app were:

1. Cloudinary URL
2. Database URL
3. SECRET_KEY

- Below this click Add buildpack and choose python.

### Deployment of the app

- Click on the Deploy tab and select Github-Connect to Github.
- Enter the repository name and click Search.
- Choose the repository that holds the correct files and click Connect.
- A choice is offered between manual or automatic deployment whereby the app is updated when changes are pushed to GitHub. Select automatic (when testing you can also choose to do a manual refresh to speed things up)
- Once the deployment method has been chosen the app will be built and can be launched by clicking the Open app button which will either appear below the build information window or in the top right of the page.

___

## Credits

This project was based on the Code Institute's - drf-api setup. I used this template and manipulated it do add features relevant to my project.

When running into blockers I often referred to Stack Overflow for inspiration

___

## Acknowledgments and Thanks

Massive thanks to the team at Code Institute for helping me learn to debug issues independently.