#Jeeves, the infamous Couscous detector.

##Introduction
Nobody likes couscous, so we built this to email us when it's tragically on the menu. By popular demand it's expanded to tell you when other horrible dishes are avilable, and there's more hall amelioration measures in the pipeline.

##Usage

`food_search.py` scrapes the hall menu for our hated foods, provided as an argument. So `python food_search.py "Soup"` will return a list of the days the dreaded Soup is due.

`receive_email.py` and `send_email.py` check our inbox for new subscribers and send out the email alerts to our mailing list, respectively.

`crs_ids.txt` forms our mailing list, holding those unlucky enough to be subscribed to our emails of doom.

`Main.pl` 'CRSID (for logging into mealbooking)' 'Jeeves' email' 'Jeeves' password' 'associated raven password for CRSID' sends a standard email (content pending) to all users in the text file