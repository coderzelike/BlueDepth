from fastapi import APIRouter

router = APIRouter(prefix="/dives", tags=["Dives"])


@router.get("/")
def get_dives():
    return []