#import the library used to query a website
from urllib.request import urlopen

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame()
j =0

#specify the url
job_listing1 = "https://losangeles.craigslist.org/d/computer-gigs/search/cpg"
job_listing2 = "https://losangeles.craigslist.org/d/web-html-info-design/search/web"

job_listing3 = "https://newyork.craigslist.org/search/web?search_distance=200&postal=10005"
job_listing4 = "https://newyork.craigslist.org/d/computer-gigs/search/cpg"

job_listing5 = "https://sfbay.craigslist.org/search/sfc/cpg?is_paid=yes"
job_listing6 = "https://sfbay.craigslist.org/search/sfc/web"

job_listing = [job_listing1, job_listing2, job_listing3, job_listing4, job_listing5, job_listing6]

for i in job_listing:

    #Query the website and return the html to the variable 'page'
    page = urlopen(i)
    print("Getting data from",i) 
    #Parse the html in the 'page' variable, and store it in Beautiful Soup format
    soup = BeautifulSoup(page)
    #print(soup.prettify())
    
    right_listing = soup.find('ul', class_='rows')
    
    #Generate lists
    A=[]
    B=[]
    C=[]
    
    for row in right_listing.findAll("li"):
        j =  j + 1;
        date = row.find('time', class_='result-date')
        formatted_date = date.get("datetime")
        correct_date = formatted_date[0:10]
        title = row.find('a', class_='result-title hdrlnk')
        link = title.get("href")
      
        A.append(correct_date)
        B.append(title.find(text=True))
        C.append(link)
        if j == 21:
            break 
        
    
    j=0
    
    df1 = pd.DataFrame()
    df1['Time']=A
    df1['Job']=B
    df1['Link']=C
    print("Number of jobs fetched", df1.shape)

    df=df.append(df1)


df=df.sort_values(by='Time', ascending=False) 
print("Total number of jobs", df.shape)

#df.set_option('display.html.render_links',)

# send the results into an HTML page which will open in default browser

df.to_html('filename.html', escape=False)
webbrowser.open("/home/maninder/filename.html", new=2)

#df.to_csv('out.csv', index=False)
#df.to_csv('out.csv', encoding='utf-8', index=False)


                   


