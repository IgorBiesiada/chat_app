from channels.generic.websocket import WebsocketConsumer

class ChatRoomConsumer(WebsocketConsumer):
    def connect(self):
        return self.accept()