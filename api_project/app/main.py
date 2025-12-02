
from fastapi import FastAPI, Depends
from app.database import Base, engine
from app.routers import user, lead, agent, company, branch, onboarding
from app.utils.auth_user import get_current_user


app = FastAPI(title="EcomAgent API")


"""

 if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
"""


Base.metadata.create_all(bind=engine)

app.include_router(
    user.router
    )

app.include_router(
    lead.router,
    dependencies=[Depends(get_current_user)]
    )

app.include_router(
    agent.router,
    dependencies=[Depends(get_current_user)]
    )

app.include_router(company.router)
app.include_router(branch.router)

app.include_router(onboarding.router)



@app.get("/")
def root():
    return {"message": "EcomAgent first API is running"}
