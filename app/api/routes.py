from fastapi import APIRouter, Depends, FastAPI
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.api.schemas import ItemCreate
from app.db.models import Item
from app.db.database import Base, engine

router = APIRouter()

Base.metadata.create_all(bind=engine)


@router.get("/")
async def get_user() -> dict[str, str]:
    return {"message": "User endpoint is working"}


@router.get("/health")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/items", status_code=201)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)) -> dict[str, object]:
    db_item = Item(name=item.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"id": db_item.id, "name": db_item.name}


@router.get("/items")
async def list_items(db: Session = Depends(get_db)) -> list[dict[str, object]]:
    items = db.query(Item).all()
    return [{"id": item.id, "name": item.name} for item in items]


def include_routes(app: FastAPI) -> None:
    app.include_router(router)
