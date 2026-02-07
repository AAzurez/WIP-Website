from fastapi import APIRouter, HTTPException
from backend.app.data.cards import FAKE_CARDS

router = APIRouter(
    prefix="/cards",
    tags=["cards"],
)

@router.get("/")
def list_cards():
    return FAKE_CARDS

@router.get("/{card_id}")
def get_card(card_id: str):
    for card in FAKE_CARDS:
        if card["id"] == card_id:
            return card
    raise HTTPException(status_code=404, detail="Card not found")