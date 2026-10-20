"""The plugin's settings, edited in its Settings tab in dashAI."""

from DashAI.back.core.schema_fields import int_field, schema_field
from DashAI.back.core.utils import MultilingualString
from DashAI.back.plugins.settings import BasePluginSettings


class Settings(BasePluginSettings):
    decimals: schema_field(
        int_field(ge=0, le=6),
        4,  # the default value
        MultilingualString(
            en="Decimals the error rate is rounded to.",
            es="Decimales a los que se redondea la tasa de error.",
        ),
        alias=MultilingualString(en="Decimals", es="Decimales"),
    )  # type: ignore
