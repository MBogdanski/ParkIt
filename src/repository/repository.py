from pydantic import BaseModel


class Repository(BaseModel):
    def add(self, entity):
        raise NotImplementedError

    def update(self, entity):
        raise NotImplementedError

    def delete(self, entity_id):
        raise NotImplementedError

    def get(self, entity_id):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError
