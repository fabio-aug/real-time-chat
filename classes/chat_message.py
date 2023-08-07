from flet import colors, CircleAvatar, FontWeight, Column, Text, Row

from classes.message import Message


def get_initials(user_name: str):
    return user_name[:1].capitalize()


def get_avatar_color(user_name: str):
    colors_lookup = [
        colors.RED,
        colors.CYAN,
        colors.BLUE,
        colors.PINK,
        colors.LIME,
        colors.TEAL,
        colors.BROWN,
        colors.GREEN,
        colors.AMBER,
        colors.INDIGO,
        colors.ORANGE,
        colors.PURPLE,
        colors.YELLOW,
    ]
    return colors_lookup[hash(user_name) % len(colors_lookup)]


class ChatMessage(Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment = "start"
        self.color = get_avatar_color(message.user_name)
        self.initial_letter = get_initials(message.user_name)
        self.controls = [
            CircleAvatar(
                color=colors.WHITE,
                bgcolor=self.color,
                content=Text(self.initial_letter),
            ),
            Column(
                [
                    Text(message.user_name, weight=FontWeight.W_700),
                    Text(message.text, selectable=True),
                ],
                tight=True,
                spacing=5,
            ),
        ]
