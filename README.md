# Scrapping_MUBAWAB.ma-
collecting data from mubawab.ma website to use it for creating predictive model
## how it works?
>This web scrapper extract posted articles links from each page , and it use each article link to access into article details , after that the needed content of this webpage will be exracted and returned as a python dictionnary. Also, each article data collected will be stored as row in a csv file using dictionnary writer.
## how much time it take?
> In my personnal computer (8GB RAM , intel i7-10th) it take 3 hour to extract data from 18100 webpages.
## frameworks used:
>I used Beautifulsoup4 for parsing the html code extracted from the web server using requests library, also i used python regular expression to extract and clean alphanumerical data from the web page .
