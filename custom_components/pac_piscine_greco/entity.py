from .const import DOMAIN
from .models import DEVICE_NAME, MANUFACTURER, MODEL


class PacDeviceMixin:
    """device_info commun à toutes les entités de la PAC (un seul appareil)."""

    _entry_id: str

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._entry_id)},
            "name": DEVICE_NAME,
            "manufacturer": MANUFACTURER,
            "model": MODEL,
        }
