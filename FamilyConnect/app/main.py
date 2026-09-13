import uuid
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import kết nối Supabase dùng chung từ database.py
from app.database import supabase

# Import các router chức năng
from app.routers import (
    admin,
    ai_router,
    analytics,
    auth,
    community,
    directory,
    events,
    genealogy,
    heritage,
)

app = FastAPI(
    title="FamilyConnect API Enterprise",
    description="Hệ thống API Quản lý Gia đình Toàn diện",
    version="2.0.0",
)

# Cho phép Frontend truy cập API từ bất kỳ nguồn nào
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic Schemas
class UserCreate(BaseModel):
    username: str | None = None
    email: str
    password_hash: str
    full_name: str | None = None


class UserLogin(BaseModel):
    email: str
    password_hash: str


# --- ROOT & HEALTH CHECK ENDPOINTS ---
@app.get("/")
def read_root():
    return {"message": "Chào mừng đến với FamilyConnect API!"}


@app.get("/users")
def get_users():
    response = supabase.table("users").select("*").execute()
    return {"data": response.data}


@app.post("/users")
def create_user(user: UserCreate):
    try:
        data_to_insert = {
            "user_id": str(uuid.uuid4()),
            "email": user.email,
            "password_hash": user.password_hash,
            "full_name": user.full_name,
            "status": "Active",
            "is_verified": False,
        }

        if user.username:
            data_to_insert["username"] = user.username

        response = supabase.table("users").insert(data_to_insert).execute()
        return {"message": "Tạo người dùng thành công!", "data": response.data}
    except Exception as e:
        print(">>> LỖI CHI TIẾT:", e)
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/login")
def login(user: UserLogin):
    try:
 
        response = (
            supabase.table("users")
            .select("*")
            .eq("email", user.email)
            .eq("password_hash", user.password_hash)
            .execute()
        )

        # 2. Nếu không tìm thấy dòng nào khớp -> Báo lỗi
        if len(response.data) == 0:
            raise HTTPException(
                status_code=400, detail="Sai email hoặc mật khẩu!"
            )

        # 3. Nếu đúng -> Trả về thông tin người dùng
        return {
            "message": "Đăng nhập thành công!",
            "user": response.data[0],
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/test-db")
def test_db_connection():
    try:
        res = supabase.table("users").select("*").limit(1).execute()
        return {
            "status": "connected",
            "message": "Kết nối Supabase thành công!",
            "data": res.data,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": "Kết nối Supabase thất bại",
            "detail": str(e),
        }


# --- ĐĂNG KÝ TOÀN BỘ 9 NHÓM ROUTER CHỨC NĂNG ---
app.include_router(auth.router)
app.include_router(genealogy.router)
app.include_router(community.router)
app.include_router(events.router)
app.include_router(directory.router)
app.include_router(heritage.router)
app.include_router(ai_router.router)
app.include_router(analytics.router)
app.include_router(admin.router)