from django.test import TestCase
from .models import MemoCard


class ModelCardTestCase(TestCase):
    """ This class defines the test suite for the game model."""

    def setUp(self):

        self.memo_card_name = "Dog1"
        self.memocard = MemoCard(name=self.memo_card_name)

    def test_model_can_create_a_memocard(self):
        """ Test the game model can create a memocard """
        old_count = MemoCard.objects.count()
        self.memocard.save()
        new_count = MemoCard.objects.count()
        self.assertNotEqual(old_count, new_count)

