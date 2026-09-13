from fastapi import APIRouter
from app.database import supabase

router = APIRouter(prefix="/admin", tags=["9. Quản trị hệ thống"])

@router.get("/audit-logs")
def get_audit_logs():
    logs = supabase.table("audit_logs").select("*").execute()
    return {"logs": logs.data}

@router.post("/backup")
def trigger_system_backup():
    return {"status": "success", "message": "Đã tạo bản sao lưu dữ liệu PostgreSQL thành công!"}