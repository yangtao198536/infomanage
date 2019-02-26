import os

class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_MAIL_SUBJECT_PREFIX = 'Webdev'
    FLASKY_MAIL_SENDER = 'wangli@wicent.com'
    FLASKY_ADMIN = '3123093309@qq.com'
    DEBUG = True
    MAIL_SERVER = 'smtp.exmail.qq.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'wangli@wicent.com'
    MAIL_PASSWORD = 'Wl123456'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1/myweb'
    SCHEDULER_API_ENABLED = True
    use_reloader=False
    UPLOADED_FILE_DEST = '/Users/root1/webdev/fileloads'
    SCRIPT_LOCAL_PATH = '/Users/root1/webdev/script'

    @staticmethod
    def init_app(app):
        pass


config = {'default':Config}
