# Vegan recipes
#### Video Demo:  https://youtu.be/cKYtidB7kj0
#### Description:
    This is web site which is aggregator of vegan video recipes. It has search bar, which could help to find a recipe by title or ingredient. You can sort recipe by category. You can open any recipe and watch it. The ingredients, that are used you can see in the right side. If recipe has recommendations then you can see it under video. The link to the author you can see in the bottom. If you like this author you can open his other recipes on my site. Also you can sign up in the site to add any recipe to your favorites. Then you can remove any recipe from your favorites.
    
#### Technologies and frameworks:    
    I have used Python (Flask, SQLAlchemy), HTML, CSS (Bootstrap), SQLite.  
    I have created 3 tables in my database: users, recipes and user-recipes. Table users has 3 columns: id, email, pas. Table recipes has 8 columns: id, title, ref, ingridients, recipe, ref_pic, category, author. Table user-recipes has 2 columns: recipe_id, user_id. The user-recipes table used the many-to-many relationships. 
    
#### What was a hardest part:       
    *The hardest part was populating the database. I did it by hand and have contributed 200 recipes so far. 
    *It was difficult to make a search bar, because sqlAlchemy "ilike" function does not support Cyrillic.

#### Folders and files:  
    *The mail file is app.py in folder "final project". This is the main application module, where the main settings are defined and extensions are registered, it also implements the web server.  
    *Folder static — css.  
    *Folder templates - html templates. I have created 11 html files.  
    
#### Dynamic templates:      
    Every recipe is open by tamplate reciept.html by adding dynamic id number. Also user profile is open by template profile.html by adding dynamic user email.

#### User registration: 
    *The application could check email already exist in database or not. 
    If user submit form without any email, application will return error: "Empry email."   
    *If user submit form without any password, application will return error: "Empry password."  
    *If user submit form with different passwods, application will return error: "Passwords are different." 

#### Page not found: 
    If user will write non-existent url then application will return template page404.html where will be text and link: "Page not found, return homepage".

#### My plans to the nearest future: 
    *I will check the length of password during registration. The minimum length need to be 6 simbols.  
    *I will send the email to user email if he has success registration on my site.
    *Make a button "forgot password" and if user click on it send to the user email the new password.