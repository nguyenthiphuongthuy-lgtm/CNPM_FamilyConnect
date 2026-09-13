from pydantic import BaseModel, EmailStr
from typing import Optional, List
from enum import Enum

# --- ENUMS (RBAC & Roles) ---
class UserRole(str, Enum):
    ADMIN = "admin"
    FAMILY_HEAD = "family_head"
    MEMBER = "member"

class RelationshipType(str, Enum):
    PARENT_CHILD = "parent_child"
    SPOUSE = "spouse"

# --- AUTH & USER SCHEMAS ---
class UserRegister(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    role: Optional[UserRole] = UserRole.MEMBER

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserProfileUpdate(BaseModel):
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    occupation: Optional[str] = None
    education: Optional[str] = None
    location: Optional[str] = None

# --- GENEALOGY SCHEMAS ---
class RelationshipCreate(BaseModel):
    person_id_1: str
    person_id_2: str
    type: RelationshipType

# --- COMMUNITY SCHEMAS ---
class PostCreate(BaseModel):
    content: str
    image_url: Optional[str] = None

class CommentCreate(BaseModel):
    post_id: str
    content: str

# --- EVENT SCHEMAS ---
class EventCreate(BaseModel):
    title: str
    description: str
    event_date: str
    location: Optional[str] = None

class RSVPUpdate(BaseModel):
    event_id: str
    status: str  # Accepted, Declined, Tentative

# --- HERITAGE SCHEMAS ---
class StoryCreate(BaseModel):
    title: str
    content: str
    historical_date: Optional[str] = None

# --- AI SCHEMAS ---
class AIQuery(BaseModel):
    query: str