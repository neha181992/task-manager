from fastapi import FastAPI
from .routes import auth, projects, tasks
from .sockets import socket_manager

app = FastAPI()

app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(tasks.router)

socket_manager.setup(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
