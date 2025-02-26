# [Create a Slack bot](https://cloud.google.com/dialogflow/cx/docs/concept/integration/slack#create_a_slack_bot)

```yaml
display_information:
  name: Conversational Agents (Dialogflow CX)
  description: Conversational Agents (Dialogflow CX) integration
  background_color: "#1148b8"
features:
  app_home:
    home_tab_enabled: false
    messages_tab_enabled: true
    messages_tab_read_only_enabled: false
  bot_user:
    display_name: CX
    always_online: true
oauth_config:
  scopes:
    bot:
      - app_mentions:read
      - chat:write
      - im:history
      - im:read
      - im:write
      - incoming-webhook
settings:
  event_subscriptions:
    request_url: https://dialogflow-slack-4vnhuutqka-uc.a.run.app
    bot_events:
      - app_mention
      - message.im
  org_deploy_enabled: false
  socket_mode_enabled: false
  token_rotation_enabled: false
```