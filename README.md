# synent-task8-webscraper-harisfarooq
it is the web scraper used to extract the news data from BBC news website of different domain



News Website Data Scraper


Project Overview

This project is a Python-based web scraping application developed during my internship task. The main purpose of this project is to extract news titles and news links from the BBC News website and store the scraped data in an organized Excel file for easy access and analysis.

The scraper uses Python libraries such as BeautifulSoup, Requests, and OpenPyXL to fetch webpage content, parse HTML data, and save the extracted information into an .xlsx file.

This project helped in understanding real-world web scraping techniques, HTML parsing, data extraction, and Excel file automation.

Features
Connects to the BBC News website
Extracts news titles from the webpage
Collects corresponding news article links
Converts relative links into complete URLs
Stores structured data in an Excel file
Handles request errors using exception handling
Technologies Used
Python
BeautifulSoup (bs4)
Requests
OpenPyXL
How It Works
Sends a request to the BBC News website
Retrieves the HTML content of the webpage
Parses the HTML using BeautifulSoup

Output
The final output is saved in an Excel file named:
News_Website_Data.xlsx
The file contains:


News Title


News Link



Learning Outcome
Through this project, I improved my practical knowledge of:


Web scraping


HTML structure analysis


Data extraction from websites


Python automation


Excel file handling using Python


This project was completed as part of my internship task and strengthened my understanding of real-world Python applications.

Finds all anchor (<a>) tags containing news data
Extracts the title and link of each news item
Saves the extracted data into an Excel sheet
