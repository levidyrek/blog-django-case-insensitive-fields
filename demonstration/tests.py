from django.db import IntegrityError
from django.test import TestCase

from .models import TestModel


class CaseInsensitiveTests(TestCase):

    def setUp(self):
        self.test_model = TestModel.objects.create(
            name='test',
            email='test@test.com'
        )

    def test_unique_name(self):
        with self.assertRaises(IntegrityError):
            TestModel.objects.create(
                name='TeSt',
                email='test2@test.com'
            )

    def test_unique_email(self):
        with self.assertRaises(IntegrityError):
            TestModel.objects.create(
                name='test2',
                email='TeST@TeST.coM'
            )

    def test_filter(self):
        count = TestModel.objects.filter(
            name='TeST',
            email='tEST@TEsT.COM',
        ).count()
        self.assertEqual(count, 1)

    def test_get(self):
        try:
            TestModel.objects.get(
                name='TEsT',
                email='TEST@TesT.COM',
            )
        except TestModel.DoesNotExist:
            self.fail('get() failed to retrieve.')

    def test_contains(self):
        count = TestModel.objects.filter(
            name__contains='TEs',
            email__contains='tES',
        ).count()
        self.assertEqual(count, 1)

    def test_startswith(self):
        count = TestModel.objects.filter(
            name__startswith='TeS',
            email__startswith='TEs',
        ).count()
        self.assertEqual(count, 1)

    def test_endswith(self):
        count = TestModel.objects.filter(
            name__endswith='eST',
            email__endswith='.COm',
        ).count()
        self.assertEqual(count, 1)

    def test_regex(self):
        count = TestModel.objects.filter(
            name__regex='TeST',
            email__regex='TEST@TESt.COM',
        ).count()
        self.assertEqual(count, 1)
