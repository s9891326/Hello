from typing import Optional

from fastapi import HTTPException
from fastapi.params import Header


class PaginationParms:
    def __init__(self, keyword: Optional[str] = None, last: int = 0, limit: int = 50):
        self.keyword = keyword
        self.last = last
        self.limit = limit


def pagination_params(keyword: Optional[str] = None, last: int = 0, limit: int = 50):
    return {"keyword": keyword, "last": last, "limit": limit}


def verify_token(verify_header: str = Header()):
    if verify_header != "secret-token":
        raise HTTPException(status_code=403, detail="Forbidden")
    return verify_header
