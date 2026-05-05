from pydantic import BaseModel
from typing import List

class BulkUpsertRequest(BaseModel):
    items: List[dict]