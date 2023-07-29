import unittest
from classes.message import Message
from classes.chat_message import ChatMessage, get_avatar_color, get_initials


class ChatMessageTests(unittest.TestCase):

    def test_username(self):
        message = Message("user_name", "text_message", "chat_message")
        message_render = ChatMessage(message)

        self.assertEqual(get_avatar_color(message.user_name), message_render.color)
        self.assertEqual(get_initials(message.user_name), message_render.initial_letter)


if __name__ == '__main__':
    unittest.main()
