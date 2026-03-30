from __future__ import annotations
from dataclasses import dataclass, field
from typing import Final

# Konstanta
RATE_PER_KM: Final[int] = 5_000
HANDLING_FEE: Final[int] = 20_000
PRIORITY_FEE: Final[int] = 50_000
INSURANCE_RATE: Final[float] = 0.10

# Kelas Dasar
@dataclass
class Shipment:
    distance_km: int

    def __post_init__(self) -> None:
        if self.distance_km <= 0:
            raise ValueError(f"distance_km harus > 0, diterima: {self.distance_km}")

    def calculateBaseCost(self) -> int:
        return self.distance_km * RATE_PER_KM

# Pengiriman Standar
@dataclass
class StandardShipment(Shipment):
    handling_fee: int = field(default=HANDLING_FEE, init=False)

    def calculateTotalCost(self) -> int:
        return self.calculateBaseCost() + self.handling_fee



# Pengiriman Barang Fragil
@dataclass
class FragileGoodsShipment(StandardShipment):

    def calculateTotalCost(self) -> int:
        base_total = super().calculateTotalCost()
        insurance = round(base_total * INSURANCE_RATE)
        return base_total + insurance

# Pengiriman Prioritas
@dataclass
class PriorityShipment(StandardShipment):

    def calculateTotalCost(self) -> int:
        return super().calculateTotalCost() + PRIORITY_FEE

# Helper — format Rupiah
def format_rupiah(amount: int) -> str:
    return f"Rp {amount:,.0f}".replace(",", ".")

# Helper — cetak rincian per kiriman
def print_detail(index: int, shipment: StandardShipment) -> None:
    nama_kelas  = shipment.__class__.__name__
    base        = shipment.calculateBaseCost()
    handling    = shipment.handling_fee
    separator   = "  " + "─" * 35

    print(f"\n  Kiriman #{index}  ({nama_kelas}, {shipment.distance_km} km)")
    print(f"    Biaya dasar       : {format_rupiah(base)}")
    print(f"    + Handling fee    : {format_rupiah(handling)}")

    if isinstance(shipment, FragileGoodsShipment):
        standard_total = base + handling
        insurance      = round(standard_total * INSURANCE_RATE)
        print(f"    + Asuransi 10%    : {format_rupiah(insurance)}")

    elif isinstance(shipment, PriorityShipment):
        print(f"    + Biaya prioritas : {format_rupiah(PRIORITY_FEE)}")

    print(separator)
    print(f"    Total              : {format_rupiah(shipment.calculateTotalCost())}")

# Eksekusi Utama
#  Buat instance
fragile  = FragileGoodsShipment(distance_km=100)
priority = PriorityShipment(distance_km=50)

# Simpan dalam array
shipments = [fragile, priority]

#  Loop, cetak rincian, akumulasi grand total
grand_total_cost = 0
for i, shipment in enumerate(shipments, start=1):
    print_detail(i, shipment)
    grand_total_cost += shipment.calculateTotalCost()

#  Tampilkan grand total
garis = "─" * 55
print(f"\n{garis}")
print(f"  GRAND TOTAL : {format_rupiah(grand_total_cost)}")
print(garis)
