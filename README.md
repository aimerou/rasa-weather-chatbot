# Weather bot

This chatbot is conversational agent that informs user about the weather of a specific location throughout the world.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table Of Contents**

- [Install dependencies](#install-dependencies)
- [Run the bot](#run-the-bot)
- [Run the django server](#run-the-django-server)
- [Overview of the files](#overview-of-the-files)
- [Things you can ask the bot](#things-you-can-ask-the-bot)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Install dependencies

Run:
```bash
pip install -r requirements.txt
```

## Run the bot

Move to the chatbot folder `cd chatbot`.

To train a model, use:
```bash
rasa train
```

Then, to run, first set up your action server in one terminal window:
```bash
rasa run actions
```

In another window, you can enable the api by running:
```
 rasa run -m models --enable-api --cors "*" --debug 
```

> Note that `--debug` mode will produce a lot of output meant to help you understand how the bot is working under the hood. To simply talk to the bot, you can remove this flag.


## Run the django server

Move to the django folder `cd django_ui`.

To run the django server:
```bash
python manage.py runserver
```

Then, you can see your app at the url `http://127.0.0.1:8000/`.

## Overview of the files

`data/stories.md` - contains stories

`data/nlu.md` - contains NLU training data

`actions/actions.py` - contains custom action/api calls code

`domain.yml`         - the domain file, including bot response templates

`config.yml`         - training configurations for the NLU pipeline and policy ensemble

## Things you can ask the bot

The bot currently has __one skill__. You can ask it to tell you the weather in a specific location.
