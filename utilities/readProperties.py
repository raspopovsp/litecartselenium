import configparser

config = configparser.RawConfigParser()
config.read("./configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('common info', 'baseUrl')

    @staticmethod
    def get_username():
        return config.get('common info', 'username')

    @staticmethod
    def get_password():
        return config.get('common info', 'password')

    @staticmethod
    def get_admin_url():
        return config.get('admin info', 'adminUrl')

    @staticmethod
    def get_admin_login():
        return config.get('admin info', 'login')

    @staticmethod
    def get_admin_password():
        return config.get('admin info', 'password')
