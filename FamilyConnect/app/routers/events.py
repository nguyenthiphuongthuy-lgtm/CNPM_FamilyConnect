from fastapi import APIRouter
from app.models.schemas import EventCreate, RSVPUpdate
from app.database import supabase

router = APIRouter(prefix="/events", tags=["4. Sự kiện"])

@router.post("/create")
def create_event(event: EventCreate):
    res = supabase.table("events").insert(event.dict()).execute()
    return {"message": "Tạo sự kiện gia đình thành công", "data": res.data}

@router.post("/rsvp")
def update_rsvp(user_id: str, rsvp: RSVPUpdate):
    data = {"user_id": user_id, "event_id": rsvp.event_id, "status": rsvp.status}
    res = supabase.table("event_rsvps").upsert(data).execute()
    return {"message": "Cập nhật RSVP thành công", "data": res.data}

@router.get("/reminders/{user_id}")
def get_event_reminders(user_id: str):
    return {"reminders": ["Sự kiện Giỗ Tổ vào cuối tuần này", "Sinh nhật Chú B đợt tới"]}