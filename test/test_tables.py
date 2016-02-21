import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.tables import Base, User, SensorSession, SensorData

class TestDB(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.DBsession = sessionmaker(self.engine)

    def test_user_x_session(self):
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

    def test_session_x_data(self):
        # commit objects
        user = User(name='username')
        sess = SensorSession()
        sess.user = user
        data = SensorData(nano_time=1)
        data.session = sess
        # commit to database
        session = self.DBsession()
        session.add_all([user, sess, data])
        session.commit()

        assert sess.id is not None
        assert sess.created is not None
        assert data.session_id == sess.id
        assert data.session == sess
        assert data.nano_time == 1

if __name__ == '__main__':
    unittest.main()
