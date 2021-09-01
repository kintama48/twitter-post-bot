# Twitter Post Bot
**Contents:**
 1. bot.py
 2. config.json
 3. README.md
 4. requirements.txt
 5. Procfile
 
 ## bot.py
 The bot.py file is our bot. To actually run the bot you, you will need to run this file on your hosting service.
 
 ## config.json
 This file has API keys, access keys and secrets. Don't mess with this, it is customised to your server, channels, twitter account and developer portal.
 
 ## README.md
 It's the file you are reading right now.

## requirements.txt
This file has all the dependencies that you will need.

## Procfile
It's the configuration for deploying on Heroku.

# How to Run:
 **On custom hosting service:**
 1. Make sure you have python3 installed on your hosting service or device. Visit https://www.python.org/downloads/ to download python3.
 2. After it's installed make a virtual environment and activate it. This step is not necessary but recommended.
 3. To install all the dependencies, in your terminal type "pip3 install -r requirements.txt".
 4. Run bot.py  after navigating to its directory(in terminal type "python bot.py" or if you are using linux then "python3 bot.py")

 **On Heroku:**
 1. Upload this code to a git repository
 2. Create a new app on heroku
 3. In the heroku app, go to deploy tab and scroll down
 4. Press connect to github and authorize the app
 5. After authorization, you can select the repository where our code was uploaded
 6. It will be deployed automatically
 7. Now go to the resources section and turn on the dynos toggle button