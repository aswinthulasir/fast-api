from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL='postgresql://<username>:<password>@ip-address/host_name>/<database_name>'

SQLALCHEMY_DATABASE_URL='postgresql://postgres:Aswin2000@ip-address/localhost/<fastapi_database>'

engine=create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False, bind=engine)
Base=declarative_base()