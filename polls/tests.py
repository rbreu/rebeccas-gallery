from datetime import datetime
from django.test import TestCase
from polls.models import Poll, Choice
from django.test import Client


class PollTest(TestCase):

    def setUp(self):
        question="What is your favourite colour?"
        now = datetime.now()
        self.poll = Poll.objects.create(question=question, published_at=now)
        self.poll.choice_set.create(choice="Red", votes=0)
        self.poll.choice_set.create(choice="Blue", votes=0)
        self.poll.choice_set.create(choice="Green", votes=0)

    def test_models(self):
        self.assertEqual(self.poll.choice_set.all().count(), 3)
        
    def test_voting(self):
        c = Client()
        # Perform a vote on the poll by mocking a POST request.
        response = c.post('/polls/1/vote/', {'choice': '1',})
        # In the vote view we redirect the user, so check the 
        # response status code is 302.
        self.assertEqual(response.status_code, 302)
        # Get the choice and check there is now one vote.
        choice = Choice.objects.get(pk=1)
        self.assertEqual(choice.votes, 1)
