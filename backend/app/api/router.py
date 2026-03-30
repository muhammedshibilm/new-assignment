from fastapi import APIRouter, Depends, HTTPException, status

from app.routers import auth, projects, tasks, users

router = APIRouter()

# include all sub-routers
router.include_router(auth.router)
router.include_router(users.router)
router.include_router(projects.router)
router.include_router(tasks.router)