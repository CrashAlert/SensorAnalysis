import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Base, User, SensorSession, SensorData

class TestDB(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.DBsession = sessionmaker(self.engine)

    def test_user(self):
        # setup user and relationship
        user = User(name='username')
        sess = SensorSession()
        sess.user = user

        # commit to database
        session = self.DBsession()
        session.add_all([user, sess])
        session.commit()

        assert user.name == 'username'
        assert user.id is not None
        assert sess.id is not None
        assert sess.created is not None
        assert sess.user_id == user.id


