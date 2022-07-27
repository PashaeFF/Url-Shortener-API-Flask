# URL Shortener

- [URL Shortener](#url-shortener)
- [Project Title](#project-title)
- [Description](#description)
- [Installing](#installing)
      - [First](#first)
      - [Second](#second)
      - [Third](#third)
      - [First m](#first-m)
      - [Second](#second-1)
      - [Third](#third-1)
- [Executing program](#executing-program)
- [Environment variables](#environment-variables)
- [Author](#author)
- [Version](#version)
___

# Project Title
___
* <b> URL Shortener</b>
___

# Description
___
* <b> Create short URL </b>
* <b> Short URL visits count(with UUID)</b>
* <b> Statistics for URL visits count</b>
* <b> Statistics for each url (with id) </b>
____

# Installing
>### for <font color = "red">Windows</font>
#### First                
``` 
> py -3 -m venv env

```
#### Second
```
> env\Scripts\activate
> pip install -r requirments.txt

```
#### Third
*<b> Open a new file named ".env" and copy the following items into the file.</b>

```
FLASK_ENV=development
FLASK_APP=src
SQLALCHEMY_DB_URI="POSTGRESQL DB URI"
SECRET_KEY="YOUR SECRET KEY"

```


>### for <font color = "red">macOS / Linux</font>
#### First m
``` 
$ python3 -m venv env

```
#### Second
```
$ .env/bin/activate
$ pip install -r requirments.txt

```
#### Third
* <b>Open a new file named ".env" and copy the following items into the file.</b>

```
FLASK_ENV=development
FLASK_APP=src
SQLALCHEMY_DB_URI="POSTGRESQL DB URI"
SECRET_KEY="YOUR SECRET KEY"

```


# Executing program
___

<b>* How to run the program</b>

```
flask run
```
___

# Environment variables



| Variable name                                  | Value                                   | Description                                                                                                                                                                                             |
| ---------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `FLASK_ENV`                              | `"Development"`                                   | Mode.                                                                                                                                                                             |
| `FLASK_APP`                              | `src`                                          | APP file.                                                                                                                                                                             |
| `SQLALCHEMY_DB_URI`                          | `"POSTGRESQL DB URI"`                                        | PostgreSQL connection.                                                                                                                                                                         |
| `SECRET_KEY`                          | `"YOUR SECRET KEY"`                                        | Secret key password.                                                                                                                                                                                                                                                                                                                                       |
____

# Author

<b>Contributors names and contact info</b>

<b>ex. Pashayev Rafig - [PashaeFF - Github](https://github.com/PashaeFF) </b>

# Version

>* <b>v1.0</b>
>* <b>Initial Release</b>

___