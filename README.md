# Formaloo SDK

This is a free SDK for using the API of Formaloo Customer Data Platform.

Formaloo is the next generation of data analytics. With Formaloo you can Use your own data to analyze your customers, your business and even predict the future. Formaloo adds an AI-powered data expert to SMBs & SMEs so they can really understand their business and their customers and act on it to boost their Loyalty, LTV and CX.

Formaloo is built for businesses, not data scientists. It's super simple to use and understand, you don't have to know data analytics or coding and best of all, it requires no data experts to operate it.

Formaloo CDP is a Customer Data Platform that collects, analyzes, and unifies data from all data sources in order to grow customers' loyalty.

Formaloo is a business productivity solution built to transform the way people collect information and put it to work.
Formaloo solutions such as Formaloo CDP, Data Collection (Database & Form builder), Formaloo DataFlow, Data Analysis tool, Workflow Automation helps thousands of businesses every day to collect & manage their data with impact.


# Installation
Install formaloo sdk using pip:
pip install formaloo-cdp

# Authentication
Get **client key** and **secret key** in formaloo dashboard:
https://cdp.formaloo.net/redirect/current-organization/integrations

Then export them as environment variables:
`export FORMALOO_CLIENT_KEY = 'YOUR_FORMALOO_CLIENT_KEY'`
`export FORMALOO_CLIENT_SECRET = 'YOUR_FORMALOO_CLIENT_SECRET'`

# Usage

**Example**: we want to get stats of a form, first we should import `Form` class and create an instance,
then we call `get_stats` method like below:

    from formaloo.forms import Form
    
    form = Form()
    
    form.get_stats(
        url_params=['9mpTfdpR']
    )
 **action**: Every class has a list of actions. in this example get_stats is a action of `Form` class.
 You have access to list of actions for a class by `actions_list` property.
` print(form.actions_list)`

**url_params**: in this argument we set parameters of url in a list by order, in this example `9mpTfdpR` is slug of form.
