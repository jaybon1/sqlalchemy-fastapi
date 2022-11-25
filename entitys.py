from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base

class Regions(Base):
    __tablename__ = "REGIONS"

    REGION_ID = Column(Integer, primary_key=True, index=True)
    REGION_NAME = Column(String)

