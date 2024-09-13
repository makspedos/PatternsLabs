from factory import Factory


if __name__ == '__main__':
    factory = Factory()
    network = factory.factory_method(email="Max", password="12345")
    message = network.create_message()
    message.post("Hi, I'm Max")

    network = factory.factory_method(login="Max", password="12345")
    message = network.create_message()
    message.post("Hi, I'm Max")
