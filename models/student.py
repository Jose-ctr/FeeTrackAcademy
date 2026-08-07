from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Optional, Dict, Any


_DECIMAL_QUANT = Decimal("0.01")


@dataclass
class Student:
    student_id: str
    name: str
    class_name: Optional[str] = None
    admission_no: Optional[str] = None
    parent_phone: Optional[str] = None
    total_fee: Decimal = field(default_factory=lambda: Decimal("0.00"))
    paid: Decimal = field(default_factory=lambda: Decimal("0.00"))
    admission_date: Optional[date] = None

    def __post_init__(self) -> None:
        # normalize numeric inputs to Decimal
        try:
            self.total_fee = Decimal(self.total_fee)
        except (InvalidOperation, TypeError):
            raise ValueError("total_fee must be numeric or Decimal-like")
        try:
            self.paid = Decimal(self.paid)
        except (InvalidOperation, TypeError):
            raise ValueError("paid must be numeric or Decimal-like")

        if self.total_fee < 0 or self.paid < 0:
            raise ValueError("total_fee and paid must be non-negative")

        # keep two-decimal precision
        self.total_fee = self.total_fee.quantize(_DECIMAL_QUANT, rounding=ROUND_HALF_UP)
        self.paid = self.paid.quantize(_DECIMAL_QUANT, rounding=ROUND_HALF_UP)

    @property
    def balance(self) -> Decimal:
        return (self.total_fee - self.paid).quantize(_DECIMAL_QUANT, rounding=ROUND_HALF_UP)

    # compatibility alias if other code expects `.id`
    @property
    def id(self) -> str:
        return self.student_id

    def to_dict(self) -> Dict[str, Any]:
        return {
            "student_id": self.student_id,
            "id": self.student_id,  # keep both for compatibility
            "name": self.name,
            "class_name": self.class_name,
            "admission_no": self.admission_no,
            "parent_phone": self.parent_phone,
            "total_fee": str(self.total_fee),
            "paid": str(self.paid),
            "balance": str(self.balance),
            "admission_date": self.admission_date.isoformat() if self.admission_date else None,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Student":
        adm = data.get("admission_date")
        if adm and not isinstance(adm, date):
            try:
                adm = datetime.fromisoformat(adm).date()
            except Exception:
                adm = None
        return cls(
            student_id=data.get("student_id") or data.get("id"),
            name=data["name"],
            class_name=data.get("class_name"),
            admission_no=data.get("admission_no"),
            parent_phone=data.get("parent_phone"),
            total_fee=Decimal(data.get("total_fee", "0.00")),
            paid=Decimal(data.get("paid", "0.00")),
            admission_date=adm,
        )

    def __repr__(self) -> str:
        return f"<Student {self.student_id} {self.name} balance={self.balance}>"
        
