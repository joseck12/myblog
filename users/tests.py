from django.test import TestCase
from .models import Profile
from whatever.models import Whatever
from django.utils import timezone
from django.core.urlresolvers import reverse
from whatever.forms import WhateverForm

class ProfileTestClass(TestCase):

    def setUp(self):
        self.joseck = Profile()
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.joseck,Profile))
    #testing save method
    def test_save_method(self):
        self.joseck.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
