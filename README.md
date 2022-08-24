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


## Step 1 : Find the URL of the webpage that you want to scrape.  

The example url here is :<br>
url : "http://quotes.toscrape.com/"

The webpage that we are gonna scrape data from is a simple website for webscraping training, this is the simplest page to scrap, but if you are interested you can try the others.

We are going to scrap the Quotes and the Authors
  
**We will be using two Python libraries.**<br>These were automatically installed at start up.

  * **requests** Requests is a HTTP library for the Python programming language. The goal of the project is to make HTTP requests simpler and more human-friendly. <span> </span>
  * **bs4 for BeautifulSoup** Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.

## Step 2 : Select the required elements by inspecting

If you go on "http://quotes.toscrape.com/", and inspect the page, you will be able to see the elements of the html and you'd be able to understand what to scrap.

As you can see, we have a `div class="quote"` that contains all the quote we want to scrap. Then, in each of these div, we have a `span class="text"` and a `small class="author"`.

We now know what we want to gather and how to access them.


## Step 3 : Write the code to get the content of the selected elements

First we need to requests the HTML from the website and parse it into a bs4 object :
```
req = requests.get(request.url)
soupdata = bs4.BeautifulSoup(req.text, features="html.parser")
```


**Here is the code that need to be changed for another webpage**
Access `src/python/bo/py` in the `on_scrap_request` function.

We will be using the findAll functionality on BeautifulSoup to look for all the tags which contains the type div and the class quote :
```
divs = soupdata.findAll("div",{"class":"quote"})
```

Then, for each quote, we want to get the type span and class text, and the type small and class author :
```
for i in range(len(divs)):
    text = divs[i].find("span",{"class":"text"}).text
    author = divs[i].find("small", {"class":"author"}).text
```

We then put all those results in our IRIS message and send them back to you, the user.

## Step 4 : Use the production
You must access the `Production` following this link :
```
http://localhost:52795/csp/irisapp/EnsPortal.ProductionConfig.zen?PRODUCTION=iris.Production
```

And connect using :<br>
```SuperUser``` as username and ```SYS``` as password.


To call the scraping, click on the `Python.ScrapingOperation`, and select in the right tab `Actions`, you can `Test` the production.

In this test window, select :

Type of request : Grongier.PEX.Message

For the classname you must enter :
```
msg.ScrapRequest
```

And for the json, you must enter the url you want to scrap :
```
{
  "url":"http://quotes.toscrape.com/"
}
```

From here press `Invoke Testing Service` and watch the visual trace.

By going on the last message and clicking on `contents` you shall see the scraped data.

# Conclusion
Here is the simplest example of scraping, it can be easily used by anyone and is implemented on IRIS, this means that with just a few tweaks you can connect this Operation [to a CRUD API](https://github.com/grongierisc/iris-python-flask-api-template) or to a automatic service that gather data from the web and input it into the IRIS DATABASE
[This last link is in fact a link to a Formation in Python](https://github.com/LucasEnard/formation-template-python) on IRIS that shows how to use this module properly and how to connect to the IRIS DB or an external PostGres DB and doing so using a CRUD API.

# References
[See this post on the DC ](https://community.intersystems.com/post/introduction-web-scraping-embedded-python-let%E2%80%99s-extract-python-job%E2%80%99s) as my inspiration to do this GitHub.