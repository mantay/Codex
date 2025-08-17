import os
from typing import List, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YANDEX_MARKET_TOKEN")
CAMPAIGN_ID = os.getenv("CAMPAIGN_ID")
BASE_URL = "https://api.partner.market.yandex.ru"


def _headers() -> Dict[str, str]:
    if not API_KEY:
        raise RuntimeError("YANDEX_MARKET_TOKEN is not set")
    return {"Api-Key": API_KEY}


def list_orders() -> Dict:
    """Fetch orders for the configured campaign."""
    if not CAMPAIGN_ID:
        raise RuntimeError("CAMPAIGN_ID is not set")
    url = f"{BASE_URL}/campaigns/{CAMPAIGN_ID}/orders"
    response = requests.get(url, headers=_headers())
    response.raise_for_status()
    return response.json()


def deliver_digital_goods(order_id: int, items: List[Dict]) -> None:
    """Send digital goods codes to customer."""
    if not CAMPAIGN_ID:
        raise RuntimeError("CAMPAIGN_ID is not set")
    url = f"{BASE_URL}/campaigns/{CAMPAIGN_ID}/orders/{order_id}/deliverDigitalGoods"
    payload = {"items": items}
    response = requests.post(url, headers=_headers(), json=payload)
    response.raise_for_status()
