from fastapi import APIRouter

router = APIRouter(prefix="/analytics", tags=["8. Bảng điều khiển & Thống kê"])

@router.get("/dashboard")
def get_dashboard_data():
    return {
        "total_members": 120,
        "active_posts": 45,
        "upcoming_events": 3,
        "demographics": {"male": 60, "female": 55, "other": 5}
    }

@router.get("/generate-report")
def generate_family_report():
    return {"report_url": "https://supabase.co/storage/v1/object/public/reports/family_summary.pdf"}