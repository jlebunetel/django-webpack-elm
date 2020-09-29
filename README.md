# django-webpack-elm
A template to quickly create a modern web application project with Django and Elm.

## Features
* Create a fully functional [Django](https://www.djangoproject.com/) project witch includes:
    * Custom user management with [django-allauth](https://django-allauth.readthedocs.io);
    * Web API framework with [Django REST framework](https://www.django-rest-framework.org/);
    * Dynamic content translation with [Modeltranslation](https://django-modeltranslation.readthedocs.io).
* Sets up the JavaScript module bundler [webpack](https://webpack.js.org/) which integrates:
    * [Elm](https://elm-lang.org/) compilation;
    * The CSS framework [Bulma](https://bulma.io/);
    * The [Font Awesome](https://fontawesome.com/) icon set.
* Provides a `Makefile` with a set of tools to manage the project:
    * install tools for development or production environments;
    * a [Cookiecutter](https://cookiecutter.readthedocs.io) template to create new apps;
    * deploy tools, etc.

## Quickstart
Make sure you have `python3.8` and `venv` module installed on your machine, then run:
```
$ make quickstart
```
Then, visit http://127.0.0.1:8000/ with your Web browser.

## Technical details
To know more about the development guidelines of this project, see the [TECHNICAL_DETAILS.md](TECHNICAL_DETAILS.md) file.

## Contributing
If you'd like to contribute, please raise an issue or fork the repository and use a feature branch. Pull requests are warmly welcome!

## Licensing
The code in this project is licensed under MIT license. See the [LICENSE](LICENSE) file for details.

## Contributors
* **Julien Lebunetel** - [jlebunetel](https://github.com/jlebunetel)
