from lettuce import *
from lettuce.django import django_url
from lettuce import world
from django.test.client import Client
import nose.tools as nt

@before.all
def set_browser():
    world.client = Client()

@step(u'When I visit the url "(.*)"')
def when_i_visit_the_url(step, url):
    world.response = world.client.get(django_url(url))
    
@step(u'Then I should see "(.*)"')
def then_i_should_see(step, content):
    nt.assert_in(content, world.response.content.decode("utf-8"))
