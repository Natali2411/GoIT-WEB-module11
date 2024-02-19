from fastapi import FastAPI

from src.routes import contacts, channels, contacts_channels

app = FastAPI()

app.include_router(contacts.router, prefix='/api')
app.include_router(channels.router, prefix='/api')
app.include_router(contacts_channels.router, prefix='/api')

#
# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}

