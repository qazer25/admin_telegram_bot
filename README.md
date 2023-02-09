# admin_telegram_bot


want wishes and service feedback automated with regular reminders? Look no further!\n


Steps to setup bot (for people with no python background)

Things to need:  
-fly.io account and platform  
-Google account  
-a working com  
-a credit card/debit card  
-no money(its still free)  
-these files in 1 folder

1. main file install  
install vscode  
use vs code to go to the file  
open terminal  
install pip3  
install pipenv  
enter <pipenv install>  
enter <pipenv run shell python main.py>  

2. google drive setup  
(https://developers.google.com/apps-script/api/quickstart/python)  
set up google cloud project  
set up google oauth stuff  
add script  
deploy as api exec  
(setup GCP)  
add script id into script  

3. Fly.io setup  
(https://bakanim.xyz/posts/deploy-telegram-bot-to-fly-io/)  
(https://fly.io/docs/hands-on/)  
install fly on cmd/linux shell  
setup app with redis database  
setup postgres database  
(rmb all connection strings to add into script later)  
change name in fly.toml  
set secrets for database and redis if needed  
fly deploy  
 







