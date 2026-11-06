"""Shipping rate calculations."""

_EXPRESS_SURCHARGE = 7.0
_VALID_SERVICES = {"standard", "express"}


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping in dollars.

    Args:
        weight_kg: Parcel weight; must be positive.
        zone: Delivery zone — ``"local"`` or ``"regional"``.
        service: ``"standard"`` (default) or ``"express"``.
            Express adds $7.00 to the standard rate.

    Returns:
        Total shipping cost rounded to two decimal places.

    Raises:
        ValueError: If *weight_kg* is not positive, *zone* is unknown,
            or *service* is not recognised.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in {"local", "regional"}:
        raise ValueError("unknown zone")
    if service not in _VALID_SERVICES:
        raise ValueError(f"unknown service: {service!r}")
    base = 5.0 if zone == "local" else 8.0
    total = base + 1.5 * weight_kg
    if service == "express":
        total += _EXPRESS_SURCHARGE
    return round(total, 2)
