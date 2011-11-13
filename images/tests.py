from images.models import Image
import nose.tools as nt
from django.test import Client


class TestImage(object):

    def setup(self):
	self.image = Image(title="Hellow World",
                           description="My first test image. Yay!",
                           filename="test.png")


    def test_basic_save(self):
        self.image.save()

    def test_image_url(self):
        nt.assert_equal(self.image.image_url(), "/media/test.png")

    def test_thumb_url(self):
        nt.assert_equal(self.image.thumb_url(), "/media/test_thumbnail.png")



class TestImageView(object):
    
    def setup(self):
        self.client = Client()

        
    def test_image_index(self):
        response = self.client.get("/images/")
        nt.assert_in("Art by Date", response.content)

        
    def test_image_index(self):
        response = self.client.get("/images/tags/")
        nt.assert_in("Art by Tag", response.content)
