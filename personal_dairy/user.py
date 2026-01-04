class User:
    total_user_connected = 0

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
        # start count total user
        User.total_user_connected += 1

    # if authen() = true...login else wrong credential

    def authenticate(self, pwd):

        return self.__password == pwd

    def __str__(self):
        return f"User name: {self.username} \n Email : {self.email} \n User Connected : {User.total_user_connected}"
    # def get_password(self):
    #     return self.__password

# login requiered
