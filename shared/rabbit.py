import json


class SenderMessage:
    def __init__(
        self,
        action: str,
        user_id: int,
        digest_id: int,
        inform_empty: bool,
        offset: int,
        message_id: int
    ):
        self.action = action
        self.user_id = user_id
        self.digest_id = digest_id
        self.inform_empty = inform_empty
        self.offset = offset
        self.message_id = message_id

    @classmethod
    def from_bytes(cls, bytestr: bytes):
        data = json.loads(bytestr.decode('utf-8'))
        return cls(
            action=data['action'],
            user_id=int(data['user_id']),
            digest_id=int(data['digest_id']),
            inform_empty=data['inform_empty'],
            offset=int(data['offset']),
            message_id=int(data['message_id']),
        )

    def __bytes__(self):
        data = {
            'action': self.action,
            'user_id': self.user_id,
            'digest_id': self.digest_id,
            'inform_empty': self.inform_empty,
            'offset': self.offset,
            'message_id': self.message_id,
        }
        return json.dumps(data).encode()

    def __str__(self):
        action = f'action={self.action}'
        user_id = f'user_id={self.user_id}'
        digest_id = f'digest_id={self.digest_id}'
        offset = f'offset={self.offset}'
        message_id = f'message_id={self.message_id}'
        inform_empty = f'inform_empty={self.inform_empty}'
        return f'SenderMessage[{action}, {user_id}, {digest_id}, {offset}, {message_id}, {inform_empty}]'


class SummaryMessage:
    def __init__(self, channel_username: str, post_id: int, text: str):
        self.channel_username = channel_username
        self.post_id = post_id
        self.text = text

    @classmethod
    def from_bytes(cls, bytestr: bytes):
        data = json.loads(bytestr.decode('utf-8'))
        return cls(
            channel_username=data['channel_username'],
            post_id=int(data['post_id']),
            text=data['text'],
        )

    def __bytes__(self):
        data = {
            'channel_username': self.channel_username,
            'post_id': self.post_id,
            'text': self.text,
        }
        return json.dumps(data).encode()

    def __str__(self):
        channel_username = f'channel_username={self.channel_username}'
        post_id = f'post_id={self.post_id}'
        text = f'text={self.text}'
        return f'SummaryMessage[{channel_username}, {post_id}, {text}]'
