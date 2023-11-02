from django.test import TestCase
from django.contrib.auth.models import User
from .models import Thread, Message

# Create your tests here.
class ThreadTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'test1111')
        self.user2 = User.objects.create_user('user2', None, 'test2222')
        self.user3 = User.objects.create_user('user3', None, 'test2222')

        self.thread = Thread.objects.create()

    # creamos el test (tiene que empezar con 'test_')
    def test_add_users_to_thread(self):
        self.thread.users.add(self.user1, self.user2) # creamos el Thread
        self.assertEqual(len(self.thread.users.all()), 2) # ¿hay 2 users?

    def test_filter_thread_by_users(self):
        self.thread.users.add(self.user1, self.user2) # creamos el Thread
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2) # doble filtro
        self.assertEqual(self.thread, threads[0])
    
    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2) # doble filtro
        self.assertEqual(len(threads), 0)

    def test_add_messages_to_thread(self):
        self.thread.users.add(self.user1, self.user2) # creamos el Thread
        message1 = Message.objects.create(user=self.user1, content='Hola!')
        message2 = Message.objects.create(user=self.user2, content='Hola, cómo andas?')
        self.thread.messages.add(message1, message2)
        self.assertEqual(len(self.thread.messages.all()), 2)

        for message in self.thread.messages.all():
            print("({}): {}".format(message.user, message.content))
    
    def test_add_message_from_user_not_in_thread(self):
        self.thread.users.add(self.user1, self.user2) # creamos el Thread
        message1 = Message.objects.create(user=self.user1, content='Hola!')
        message2 = Message.objects.create(user=self.user2, content='Hola, cómo andas?')
        message3 = Message.objects.create(user=self.user3, content='Soy un espía..')
        self.thread.messages.add(message1, message2, message3)
        self.assertEqual(len(self.thread.messages.all()), 2)