from typing import List
from app.core.base_db import DB

module_name = 'sample'
module_text = 'Sample'


class Sample(DB):
    f"""
    Use this model to manage a {module_text}
    """

    def __init__(self, _id=None, module_name=module_name, module_text=module_text, db=None,
                 name=''):
        self._id: str = _id
        self.name: str = name
        super().__init__(_id=_id, module_name=module_name, module_text=module_text, db=db)

    def list(self, query=None) -> List['Sample']:
        return super().list(query=query)
