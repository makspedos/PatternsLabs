from user import User

if __name__ == '__main__':
    user1 = User("test1")


    user1.select_storage("local")
    print(user1.storage)
    user1.select_storage("local")
    print(user1.storage)


    user1.storage.upload(r"test.png",r'C:\Users\Maksim\PycharmProjects\lab1_singleton\img',  )
    user1.storage.download(r"C:\Users\Maksim\PycharmProjects\lab1_singleton\img\test2.png")
    user1.storage.delete(r"C:\Users\Maksim\PycharmProjects\lab1_singleton\img\test3.png")

    user2 = User("test2")
    user2.select_storage("amazon")
    print(user2.storage)
    user2.select_storage("amazon")
    print(user2.storage)
