from fastapi import FastAPI
from app.routes import user, task
from app.database import Base, engine

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

# Including API routers
app.include_router(user.router, prefix="/api/users", tags=["Users"])
app.include_router(task.router, prefix="/api/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "Task Manager API is running"}
