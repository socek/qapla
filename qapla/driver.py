class BaseDriver(object):
    model = None

    def __init__(self, database):
        self.database = database

    def query(self):
        return self.database.query(self.model)


class ReadDriver(BaseDriver):

    def get_by_id(self, id):
        return self.query().filter(self.model.id == id).one()

    def list_all(self):
        return self.query().all()


class WriteDriver(BaseDriver):

    def create(self, **kwargs):
        obj = self.model()
        for key, value in kwargs.items():
            setattr(obj, key, value)

        self.database.add(obj)
        self.database.commit()
        return obj
