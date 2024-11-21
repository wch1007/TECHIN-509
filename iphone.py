class Message:
    def __init__(self, content, timestamp, sender):
        self.content = content
        self.timestamp = timestamp
        self.sender = sender
        self.is_read = False       
    def check_is_read(self):
        return self.is_read
    def mark_as_read(self):
        self.is_read = True


class iPhone:
    def __init__(self, name, model, version, color, phone_num, pw): # constructor
        self.name = name
        self.model = model
        self.version = version
        self.color = color
        self.password = pw
        self.files = []
        self.messages = []

    def send_imessage(self, receipt, content, timestamp):
        message = Message(content = content, sender = self.name, timestamp = timestamp)
        receipt.messages.append(message)
        print(f"{self.name} send {receipt.name} an iMessage at {timestamp}, which says:\n{content}")
        pass

    def check_imessage(self):
        print(f"{self.name}'s iMessages:")
        if not self.messages:
            print("No messages.")
        for i, msg in enumerate(self.messages, 1):
            status = "Read" if msg.check_is_read() else "Unread"
            print(f"{i}. From: {msg.sender}, Content: '{msg.content}', Time: {msg.timestamp}, Status: {status}")
            msg.mark_as_read()
        pass


    # these are the methods and actions of this object
    def airdrop(self, filename, recipient):
        print(f"Dropping {filename} to {recipient}.")
        pass
    
    def receive(self, filename, sender):
        print(f"Recieved {filename} from {sender}.")
        pass

    def update_ver(self, version, new_version):
        self.version = new_version
        print(f"Updated IOS into {new_version}.")

# Instead of simply Caelens_iphone.name = ... we use def
    def set_name(self,new_name):
        if len(new_name) < 3:
            print("Name must be longer than 3 letters.")
        self.name = new_name
        print(f"Set name to {new_name}")



Caelens_iphone = iPhone(name = "Caelen's iPhone", model = "iPhone 15 Pro Max", version = "17.6.1", color = "silver", phone_num = "4255364595", pw = "123456")
Ians_iphone = iPhone(name = "Ian's iPhone", model = "iPhone 16 Pro Max", version = "17.6.1", color = "black", phone_num = "1231234567", pw = "123456")
print(Caelens_iphone.name)
Caelens_iphone.airdrop("notes.pdf","Ian's iPhone")
Caelens_iphone.set_name("Caelen")
Caelens_iphone.send_imessage(Ians_iphone, "Hello, Ian! Can I get a full score?", "2024-11-20 8:30 PM")
Ians_iphone.check_imessage()
Caelens_iphone.send_imessage(Ians_iphone, "Just kidding. Happy weekend, professor!", "2024-11-20 8:33 PM")
Ians_iphone.check_imessage()

