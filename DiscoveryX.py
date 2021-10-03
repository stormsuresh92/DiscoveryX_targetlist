from requests_html import HTMLSession
import pandas as pd


s = HTMLSession()

def url():
    url = 'https://www.discoverx.com/targets/alphabetical-target-list'
    r = s.get(url)
    urls = r.html.find('td')
    linklist = []
    for url in urls:
        links = 'https://www.discoverx.com' + url.find('a', first=True).attrs['href']
        linklist.append(links)
    return linklist

def genedata(url):
    r = s.get(url)
    content = r.html.find('dl.target-info')
    for item in content:
        try:
            Official_Symbol = item.find('dl > dd:nth-child(6)', first=True).text
        except:
            Official_Symbol = ''
        try:
            Entrez_ID = item.find('dl > dd:nth-child(8)', first=True).text
        except:
            Entrez_ID = '' 
        try:
            Species = item.find('dl > dd:nth-child(10)', first=True).text
        except:
            Species = ''
        try:
            Accession_Number = item.find('dl > dd:nth-child(12)', first=True).text
        except:
            Accession_Number = '' 
        try:
            Aliases = item.find('dl > dd:nth-child(14)', first=True).text
        except:
            Aliases = ''
        dic = {
            'Gene':Official_Symbol,
            'Aliases':Aliases,
            'Species':Species,
            'Entrez':Entrez_ID,
            'Accession':Accession_Number
        }
        
    return dic

mainlist = []
urls = url()[0:6]
for link in urls:
    mainlist.append(genedata(link))
    
df = pd.DataFrame(mainlist)
df.to_csv('genes.csv', index=False)
print('fin')