# EnergySage Django Example

I use a third party library for a phone number field, so the requirements.txt
incldues the packages and versions I used, in case you'd like to set up a
virtual environment.

I mostly used the "Writing your first Django app" tutorial found
(here)[https://docs.djangoproject.com/en/3.0/intro/tutorial01/]. The project
structure follows the recommendations of the tutorial including the template
directory `es_proj/picosage/templates/picosage`. As I understand most of this
structure is trivial given Django's enforcement of it, but I am happy to expand on
this if needed.

The models contain the fields you mentioned and a couple extra to track events
like creation and modification. These seemed like the easiest way to add
functionality to the project. The models also use one third party field for
phone numbers. The views render templated html and err on the side of too-much
info.


## Admin Interface

Root uri: `/admin/`
User: `admin`
Pass: `admin`

All models are modifyable in the admin interface.


## Process

1. Project Environment
  - **Virtual Environment**
    Pyenv and virtualenv are used to isolate the current
    version of Django, the latest version of 3.7 and necessary modules.
2. Django Research
   My primary goals are:
   - Understand the project specifications w/r/t a Django app
     (https://docs.djangoproject.com/en/3.0/intro/overview/)
     - **Database Model:** A Series of model.Model objects which desribe the
       database in python.
     - **View:** Reutrns an HTTPResponse (or 404) and does whatever necessary to
       create the response. See Templates.
     - **Url Mappings:** A 'URLConf' will map/match paths to callbacks.
     - **Admin Config:** Django's default admin interface can be configured to
       allow edits of models.
     - **Templates:** html (or text,csv,etc?) with placeholders to be filled by
       django.
     - **(Bonus) Form:**
   - Find examples/references to create a bare minimum Django app
     (https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
3. Django tutorial After finding the tutorial, I was able to complete the
   requirements by walking through the tutorial and checking the assignment. I
   will leave the tutorial and revision history as evidence of my process.
