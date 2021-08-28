# Django_logical


An [HTTP request](https://rapidapi.com/blog/api-glossary/http-request-methods/) is an action to be performed on a resource identified by a given Request-URL. 

An [HTTP response](https://www.ibm.com/support/knowledgecenter/SSGMCP_5.3.0/com.ibm.cics.ts.internet.doc/topics/dfhtl22.html) is made by a server to a client. 

In this assignment, we would learn about different types of HTTP requests and Responses in Django. Django uses request and response objects to pass state through the system.

When a client requests a resource, an HttpRequest object is created, and correspond view function is called that returns the HttpResponse object.

To handle request and response, Django provides HttpRequest and HttpResponse/JsonResponse, classes

Some More details can be found here https://docs.djangoproject.com/en/3.1/ref/request-response/

At a High level, this Django application will perform different HTTP requests to perform some logical operations

### Some Guide for urls.py:
1. **Name in Django URL** -> name is used for accessing that URL from your Django / Python code. 
2. For example you have this in simpleapp/urls.py
3. **url(r'^main/', views.main, name='main')**
4. In point 2, "main" is the name of this URL
5. **URL namespaces** -> URL namespaces allow you to uniquely reverse named URL patterns even if different applications use the same URL names. 
in Django_logical/urls.py, path('', include(('simpleapp.urls', 'simpleapp'),namespace='simpleapp') ), **namespace='simpleapp'**

### API

API, short for Application Programming Interface, refers to a part of a computer program designed to be used or manipulated by another program, as opposed to an interface designed to be used or manipulated by a human
API contains the following parts
1. Base URL -> All requests we make to the API must begin with this portion of the URL. All APIs have a base URL like this one that is the same across all requests to the API. Our base URL is
```
http://127.0.0.1/
```
2. Url Path -> paths are endpoints (resources), such as /users or /reports/summary/, that your API exposes. In Django url file, we set these paths
3. Together they form an API. So suppose if you find /simple/?id=10, it means API for that URL is http://127.0.0.1/users/?id=10
4. **OR** /simple/10 is http://127.0.0.1/simple/10 
5. **OR** /simple/ -d 'id=10' is 
http://127.0.0.1/simple/
Body: {'id':'10'}


### API Testing
Once you create APIs, you have to test it
The recommended way to do API testing is through Postman or curl
We would be Using Postman to test these Apis
Postman is a scalable API testing tool.




## Part 1: Calculate the square of a Number
With following HTTP requests types GET, PUT, POST, DELETE

Calculate the square of a Number passed

Django URL name: array_addition

Parameter Name: number

1. GET:
```
# With No parameter passed
/simpleapp/
Response -> "Send Parameter number in url"
```
    /simpleapp/?number=10
    Response -> Square of Number 10 is 100"
```
Incorrect parameter Passed
 /simpleapp/?no.=10
    Response -> Square of Number 10 is 100"
```


2. POST:
```
# With No data passed
    /simpleapp/
Response -> "Send Parameter number in data"
```
    /simpleapp/ -d "number=15"
    Response -> {"data": "Square of Number 15 is 225"}
```
Incorrect parameter Passed
/simpleapp/ -d "no.=15"
Response -> "Send Parameter number in data"
```


3. PUT : 
```
# With No parameter passed
/simpleapp/
Response -> "Send Parameter as /simpleapp/<number>"
```
    /simpleapp/15
    Response -> {"data": "Square of Number 15 is 225"}

4. DELETE :
```
# With No parameter passed
/simpleapp/
Response -> "Send Parameter as /simpleapp/<number>"
```
    /simpleapp/15
    Response -> {"data": "Square of Number 15 is 225"}


#### Example Curl requests

curl -X POST "http://127.0.0.1:8000/simpleapp/" -d "number=10"

{"data": "Square of Number 10 is 100"}



## Part 2: Check whether a string is a palindrome
With the following HTTP requests types GET, PUT, POST, DELETE Check whether a string is a palindrome

Django URL name: palindrome_check

Parameter Name: string
1. GET
```
# With No parameter passed
/palindrome_check/
Response -> "Send Parameter string in URL to check palindrome"
```
    /palindrome_check/?string=calender
    Response -> "<b>calender</b> is not a palindrome"
```
Incorrect parameter Passed
/palindrome_check/?text=hello
Response -> "Send Parameter string in url to check palindrome"
```

2. POST
```
# With No data passed
/palindrome_check/
Response -> "Send Parameter string in data to check palindrome"
```
    /palindrome_check/ -d "string=abbbba"
    Response -> {"result": "abbbba is a palindrome"}
```
/palindrome_check/ -d "text=jjj"
Response -> "Send Parameter string in data to check palindrome"
```

3. PUT
```
# With No parameter passed
/palindrome_check/
Response -> "Send parameter as /palindrome_check/<string>"
```
    /palindrome_check/abbbba
    Response -> '{"result": "abbbba is a palindrome"}

4. DELETE
```
# With No parameter passed
    /palindrome_check/
    Response -> "Send parameter as /palindrome_check/<string>"
```
    /palindrome_check/abbbba
    Response -> '{"result": "abbbba is a palindrome"}
    

#### Example Curl Requests

curl -X PUT "http://127.0.0.1:8000/palindrome_check/a"

{"result": "a is a palindrome"}

curl -X POST "http://127.0.0.1:8000/palindrome_check/" -d "string=12"

{"result": "12 is not a palindrome"}


## Part 3: Add all the numbers separated by Comma
With the following HTTP requests types GET, POST add all the numbers separated by Comma


Django URL name: index

Parameter Name: array

1. GET
```
# With No parameter passed
    /array_addition/
    Response -> "Send Parameter array as comma seperated numbers 2,3,4,5"
```
    /array_addition/?array=100,200,300,1000
    Response -> "<h1>Sum is 1600</h1>"
```
    /array_addition/?array=1,-1,-3,3
    Response -> "<h1>Sum is 0</h1>"
```
    Incorrect Parameter
    /array_addition/?list=1,-1,-3,3
    Response -> "Send Parameter array as comma seperated numbers 2,3,4,5"
```
```


2. POST

```
    #With No data passed
    /array_addition/
    Response -> "Send Parameter array in data as comma seperated numbers 2,3,4,5"
```
    /array_addition/ -d "array=22,25,100,3"
    Response -> {"sum": "150"}
```
Incorrect Parameter
/array_addition/ -d "list=22,25,100,3"
Response -> {"sum": "150"}
```
