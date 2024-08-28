# Project model pseudocode

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    tasks = relationship('Task', backref='project')

    def add_task(self, task):
        # Pseudocode for adding a task to the project
        pass
