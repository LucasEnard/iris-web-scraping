# **What is Web Scraping:**

In simple terms, **Web scraping**, **web harvesting**, or **web data extraction** is an automated process of collecting large data(unstructured) from websites. The user can extract all the data on particular sites or the specific data as per the requirement. The data collected can be stored in a structured format for further analysis.

<img alt="What is Web Scraping? — James Le" data-noaft="1" jsaction="load:XAeZkd;" jsname="HiaYvf" src="https://images.squarespace-cdn.com/content/v1/59d9b2749f8dce3ebe4e676d/1566319595811-MFGFIVQGNNSY2W4TZ4AV/web-scraping.png?format=1500w" />  
  
**Steps involved in web scraping:**

  1. Find the URL of the webpage that you want to scrape
  2. Select the particular elements by inspecting
  3. Write the code to get the content of the selected elements
  4. Store the data in the required format

It’s that simple !!

## **The popular libraries/tools used for web scraping are:**

  * Selenium – a framework for testing web applications
  * BeautifulSoup – Python library for getting data out of HTML, XML, and other markup languages
  * Pandas – Python library for data manipulation and analysis

##  BS4
What is Beautiful Soup? {#what-is-beautiful-soup?}

Beautiful Soup is a pure Python library for extracting structured data from a website. It allows you to parse data from HTML and XML files. It acts as a helper module and interacts with HTML in a similar and better way as to how you would interact with a web page using other available developer tools.

  * It usually saves programmers hours or days of work since it works with your favorite parsers like `lxml` and `html5lib` to provide organic Python ways of navigating, searching, and modifying the parse tree.
  * Another powerful and useful feature of beautiful soup is its intelligence to convert the documents being fetched to Unicode and outgoing documents to UTF-8. As a developer, you do not have to take care of that unless the document intrinsic doesn't specify an encoding or Beautiful Soup is unable to detect one.
  * It is also considered to be **faster** when compared to other general parsing or scraping techniques.


# **Using full Python to web scrap on IRIS**

## The Production
### Starting the Production

While in the iris-web-scraping folder, open a terminal and enter :
```
docker-compose up
```
The very first time, it may take a few minutes to build the image correctly and install all the needed modules for Python.

### Access the Production

Following this link, access the production : [Access the Production](http://localhost:52795/csp/irisapp/EnsPortal.ProductionConfig.zen?PRODUCTION=iris.Production)

### Closing the Production
```
docker-compose down
```


## Step 1
Find the URL of the webpage that you want to scrape.  
 

url : "http://quotes.toscrape.com/"

The webpage that we are gonna scrape data from is a simple website for webscraping training, this is the simplest page to scrap, but if you are interested you can try the others.

We are going to scrap the Quotes and the Authors
  
**We will be using two Python libraries.**<br>These were automatically installed at start up.

  * **requests** Requests is a HTTP library for the Python programming language. The goal of the project is to make HTTP requests simpler and more human-friendly. <span> </span>
  * **bs4 for BeautifulSoup** Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.

## Step 2
Select the required elements by inspecting

If you go on "http://quotes.toscrape.com/", and inspect the page, you will be able to see the elements of the html and you'd be able to understand what to scrap.



###  
Step 3: Write the code to get the content of the selected elements

We will be using the find_all functionality on BeautifulSoup to look for all the tags which contains the class name "cardOutline"

{
  "url":"http://quotes.toscrape.com/"
}