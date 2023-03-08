import voluptuous as vol
from homeassistant import config_entries

from .const import DOMAIN

# Validate user input
CONFIG_SCHEMA = vol.Schema({DOMAIN: vol.Schema({})}, extra=vol.ALLOW_EXTRA)


class ExampleConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""

    async def async_step_user(self, user_input=None):
        """Step when user initializes a integration."""
        return self.async_show_form(step_id="user")


    async def async_step_import(self, user_input=None):
        """Step when importing a configuration flow from config.yaml."""
        return self.async_show_form(step_id="import")


    async def async_step_zeroconf(self, discovery_info=None):
        """Step when discovered by zeroconf."""
        return self.async_show_form(step_id="zeroconf")


    async def async_step_homekit(self, discovery_info=None):
        """Step when discovered by HomeKit."""
        return self.async_show_form(step_id="homekit")
