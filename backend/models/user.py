# User model pseudocode

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    tasks = relationship('Task', backref='owner')

    def verify_password(self, password):
        # Pseudocode for password verification
        pass
