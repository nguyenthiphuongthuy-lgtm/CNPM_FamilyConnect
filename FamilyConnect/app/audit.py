from app.database import supabase

def log_audit_event(user_id: str, action: str, details: str = None):
    """Hàm ghi lại lịch sử thao tác người dùng (Audit Log)."""
    try:
        data = {
            "user_id": user_id,
            "action": action,
            "details": details
        }
        supabase.table("audit_logs").insert(data).execute()
    except Exception as e:
        print(f"Lỗi ghi log audit: {e}")