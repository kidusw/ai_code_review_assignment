from typing import List, Dict, Any

def calculate_average_order_value(orders:List[Dict[str,Any]])->Dict[str,Any]:

    valid_orders = [
        order for order in orders
        if order.get("status") != "cancelled"
        and isinstance(order.get("amount"), (int, float))
        and order.get("amount", 0) >= 0
    ]
    
    if not valid_orders:
        return 0.0

    total = sum(order["amount"] for order in valid_orders)
    return total / len(valid_orders)

items = [
    {"id": 1, "status": "cancelled", "amount": 2},
    {"id": 2, "status": "cancelled", "amount": 2},
    {"id": 3, "status": "approved", "amount": "hk"},
    {"id": 4, "status": "approved", "amount": 2},
    {"id": 5, "status": "approved", "amount": 2},
    {"id": 6, "status": "approved", "amount": 2},
    {"id": 7, "status": "cancelled", "amount": 2},
]

result = calculate_average_order_value(items)

print("result:", result)
