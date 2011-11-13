from lettuce import *
from lettuce.django import django_url
from lettuce import world
from django.test.client import Client
import nose.tools as nt
from images.models import Image

@step(u'the image "(.*)" exists$')
def an_image_with_title_exists(step, title):
    image = Image(title=title,
                  filename=title.replace(" ", "_").lower() + ".png",
                  description=title + " description")
    image.save()
    
    
@step(u'I should see the image title "(.*)"$')
def i_should_see(step, title):
    nt.assert_equal(title, world.browser.find_by_css("a.title").first.value)


@step(u'I should see the image description "(.*)"$')
def i_should_see(step, description):
    nt.assert_equal(description, world.browser.find_by_css("p.description").first.value)
