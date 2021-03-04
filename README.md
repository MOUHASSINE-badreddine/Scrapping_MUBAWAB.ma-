# Scrapping_MUBAWAB.ma-
collecting data from mubawab.ma website to use it for creating predictive model
## how it works?
>This web scrapper extract posted articles urls from each page , and it uses each article url to access into article details , after that the needed content of this webpage will be exracted and returned as a python dictionary. Also, each article data collected will be stored as row in a csv file using dictionary writer.
## how much time it takes?
> In my personal computer (8GB RAM, Intel i7-10th) it takes 3 hours to extract data from 18100 web pages.
## frameworks used:
>I used Beautifulsoup4 for parsing the html code extracted from the web server using request library, also I used python regular expression to extract and clean alphanumerical data from the web page.
