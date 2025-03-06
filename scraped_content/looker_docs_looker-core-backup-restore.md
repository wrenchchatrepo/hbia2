# https://cloud.google.com/looker/docs/looker-core-backup-restore

Depth: 3

Looker (Google Cloud core) instances are backed up once automatically every 24 hours. Each backup contains a record of all the data in the instance's internal database and in the instance's file server, which is most of the operational data for the Looker (Google Cloud core) instance. However, the data for [Elite System Activity](/looker/docs/elite-system-activity) is not backed up.

Backups are retained for 30 days. To access and restore a backup, [contact technical support](/looker/docs/looker-core-support).

**Caution:** Disabling the Looker API disables the ability to create instance backups.

## What's next

  * [Delete and restart a Looker (Google Cloud core) instance](/looker/docs/looker-core-delete-restart)