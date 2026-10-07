# main.py
# Author: Darian Peters
from business_rules import (
    apply_discount,
    calculate_total,
    get_approval_tier,
    requires_review,
)

price, qty = 450.00, 3
total = calculate_total(price, qty)

print()
print("===== Order Summary =====")
print("--------------------------")
print(f"Subtotal:        ${price * qty:,.2f}")
print(f"Tax:             ${price * qty * 0.07:,.2f}")
print(f"Total:           ${total:,.2f}")
print("--------------------------")
print(f"Requires review: {requires_review(total)}")
print(f"Approval tier:   {get_approval_tier(total)}")
print(f"10% discount:    ${apply_discount(price, 10):,.2f}")
print()
