requirements: python 3.9 is installed

How to run the project:
# install dependancies

pip install -r requirements.txt

# run project

python run.py

#get data

run api scrape_Grubhub

go to postman with get method  :

http://127.0.0.1:5000/scrape_Grubhub

the url to collect is on urls.txt file , you can put many urls and the script will iterate them and generate a xls file having name the restaurent name


To collect many urls we can use multithreading to use parallele execution of each url
