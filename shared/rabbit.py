import json


class SenderMessage:
    def __init__(
        self,
        action: str,
        news_id: int,
        inform_empty: bool,
        offset: int,
        message_id: int
    ):
        self.action = action
        self.news_id = news_id
        self.inform_empty = inform_empty
        self.offset = offset
        self.message_id = message_id

    @classmethod
    def from_bytes(cls, bytestr: bytes):
        data = json.loads(bytestr.decode('utf-8'))
        return cls(
            action=data['action'],
            news_id=int(data['news_id']),
            inform_empty=data['inform_empty'],
            offset=int(data['offset']),
            message_id=int(data['message_id']),
        )

    def __bytes__(self):
        data = {
            'action': self.action,
            'news_id': self.news_id,
            'inform_empty': self.inform_empty,
            'offset': self.offset,
            'message_id': self.message_id,
        }
        return json.dumps(data).encode()

    def __str__(self):
        action = f'action={self.action}'
        news_id = f'news_id={self.news_id}'
        offset = f'offset={self.offset}'
        message_id = f'message_id={self.message_id}'
        inform_empty = f'inform_empty={self.inform_empty}'
        return f'SenderMessage[{action}, {news_id}, {offset}, {message_id}, {inform_empty}]'


class SummaryMessage:
    def __init__(self, title_en: str, text: str):
        self.title_en = title_en
        self.text = text

    @classmethod
    def from_bytes(cls, bytestr: bytes):
        data = json.loads(bytestr.decode('utf-8'))
        return cls(
            title_en=data['title_en'],
            text=data['text'],
        )

    def __bytes__(self):
        data = {
            'title_en': self.title_en,
            'text': self.text,
        }
        return json.dumps(data).encode()

    def __str__(self):
        title_en = f'title_en={self.title_en}'
        text = f'text={self.text}'
        return f'SummaryMessage[{title_en}, {text}]'
