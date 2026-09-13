from fastapi import APIRouter
from app.models.schemas import PostCreate, CommentCreate
from app.database import supabase

router = APIRouter(prefix="/community", tags=["3. Cộng đồng"])

@router.post("/posts")
def create_post(user_id: str, post: PostCreate):
    data = {"user_id": user_id, "content": post.content, "image_url": post.image_url}
    res = supabase.table("posts").insert(data).execute()
    return {"message": "Tạo bài viết thành công", "data": res.data}

@router.post("/comments")
def add_comment(user_id: str, comment: CommentCreate):
    data = {"user_id": user_id, "post_id": comment.post_id, "content": comment.content}
    res = supabase.table("comments").insert(data).execute()
    return {"message": "Đã thêm bình luận", "data": res.data}

@router.get("/notifications/{user_id}")
def get_notifications(user_id: str):
    res = supabase.table("notifications").select("*").eq("user_id", user_id).execute()
    return {"notifications": res.data}