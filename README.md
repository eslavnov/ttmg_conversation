# Talk To Me Goose 
![Logo](assets/logo.jpg)

This is a custom integration for Home Assistant to work with [Talk To Me Goose Server](https://github.com/eslavnov/ttmg_server).
Based on [OpenAI Conversation](https://www.home-assistant.io/integrations/openai_conversation/).

**Installation:**
1. HACS install: add this repo as a custom repository in HACS with the type "Integration".
   ![hacs](assets/hacs.png)
   Or simply copy `custom_components/ttgm_conversation` to your custom components folder in Home Assistant.
2. Restart Home Assistant.
3. Go to [integrations](https://my.home-assistant.io/redirect/integrations/) and search for "Talk To Me Goose Conversation". The setup and settings are mostly the same as with the original [OpenAI Conversation](https://www.home-assistant.io/integrations/openai_conversation/) integration. All these settings will be passed to your Talk To Me Goose Server.
