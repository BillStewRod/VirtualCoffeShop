💡 **The website design is inspired by:** 💡 <br>
[@divanov11](https://github.com/divanov11)
 Find his:
- repository here: https://github.com/divanov11/Digital-Resume
- YouTube video here: https://youtu.be/clwpf3VwCZQ

[@Sven-Bo](https://github.com/Sven-Bo)
Find his:
- Repository here: https://github.com/Sven-Bo/digital-resume-template-streamlit
- YouTube video here: https://www.youtube.com/watch?v=BXAeMICmUSQ&t=77s&ab_channel=CodingIsFun

## Live Demo
👉 ****https://billyresume-00129d30221d.herokuapp.com/****

## Screenshots
![Demo1](./assets/Screenshot.png?raw=true "Demo1")
![Demo2](./assets/Screenshot1.png?raw=true "Demo2")
![Demo3](./assets/Screenshot2.png?raw=true "Demo3")
![Demo4](./assets/Screenshot3.png?raw=true "Demo4")
![Demo5](./assets/Screenshot4.png?raw=true "Demo5")

## Requirements
Install the dependencies with pip
```
Pillow==9.2.0
streamlit==1.12.0
```

## Run the app
Terminal
```
# vanilla terminal
streamlit run app.py
```
## Heroku App Deployment ##
"Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps — we're the fastest way to go from idea to URL, bypassing all those infrastructure headaches."

Install the Heroku CLI
Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
```
heroku login
heroku create APP_NAME
```
Clone the repository
Use Git to clone REPOSITORY_NAME's source code to your local machine.
```
heroku git:clone -a REPOSITORY_NAME 
cd REPOSITORY_NAME 
```
Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.
```
git add .
git commit -m "DESCRIPTION"
git push heroku master
```
Once deployed web app is deployed to servers (Dynos) if you want to keep it free add the following line
```
heroku ps:scale web=1
```
Heroku apps will go to sleep after 45 min of inactivity the below web page will ping the app every 30 min 
[Kaffeine](https://kaffeine.herokuapp.com/)

## Get to Know Me & Stay Connected
- 💼 **LinkedIn:** [Connect with me](https://linkedin.com/in/billiamstewartrodriguez)
- 📸 **Instagram:** [Follow me](https://instagram.com/djcalanco)



