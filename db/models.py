from sqlalchemy import Column, Integer, String, Float
from database import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    category_main_cb = Column(Integer, index=True)
    category_sub_cb = Column(Integer, index=True)
    category_type_cb = Column(Integer, index=True)
    locality_region_id = Column(Integer, index=True)
    locality_district_id = Column(Integer, index=True)
    price = Column(Integer)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

