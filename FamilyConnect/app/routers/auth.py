from fastapi import APIRouter, HTTPException, status
from app.models.schemas import UserRegister
from app.database import supabase
from app.security import hash_password

router = APIRouter(prefix="/auth", tags=["1. Người dùng & Bảo mật"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserRegister):
    try:
        # 1. Kiểm tra email đã tồn tại chưa
        existing = supabase.table("users").select("*").eq("email", user.email).execute()
        if existing.data:
            raise HTTPException(status_code=400, detail="Email đã tồn tại!")

        # 2. Tạo dữ liệu người dùng mới khớp với bảng Supabase
        new_user = {
            "email": user.email,
            "password_hash": hash_password(user.password),
            "full_name": user.full_name,
            "role": user.role,
            "status": "Active"
        }
        
        # 3. Chèn vào database Supabase
        res = supabase.table("users").insert(new_user).execute()
        return {"message": "Đăng ký thành công", "data": res.data}
        
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))