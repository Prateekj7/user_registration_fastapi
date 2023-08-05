from fastapi import FastAPI, HTTPException
from database.postgres import create_postgres_engine, create_postgres_session
from database.mongodb import insert_profile_picture, get_profile_picture
from database.models import User, UserRegistration

app = FastAPI()
postgres_engine = create_postgres_engine()
postgres_session = create_postgres_session(postgres_engine)


@app.post("/register/", response_model=UserRegistration)
async def register_user(user: UserRegistration):
    # Check if the email already exists in PostgreSQL
    query = postgres_session.query(User).filter(User.email == user.email)
    existing_user = query.first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    # Insert user details into PostgreSQL
    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password=user.password,
        phone=user.phone,
    )
    postgres_session.add(new_user)
    postgres_session.commit()

    # Insert profile picture URL into MongoDB
    profile_data = {
        "user_id": new_user.id,
        "profile_picture": user.profile_picture,
    }
    insert_profile_picture(profile_data)

    return user


@app.get("/user/{user_id}/", response_model=UserRegistration)
async def get_user(user_id: int):
    # Fetch user details from PostgreSQL
    query = postgres_session.query(User).filter(User.id == user_id)
    user = query.first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Fetch profile picture URL from MongoDB
    profile_data = get_profile_picture(user_id)
    if profile_data is None:
        raise HTTPException(status_code=404, detail="Profile picture not found")

    return UserRegistration(
        full_name=user.full_name,
        email=user.email,
        password=user.password,
        phone=user.phone,
        profile_picture=profile_data["profile_picture"],
    )
