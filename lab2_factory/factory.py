from networks import FacebookConnection, LinkedInConnection


class Factory:
    def factory_method(self, password: str, login: str | None = None, email: str | None = None):
        if login and email:
            raise ValueError("Please provide either login or email, not both.")

        if login:
            social_media = FacebookConnection(login=login, password=password)
        elif email:
            social_media = LinkedInConnection(email=email, password=password)
        else:
            raise ValueError("Connection failed: Either login or email must be provided.")
        return social_media
