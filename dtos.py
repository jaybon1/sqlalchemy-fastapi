from pydantic import BaseModel

class ResponseDTO(BaseModel):
    code: int
    message: str
    data: object | None

class RequestInsertRegionDTO(BaseModel):
    regionName : str

class ResponseInsertRegionDTO(BaseModel):
    regionId : int
    regionName : str

    class Config:
        orm_mode = True