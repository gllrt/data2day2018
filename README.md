# Dash vs. Shiny

In this repo I provide all scripts and some documentation of the talk ["Dash & Shiny - Dashboards mit Python und R"](https://www.data2day.de/veranstaltung-7299-dash-%26-shiny---dashboards-mit-python-und-r.html?id=7299) I gave at the conference [data2day](https://www.data2day.de/) on 27th September 2018.

In particular, the talk walked the audience through building an app both in Dash and Shiny, covering the most common requirements one might have when it comes to dashboards: 

1. use a CSS-design that scales for different screen-sizes (bootstrap)
2. listen for user-input (text and dates)
3. retrieve data on a button-press,
4. display a table,
5. plotting different types of diagrams (wordcloud and timeseries) and
6. include further CSS- and HTML-code for customisation

**Please note:** The showcase app at the conference actually involved requesting tweets from the Twitter API. As to provide you with self-contained examples without the need to sign up for a Twitter developer account, I replaced a few code segments in order to include a tweet sample as a JSON-file which can be found in the `app` folder.

**Please note 2:** The content of this repo is neither complete nor final yet. I am trying to upload and update all files and text as soon as possible.

## Content of the repository
The folders `dash` and `shiny` both include four individual apps covering the above requirements as follows: app_1.* (1), app_2.* (1-2), app_3.* (1-5), app_4.* (1-6).

In addition, each of these folders contain some helper scripts in a subfolder `scripts` and `data` contains common datasets for all the apps.

## The Comparison

We summarise our findings of the comparison below. If you find some flaws or are interested in a discussion about these, please drop me an email.

### About the frameworks

- Dash: 
- Shiny: 

### Reactivity

- text input:
- date range input:
- sharing reactive element with multiple end-points:

### Customisation

### Deployment

### Documentation

### Verdict