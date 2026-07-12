from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "BlueDepth",
        "version": "0.1.0"
    }