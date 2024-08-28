# Task model pseudocode

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, default='pending')
    project_id = Column(Integer, ForeignKey('projects.id'))
    owner_id = Column(Integer, ForeignKey('users.id'))

    def update_status(self, new_status):
        # Pseudocode for updating task status
        pass
