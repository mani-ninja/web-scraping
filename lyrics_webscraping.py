#import the library used to query a website
from urllib.request import Request, urlopen

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import pandas as pd

pd.set_option('display.max_colwidth', -1)
df = pd.DataFrame()

j =0

import webbrowser

#specify the url
jl1 = "http://www.lyricsmint.com/2018/12/bandeya-rey-bandeya-lyrics-simmba-arijit-singh.html/"
jl2 = "http://www.lyricsmint.com/2018/12/dhadkan-lyrics-amavas.html/"


jl = [jl1, jl2]


for i in jl:
    
    #Query the website and return the html to the variable 'page'
    req = Request(i, headers={'User-Agent': 'Mozilla/5.0'}) 
    page = urlopen(req).read()

    print("Getting data from",i) 
    #Parse the html in the 'page' variable, and store it in Beautiful Soup format
    soup = BeautifulSoup(page)
    print(soup.prettify())
    
    #right_listing = soup.find('h1', class_='post-title entry-title')
    
    page_title = soup.find('h1', class_='post-title entry-title')
    print(page_title)
    
    summary= soup.find('p', class_='entry-summary')
    print(summary)
    
    no_lyrics = soup.find('div', {"id": "lyric"})
    lyrics = no_lyrics.find_all('p')
    
    #Generate lists
    A=[]
    B=[]
    C=[]
      
    A.append(page_title)
    B.append(summary)
    C.append(lyrics)        
    
    df1 = pd.DataFrame()
    df1['Title']=A
    df1['Summary']=B
    df1['Lyrics']=C
    print("Number of lyrics fetched", df1.shape)

    df=df.append(df1)


#df=df.sort_values(by='Title', ascending=False) 
print("Total number of lyrics", df.shape)

#df.set_option('display.html.render_links',)
df.to_html('lyrics_output.html', escape=False)

webbrowser.open("/home/maninder/lyrics_output.html", new=2)

df.to_csv('out.csv', index=False)
df.to_csv('out.csv', encoding='utf-8', index=False)


