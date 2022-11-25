from sqlalchemy.orm import Session
import entitys, dtos

def select_regions(db: Session):
    
    return Session.db.query(entitys.Regions).all()

def select_region_by_id(db : Session, region_id : int):
    return Session.db.query(entitys.Regions).all().filter(entitys.Regions.REGION_ID == region_id).first()

def insert_region(db: Session, requestInsertRegionDTO : dtos.RequestInsertRegionDTO):
    region = entitys.Regions(REGION_NAME=requestInsertRegionDTO.regionName)
    db.add(region)
    # db.flush()
    # db.commit()
    # db.refresh(region)
    return region


