# Flask_Reference

# ~ Flask

What is Web Framework?
 
- Web Application Framework or simply Web Framework 
  - represents a collection of libraries and modules 
  - that enables a web application developer to write applications 
  - without having to bother about low-level details such as protocols, thread management etc.

# What is Flask?


```python
# Flask is a web framework 
  - that provides libraries to build lightweight web applications in python. 

# It is developed by Armin Ronacher who leads an international group of python enthusiasts (POCCO).

# Flask is 
  - based on the Werkzeug WSGI toolkit and Jinja2 template engine. 
     - Both are Pocco projects.

```


```python
# Flask is considered as a micro framework.

# It aims to keep the core of an application simple yet extensible. 

# Flask does not have built-in abstraction layer for database handling, nor does it have form a validation support. 
    
# Instead, Flask supports the extensions to add such functionality to the application.
```

# What is WSGI?

It is an acronym for web server gateway interface 
- which is a standard for python web application development. 

It is considered as 
- the specification for the universal interface 
- between the web server and web application.


```python
# Werkzeug
  It is a WSGI toolkit, 
    - which implements requests, response objects, and other utility functions. 
    
# This enables building a web framework on top of it. 
# The Flask framework uses Werkzeug as one of its bases.
```

# What is Jinja2?

Jinja2 is a web template engine 
 - which combines a template with a certain data source 
     - to render the dynamic web pages

# ~ Flask Environment Setup


```python
# To install flask on the system, 
# we need to have python 2.7 or higher installed on our system. 
# However, we suggest using python 3 for the development in the flask.

```

## Install virtualenv for development environment

virtualenv is considered as the virtual python environment builder 
- which is used to create the multiple python virtual environment side by side


```python
# can be installed by using the following command.
!pip install virtualenv
```

    Collecting virtualenv
      Downloading virtualenv-20.24.3-py3-none-any.whl (3.0 MB)
         ---------------------------------------- 3.0/3.0 MB 21.2 MB/s eta 0:00:00
    Collecting distlib<1,>=0.3.7
      Downloading distlib-0.3.7-py2.py3-none-any.whl (468 kB)
         ------------------------------------- 468.9/468.9 kB 14.8 MB/s eta 0:00:00
    Collecting platformdirs<4,>=3.9.1
      Downloading platformdirs-3.10.0-py3-none-any.whl (17 kB)
    Collecting filelock<4,>=3.12.2
      Downloading filelock-3.12.2-py3-none-any.whl (10 kB)
    Installing collected packages: distlib, platformdirs, filelock, virtualenv
      Attempting uninstall: platformdirs
        Found existing installation: platformdirs 2.5.2
        Uninstalling platformdirs-2.5.2:
          Successfully uninstalled platformdirs-2.5.2
      Attempting uninstall: filelock
        Found existing installation: filelock 3.9.0
        Uninstalling filelock-3.9.0:
          Successfully uninstalled filelock-3.9.0
    Successfully installed distlib-0.3.7 filelock-3.12.2 platformdirs-3.10.0 virtualenv-20.24.3
    

    
    [notice] A new release of pip available: 22.2.2 -> 23.2.1
    [notice] To update, run: python.exe -m pip install --upgrade pip
    

Once it is installed, we can create the new virtual environment into a folder as given below.

- mkdir new   
- cd new   
- virtualenv venv  



```python
# Change directory
cd "directroy_path"
```
    


```python
mkdir Flask
```


```python
cd Flask
```

    C:\Users\Administrator\Desktop\GitHub\Flask
    


```python
!virtualenv env

# ! env\Scripts\activate
# !source  venv/bin/activatea
```

    created virtual environment CPython3.10.9.final.0-64 in 9923ms
      creator CPython3Windows(dest=C:\Users\Administrator\Desktop\GitHub\Flask\env, clear=False, no_vcs_ignore=False, global=False)
      seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Administrator\AppData\Local\pypa\virtualenv)
        added seed packages: pip==23.2.1, setuptools==68.0.0, wheel==0.41.1
      activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
    


```python
pwd
```




    'C:\\Users\\Administrator\\Desktop\\GitHub\\Flask'




```python
# We can now install the flask by using the following command.

!pip install flask
```

    Requirement already satisfied: flask in c:\users\administrator\anaconda3\lib\site-packages (2.3.3)
    Requirement already satisfied: click>=8.1.3 in c:\users\administrator\anaconda3\lib\site-packages (from flask) (8.1.7)
    Requirement already satisfied: blinker>=1.6.2 in c:\users\administrator\anaconda3\lib\site-packages (from flask) (1.6.2)
    Requirement already satisfied: Jinja2>=3.1.2 in c:\users\administrator\appdata\roaming\python\python310\site-packages (from flask) (3.1.2)
    Requirement already satisfied: Werkzeug>=2.3.7 in c:\users\administrator\anaconda3\lib\site-packages (from flask) (2.3.7)
    Requirement already satisfied: itsdangerous>=2.1.2 in c:\users\administrator\anaconda3\lib\site-packages (from flask) (2.1.2)
    Requirement already satisfied: colorama in c:\users\administrator\appdata\roaming\python\python310\site-packages (from click>=8.1.3->flask) (0.4.5)
    Requirement already satisfied: MarkupSafe>=2.0 in c:\users\administrator\appdata\roaming\python\python310\site-packages (from Jinja2>=3.1.2->flask) (2.1.1)
    

    
    [notice] A new release of pip available: 22.2.2 -> 23.2.1
    [notice] To update, run: python.exe -m pip install --upgrade pip
    

we can install the flask using the above command without creating the virtual environment.

To test the flask installation, 
 -  open python on the command line 
 -  and type python to open the python shell. 
 -  Try to import the package flask.

# ~ First Flask application


```python
# To build the python web application, 
# we need to import the Flask module. 

# An object of the Flask class is considered as the WSGI application.

app = fk.Flask(__name__) #creating the Flask class object

# We need to pass the name of the current module, 
# i.e. __name__ as the argument into the Flask constructor.

# The route() function of the Flask class defines the URL mapping of the associated function. 
# The syntax is given below:
    app.route(rule, options)
    
# It accepts the following parameters.

 - rule: It represents the URL binding with the function.
 
 - options: It represents the list of parameters to be associated with the rule object
```


```python
# This code show SystemExit exit in jupyter notebook but runs in vscode

import flask as fk
  
app = fk.Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator defines the   
def home():  
    return "hello, this is our first flask website";  
  
if __name__ =='__main__':  
    app.run(debug = True)

```

     * Serving Flask app '__main__'
     * Debug mode: on
    

    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
     * Restarting with stat
    


    An exception has occurred, use %tb to see the full traceback.
    

    SystemExit: 1
    



```python
%tb
```


    ---------------------------------------------------------------------------

    SystemExit                                Traceback (most recent call last)

    Cell In [18], line 10
          7     return "hello, this is our first flask website";  
          9 if __name__ =='__main__':  
    ---> 10     app.run(debug = True)
    

    File ~\anaconda3\lib\site-packages\flask\app.py:889, in Flask.run(self, host, port, debug, load_dotenv, **options)
        886 from werkzeug.serving import run_simple
        888 try:
    --> 889     run_simple(t.cast(str, host), port, self, **options)
        890 finally:
        891     # reset the first request information if the development server
        892     # reset normally.  This makes it possible to restart the server
        893     # without reloader and that stuff from an interactive shell.
        894     self._got_first_request = False
    

    File ~\anaconda3\lib\site-packages\werkzeug\serving.py:1097, in run_simple(hostname, port, application, use_reloader, use_debugger, use_evalex, extra_files, exclude_patterns, reloader_interval, reloader_type, threaded, processes, request_handler, static_files, passthrough_errors, ssl_context)
       1094 from ._reloader import run_with_reloader
       1096 try:
    -> 1097     run_with_reloader(
       1098         srv.serve_forever,
       1099         extra_files=extra_files,
       1100         exclude_patterns=exclude_patterns,
       1101         interval=reloader_interval,
       1102         reloader_type=reloader_type,
       1103     )
       1104 finally:
       1105     srv.server_close()
    

    File ~\anaconda3\lib\site-packages\werkzeug\_reloader.py:456, in run_with_reloader(main_func, extra_files, exclude_patterns, interval, reloader_type)
        454             reloader.run()
        455     else:
    --> 456         sys.exit(reloader.restart_with_reloader())
        457 except KeyboardInterrupt:
        458     pass
    

    SystemExit: 1



```python
print(dir(flask))
```

    ['Blueprint', 'Config', 'Flask', 'Markup', 'Request', 'Response', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_app_ctx_stack', '_request_ctx_stack', 'abort', 'after_this_request', 'app', 'appcontext_popped', 'appcontext_pushed', 'appcontext_tearing_down', 'before_render_template', 'blueprints', 'cli', 'config', 'copy_current_request_context', 'ctx', 'current_app', 'escape', 'flash', 'g', 'get_flashed_messages', 'get_template_attribute', 'globals', 'got_request_exception', 'has_app_context', 'has_request_context', 'helpers', 'json', 'jsonify', 'logging', 'make_response', 'message_flashed', 'redirect', 'render_template', 'render_template_string', 'request', 'request_finished', 'request_started', 'request_tearing_down', 'scaffold', 'send_file', 'send_from_directory', 'session', 'sessions', 'signals', 'signals_available', 'stream_with_context', 'template_rendered', 'templating', 'typing', 'url_for', 'wrappers']
    


```python
# As we can see here, the / URL is bound to the main function 
 - which is responsible for returning the server response. 
    
# It can return a string to be printed on the browser's window 
# or we can use the HTML template to return the HTML file as a response from the server.

# Finally, the run method of the Flask class is used to run the flask application on the local development server.

# The syntax is given below.

app.run(host, port, debug, options)  
```


```python
Sr.No.  Parameters & Description

1       host
        Hostname to listen on. Defaults to 127.0.0.1 (localhost). 
        Set to ‘0.0.0.0’ to have server available externally

2       port
        Defaults to 5000

3       debug
        Defaults to false. If set to true, provides a debug information

4       options
        To be forwarded to underlying Werkzeug server.
```

# Debug mode

A Flask application is started by calling the run() method. 
However, while the application is under development, 
it should be restarted manually for each change in the code. 

To avoid this inconvenience, enable debug support. 
The server will then reload itself if the code changes. 

It will also provide a useful debugger to track the errors if any, in the application.

The Debug mode is enabled by setting the debug property of the application object to True before running or passing the debug parameter to the run() method.

app.debug = True
app.run()
app.run(debug = True)

# ~ Flask - Routing

Modern web frameworks use the routing technique 
 - to help a user remember application URLs. 
    
It is useful to access the desired page directly 
without having to navigate from the home page


```python
The route() decorator in Flask is used to bind URL to a function.

example −

@app.route(‘/hello’) # @  
def hello_world():
    return ‘hello world’

# Here, URL ‘/hello’ rule is bound to the hello_world() function. 
# As a result, 
# if a user visits <!-- http://localhost:5000/hello --> URL, 
#  - the output of the hello_world() function will be rendered in the browser. -->
```

### The add_url_rule() function

- to perform routing for the flask web application 
- that can be done by using the add_url() function of the Flask class

syntax:
    - add_url_rule(<url rule>, <endpoint>, <view function>)
    
This function is mainly used :

- in the case if the view function is not given 
- and we need to connect a view function to an endpoint externally by using this function.



```python
# A decorator’s purpose is also served by the following representation

def hello_world():
    return ‘hello world’
app.add_url_rule(‘/’, ‘hello’, hello_world) # @

# The add_url_rule() function of an application object 
# is also available to bind a URL with a function 
# as in the above example, route() is used.
```


```python
import flask as fl
app = fl.Flask(__name__)  
  
def about():  
    return "This is about page";  
  
app.add_url_rule("/about","about",about)  
  
if __name__ =="__main__":  
    app.run(debug = True)
```

     * Serving Flask app '__main__' (lazy loading)
     * Environment: production
    [31m   WARNING: This is a development server. Do not use it in a production deployment.[0m
    [2m   Use a production WSGI server instead.[0m
     * Debug mode: on
    

     * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
     * Restarting with stat
    


    An exception has occurred, use %tb to see the full traceback.
    

    SystemExit: 1
    


## @ App routing

@ App routing 
- is used to map the specific URL with the associated function 
- that is intended to perform some task.

In our first application, 
The URL ('/') is associated with the home function 
- that returns a particular string displayed on the web page.

In other words, we can say that 
if we visit the particular URL mapped to some particular function, 
- the output of that function is rendered on the browser's screen.


```python
from flask import Flask  
app = Flask(__name__)  
 
@app.route('/home')  
def home():  
    return "hello, welcome to our website";  
  
if __name__ =="__main__":  
    app.run() 
```

     * Serving Flask app '__main__' (lazy loading)
     * Environment: production
    [31m   WARNING: This is a development server. Do not use it in a production deployment.[0m
    [2m   Use a production WSGI server instead.[0m
     * Debug mode: off
    

     * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
    


```python
# Flask facilitates us to add the variable part to the URL 
# - by using the section. 

# We can reuse the variable by adding that as a parameter 
# - into the view function.

from flask import Flask  
app = Flask(__name__)  

@app.route('/home/<name>')  
def home(name):  
    return "hello,"+name;  
  
if __name__ =="__main__":  
    app.run(debug = True)
```

     * Serving Flask app '__main__'
     * Debug mode: on
    

    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
     * Restarting with stat
    


    An exception has occurred, use %tb to see the full traceback.
    

    SystemExit: 1
    


The converter can also be used in the URL 
- to map the specified variable 
- to the particular data type. 

For example, we can provide the integers or float like age or salary respectively.


```python
from flask import Flask  
app = Flask(__name__)  
 
@app.route('/home/<int:age>')  
def home(age):  
    return "Age = %d"%age;  
  
if __name__ =="__main__":  
    app.run(debug = True)
```

     * Serving Flask app '__main__' (lazy loading)
     * Environment: production
    [31m   WARNING: This is a development server. Do not use it in a production deployment.[0m
    [2m   Use a production WSGI server instead.[0m
     * Debug mode: on
    

     * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
     * Restarting with stat
    


    An exception has occurred, use %tb to see the full traceback.
    

    SystemExit: 1
    



```python
# The following converters are used to convert the default string type to the associated data type.


# string: default

# int   : used to convert the string to the integer

# float : used to convert the string to the float.

# path  : It can accept the slashes given in the URL
```
