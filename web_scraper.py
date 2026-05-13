from bs4 import BeautifulSoup
import requests , openpyxl
excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = "News Website Data"
sheet.append(["News Title" , "News Link" ])

try:

   source = requests.get("https://www.bbc.com/news")
   source.raise_for_status()
   soup = BeautifulSoup(source.text , "html.parser")
   news_items = soup.find_all("a")
   for item in news_items:

       title = item.get_text(strip=True)
       link = item.get("href")

       if link and link.startswith("/"):
          link = "https://www.bbc.com/news" + link

       if title and link:
          print(title , link)
          sheet.append([title , link ])
          excel.save("News_Website_data.xlsx")
          print("Data saved sucessfully")

except Exception as e:
    print(e)