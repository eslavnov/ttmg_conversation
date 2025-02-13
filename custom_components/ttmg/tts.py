"""Support for the TTMG TTS service."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

import requests
from homeassistant.components.tts import (
    CONF_LANG,
    PLATFORM_SCHEMA as TTS_PLATFORM_SCHEMA,
    Provider,
    TextToSpeechEntity,
    TtsAudioType,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.const import CONF_URL

from .const import (
    DEFAULT_LANG,
    SUPPORT_LANGUAGES,
)

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = TTS_PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_LANG, default=DEFAULT_LANG): vol.In(SUPPORT_LANGUAGES),
    }
)


async def async_get_engine(
    hass: HomeAssistant,
    config: ConfigType,
    discovery_info: DiscoveryInfoType | None = None,
) -> TTMGProvider:
    """Set up TTMG TTS component."""
    return TTMGProvider(hass, config[CONF_LANG])

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up TTMG TTS platform via config entry."""
    default_language = "en"
    async_add_entities([TTMGTTSEntity(config_entry, default_language)])

class TTMGTTSEntity(TextToSpeechEntity):
    """The TTMG TTS API entity."""

    def __init__(self, config_entry: ConfigEntry, lang: str) -> None:
        """Init TTMG TTS service."""
        self._attr_name = "TTMG TTS"
        self._attr_unique_id = config_entry.entry_id
        self._lang = lang
        self._url = config_entry.data[CONF_URL]+"/preload-text/ttmg_tts/"

    @property
    def default_language(self) -> str:
        """Return the default language."""
        return self._lang

    @property
    def supported_languages(self) -> list[str]:
        """Return list of supported languages."""
        return SUPPORT_LANGUAGES
      
    def get_tts_audio(
        self, message: str, language: str, options: dict[str, Any] | None = None
    ) -> TtsAudioType:
        """Load TTMG TTS"""
        requests.post("http://192.168.201.10:8888/preload-text/ttmg_tts/", json={"text": message }) 
        return None, None

class TTMGProvider(Provider):
    """The TTMG TTS API provider."""

    def __init__(self, hass: HomeAssistant, lang: str) -> None:
        """Init TTMG TTS service."""
        self.hass = hass
        self._lang = lang
        self.name = "TTMG TTS"

    def get_tts_audio(
        self, message: str, language: str, options: dict[str, Any] | None = None
    ) -> TtsAudioType:
        """Load TTMG TTS"""
        requests.post("http://192.168.201.10:8888/preload-text/ttmg_tts/", json={"text": message }) 
        return None, None
