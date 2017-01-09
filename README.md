# Mobot

**Mobot** is a Python powered chatbot built on pyAIML. But this project is a Flask App integrating Mobot with Facebook messenger so that it can response at messages from different Facebook pages instantly.

## What have been used?

- **Python**: Though I am a great fan of Python3 but this project is built on Python2. The aiml package doesn't support Python3, that was the reason behind it.
- **Flask**: Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you ask: It's BSD licensed!
- **pyAIML**: PyAIML implements an interpreter for AIML, the Artificial Intelligence Markup Language developed by Dr. Richard Wallace of the A.L.I.C.E. Foundation. It can be used to implement a conversational AI program.
- **Requests**: Requests is the only Non-GMO HTTP library for Python, safe for human consumption.
- **MarkupSafe**: MarkupSafe is a library for Python that implements a unicode string that is aware of HTML escaping rules and can be used to implement automatic string escaping. It is used by Jinja 2, the Mako templating engine, the Pylons web framework and many more.

## Run the project

Let's make a Python2 virtual environment. We will play some commands on Terminal.

```
sudo pip install virtualenv
```
```
virtualenv -p /usr/bin/python2.7 env
```
```
source env/bin/activate
```
```
cd env
```
```
git clone git@github.com:maateen/mobot.git
```

Now we will see a new folder named **mobot** in the **env** directory. This is our main project part. Let's dive into it.

```
cd mobot
```
```
mv config.py.sample config.py
```

Now we have to provide some information in **config.py**. There is inner documentation there. So I am not writing them again. After that simply run the project.

```
python run.py
```

The project will run on http://127.0.0.1:5000/ bu default. Hit that address on browser and you will see mobot page. 

But you have to deploy it on any server and connect to your facebook page to make it work. I will write more on it soon.