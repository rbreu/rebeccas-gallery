from lettuce import *
from lettuce.django import django_url
from lettuce import world
from django.test.client import Client
import nose.tools as nt

@step(u'I visit the url "(.*)"$')
def i_visit_the_url(step, url):
    world.response = world.browser.visit(django_url(url))
    
@step(u'I should see "(.*)"$')
def i_should_see(step, content):
    nt.assert_in(content, world.browser.html)

@step(u'I should see the heading "(.*)"$')
def i_should_see(step, content):
    nt.assert_equal(content, world.browser.find_by_tag("h1").first.value)

@step(u'I follow "(.*)"$')
def when_i_follow_label(step, label):
    world.browser.click_link_by_text(label)
    
@step(u'And I should see the image "([^"]*)"')
def and_i_should_see_the_image_group1(step, name):
    nt.assert_true(world.browser.is_element_present_by_xpath(
            "//img[@src='/media/%s']" % name))
