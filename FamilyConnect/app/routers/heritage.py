from fastapi import APIRouter
from app.models.schemas import StoryCreate
from app.database import supabase

router = APIRouter(prefix="/heritage", tags=["6. Di sản Gia đình"])

@router.post("/stories")
def add_family_story(story: StoryCreate):
    res = supabase.table("stories").insert(story.dict()).execute()
    return {"message": "Đã lưu câu chuyện gia đình", "data": res.data}

@router.get("/archive")
def get_digital_archive():
    documents = supabase.table("heritage_docs").select("*").execute()
    return {"documents": documents.data}