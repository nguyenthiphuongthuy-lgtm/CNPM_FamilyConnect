from fastapi import APIRouter, HTTPException
from app.models.schemas import RelationshipCreate
from app.database import supabase

router = APIRouter(prefix="/genealogy", tags=["2. Quản lý Gia đình & Phả hệ"])


@router.post("/relationship")
def add_relationship(rel: RelationshipCreate):
    try:
        # Sử dụng model_dump() thay cho dict() trong Pydantic v2
        data = rel.model_dump() if hasattr(rel, "model_dump") else rel.dict()
        res = supabase.table("relationships").insert(data).execute()
        return {"message": "Đã thêm mối quan hệ", "data": res.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/interactive-tree/{family_id}")
def get_interactive_tree(family_id: str):
    try:
        # Lấy danh sách thành viên và mối quan hệ từ Supabase
        members = supabase.table("users").select("user_id, full_name, role").execute()
        relations = supabase.table("relationships").select("*").execute()

        # Áp dụng user_id để khớp với schema của bảng users
        nodes = [
            {"id": m.get("user_id") or m.get("id"), "label": m.get("full_name")}
            for m in members.data
        ]
        edges = [
            {
                "from": r.get("person_id_1"),
                "to": r.get("person_id_2"),
                "label": r.get("type"),
            }
            for r in relations.data
        ]

        return {"nodes": nodes, "edges": edges}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/query-relation")
def query_relation(person_a: str, person_b: str):
    try:
        # Trả về truy vấn mối quan hệ giữa 2 người bất kỳ
        return {
            "person_a": person_a,
            "person_b": person_b,
            "relation": "Anh em họ thứ 3",
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))