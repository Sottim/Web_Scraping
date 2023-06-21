import requests
import pandas as pd 
from bs4 import BeautifulSoup

data = pd.read_excel("input.xlsx")
#Iterate over each row of the data given in the input.xlsz file
for index, row in data.iterrows():    
    url_ID = row['URL_ID']
    url = row['URL']
    
    #Get the information req from the link provided
    url_info = requests.get(url)
    soup = BeautifulSoup(url_info.text, 'html.parser')
    # print(f"URL ID: {url_ID}")
    # print(soup.prettify())
    #For extracting the title of the article and remove trailing whitespace characters
    title = soup.find('title').get_text()
    article_title = title.strip()

    #For extracting the text from articles
    article_content = soup.find('div', attrs = {'class' : 'td-post-content tagdiv-type'})

    #There are two variety of classes in the given list of urls, Need to check both the varients.
    if article_content:
        article_text = ''
        extract_paragraphs = article_content.find_all('p')
        print(extract_paragraphs)

        for para in extract_paragraphs:
            # texts += para.get_text()
            article_text += para.get_text().strip() + '\n'
    
    else:
        article_content = soup.find('div', attrs = {'class' : 'tdb-block-inner td-fix-index'})
        if article_content: 
            article_text = ''
            extract_paragraphs = article_content.find_all('p')
            print(extract_paragraphs)
            
            for para in extract_paragraphs:
                # texts += para.get_text()
                article_text += para.get_text().strip() + '\n'
                print(article_text)
        else:
            article_text = ''

    #Saving the title
    file_name = f'{url_ID}.txt'
    with open(file_name, 'w', encoding = 'utf-8') as file:
        file.write(article_title + '\n\n')
        file.write(article_text)
    print(f'{file_name} is saved successfully.')

print('End of extraction process.')


