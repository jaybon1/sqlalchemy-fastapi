from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from fastapi.middleware.cors import CORSMiddleware

import services, entitys, dtos
from database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/regions")
def select_regions(db: Session = Depends(get_db)):
    regions = services.select_regions(db)
    return regions

@app.get("/region/{region_id}")
def select_regions(region_id : int, db: Session = Depends(get_db)):
    region = services.select_region_by_id(db, region_id)
    return region

@app.post("/insert-region")
def inert_region(requestInsertRegionDTO : dtos.RequestInsertRegionDTO , db: Session = Depends(get_db)):
    region = services.insert_region(db, requestInsertRegionDTO)
    return region