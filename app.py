"Main app"


from fastapi import FastAPI

from survey.api import router
from survey.upload import router as upload_router
from survey.response import router as response

app = FastAPI()

app.include_router(router)
app.include_router(upload_router)
app.include_router(response)
