from datetime import datetime

from pydantic import BaseModel, HttpUrl

from typing import List, Dict, Literal, Any, Optional

class ShortenRequest(BaseModel):
    your_url: str
    custom_alias: Optional[str] = None
    expires_at: Optional[datetime] = None
