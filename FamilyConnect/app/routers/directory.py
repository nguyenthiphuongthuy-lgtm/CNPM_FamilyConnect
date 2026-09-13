from fastapi import APIRouter, Query
from typing import Optional
from app.database import supabase

router = APIRouter(prefix="/directory", tags=["5. Danh bạ Gia đình"])

@router.get("/search")
def search_members(
    occupation: Optional[str] = Query(None),
    location: Optional[str] = Query(None),
    generation: Optional[int] = Query(None)
):
    query = supabase.table("users").select("*")
    if occupation:
        query = query.ilike("occupation", f"%{occupation}%")
    if location:
        query = query.ilike("location", f"%{location}%")
    res = query.execute()
    return {"results": res.data}