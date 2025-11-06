
from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth

app = FastAPI(title="EcomAgent API")


"""

 if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
"""


Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

