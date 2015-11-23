from django.test import TestCase
from login.models import Users
from login.models import User_Profiles
from login import oauth
from login import auth
from login import google
import random
import string

class UUIDTestCase(TestCase):
    def pesudo_random_string_generator(self):
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))

    def setUp(self):
        self.dummyuser = Users.objects.create(uuid="00000000-0000-0000-C000-000000000046", login_service="dummy", access_token="dummy")
        self.dummyuser2 = Users.objects.create(uuid="6a8f7800-91ba-11e5-af58-0002a5d5c51b", login_service="dummy", access_token="dummy")
        self.dummyprofile = User_Profiles.objects.create(user=self.dummyuser, username="dummy", email="admin@mail.ncku.edu.tw", default_shipping_address="nowhere", phone_number="0000000000", tw_id="A123456789", real_name="DUMMY")

    def test_validate_uuid(self):
        self.assertEqual(auth.validate_uuid4("00000000-0000-0000-C000-000000000046"), True)
        self.assertEqual(auth.validate_uuid4("576a5880-91ba-11e5-833f-0002a5d5c51b"), True)
        self.assertEqual(auth.validate_uuid4("6a8f7800-91ba-11e5-af58-0002a5d5c51b"), True)
        self.assertEqual(auth.validate_uuid4("79d4c540-91ba-11e5-a9ec-0002a5d5c51b"), True)

        #Test Different Format
        self.assertEqual(auth.validate_uuid4("00000000-0000-0000-C000-000000000046"), True)
        self.assertEqual(auth.validate_uuid4("0000000000000000C000000000000046"), True)

        #Test Broken UUIDs
        self.assertEqual(auth.validate_uuid4("00000000-0000-0000-C000-00000000004"), False)
        self.assertEqual(auth.validate_uuid4("0000000000000000C00000000000004"), False)
        self.assertEqual(auth.validate_uuid4("00000000-0000-C000-000000000046"), False)
        self.assertEqual(auth.validate_uuid4("000000000000C000000000000046"), False)

    def test_generate_static_uuid(self):
        self.assertEqual(auth.validate_uuid4(auth.generate_static_uuid(self.pesudo_random_string_generator())), True)
        secret = self.pesudo_random_string_generator()
        self.assertEqual(auth.generate_static_uuid(secret), auth.generate_static_uuid(secret))

    def test_generate_random_uuid(self):
        self.assertEqual(auth.validate_uuid4(auth.generate_random_uuid()), True)
        self.assertNotEqual(auth.generate_random_uuid(), auth.generate_random_uuid())

    def test_has_functions(self):
        self.assertEqual(auth.hasUser("00000000-0000-0000-C000-000000000046"), True)
        self.assertEqual(auth.hasUser("6a8f7800-91ba-11e5-af58-0002a5d5c51b"), True)
        self.assertEqual(auth.hasUser("576a5880-91ba-11e5-833f-0002a5d5c51b"), False)

        self.assertEqual(auth.hasProfile("00000000-0000-0000-C000-000000000046"), True)
        self.assertEqual(auth.hasProfile("6a8f7800-91ba-11e5-af58-0002a5d5c51b"), False)
        self.assertEqual(auth.hasProfile("576a5880-91ba-11e5-833f-0002a5d5c51b"), False)

    def test_create_user(self):
        self.assertEqual(auth.hasUser("79d4c540-91ba-11e5-a9ec-0002a5d5c51b"), False)

        uuid = auth.create_empty_user("79d4c540-91ba-11e5-a9ec-0002a5d5c51b", "dummy", "dummy")

        self.assertEqual(uuid, "79d4c540-91ba-11e5-a9ec-0002a5d5c51b")
        self.assertEqual(auth.hasUser("79d4c540-91ba-11e5-a9ec-0002a5d5c51b"), True)

    def test_register_profile(self):
        profile = User_Profiles(username="dummy", email="admin@mail.ncku.edu.tw", default_shipping_address="nowhere", phone_number="0000000000", tw_id="A123456789", real_name="DUMMY")
        auth.register_data("6a8f7800-91ba-11e5-af58-0002a5d5c51b", profile)
        self.assertEqual(auth.hasProfile("6a8f7800-91ba-11e5-af58-0002a5d5c51b"), True)


