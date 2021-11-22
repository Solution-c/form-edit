"Main app"


from fastapi import FastAPI

from survey.api import router

app = FastAPI()

app.include_router(router)