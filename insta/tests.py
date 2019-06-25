from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Comments,Image,Followers

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.ian=Profile(pic="img.png",bio="noddles",userId=1)
    def test_instance(self):
        self.assertTrue(isinstance(self.ian,Profile))

    def test_initialization(self):
        self.assertEqual(self.ian.pic,"img.png")
        self.assertEqual(self.ian.bio,"noodles")
        self.assertEqual(self.ian.userId,1)

    def test_save(self):
        self.ian.save_profile()
        prof=Profile.objects.all()
        self.assertTrue(len(prof)>0)

    def test_delete(self):
        self.ian.delete_profile()
        prof=Profile.objects.all()
        self.assertEqual(len(prof),0)

class TestImage(TestCase):
    def setUp(self):
        self.comment=Comments(images=1,comment='this is dope')
        self.follow=Followers(user="ian",insta='like',user_id=1)
        self.new_image=Image(image="image",name="amazing",caption="live",likes=0,userId=10)

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_instance_follow(self):
        self.assertTrue(isinstance(self.follow,Followers))

    def test_save(self):
        self.follow.save_followers()
        prof=Followers.objects.all()
        self.assertTrue(len(prof)>0)


    def test_image_save(self):
        self.new_image.save_image()
        prof=Image.objects.all()
        self.assertTrue(len(prof)>0)
        
