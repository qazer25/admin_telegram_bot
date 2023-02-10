# admin_telegram_bot


want wishes and service feedback automated with regular reminders? Look no further!\n


Steps to setup bot (for people with no python background)

Things to need:  
-fly.io account and platform  
-Google account  
-a working com(preferred windows, Mac/Linux users welcome to try)  
-a credit card/debit card(for fly.io and maybe google stuff)  
-no money(its still free)  
-these files in 1 folder

1. main file install  
install vscode  
use vs code to go to the folder  
open terminal  
install pip3 (https://blog.eldernode.com/install-pip3-on-windows/)
Type pip --version in terminal. If not found or errors return back to previous step)
install pipenv (enter *pip install --user pipenv* into cmd)
enter *pipenv install*  
enter *pipenv run python main.py*  
(Should not be able to run yet)


2. Asking BotFather for help
Type @BotFather in the searchbar  
Ask him nicely to create a bot for you (google for how, there's a lot of simple guides)  
Obtain the username and HTTP API(I called it bot token)  



3. google drive setup  
(https://developers.google.com/apps-script/api/quickstart/python)  
set up google cloud project  
set up google oauth stuff  
add script from google_scripts folder  
deploy as api exec  
(setup GCP if needed)  
add script id into bot_settings.py  

4. Fly.io setup  
(https://bakanim.xyz/posts/deploy-telegram-bot-to-fly-io/)  
(https://fly.io/docs/hands-on/)  
install fly on terminal  
setup app with redis database(don't use postgres database when prompted)  
setup postgres database  
(rmb all connection strings to add into not_settings later)  
change name in fly.toml  
set secrets for bot token, database, redis and script id as TOKEN, DATABASE_URL, REDIS_URL, SCRIPT_ID
(https://fly.io/docs/reference/secrets/)  
Change vm count to prevent multiple bots (https://fly.io/docs/reference/scaling/)
Use *fly scale count 1* in terminal
Enter *fly deploy* in terminal
 







