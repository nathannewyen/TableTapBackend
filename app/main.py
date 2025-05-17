from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
from app.db.database import engine, Base
from app.routes import menu_routes, menu_items_routes

# Create tables in the database
Base.metadata.create_all(bind=engine)

settings = get_settings()
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development. In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(menu_routes.router)
app.include_router(menu_items_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Restaurant Food Ordering API"}