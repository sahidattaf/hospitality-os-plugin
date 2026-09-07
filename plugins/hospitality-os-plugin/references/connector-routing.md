# Connector Routing

Use only connectors actually available in the current session.

| Need | Preferred connector | Boundary |
|---|---|---|
| Operating records | Notion | Read before write; exact-record owner gate for changes |
| Recipient identity | Google Contacts | Never guess among ambiguous people |
| Email | Gmail | Draft by default; send requires owner gate |
| Scheduling | Google Calendar | Verify timezone and conflicts; write requires owner gate |
| Documents | Google Drive | Preserve file identity and permissions |
| Code | GitHub | Branch, commit, push, PR, and merge are separately gated |
| Hosting | Vercel | Preview, deploy, and production promotion are separately gated |

No verified WhatsApp, POS, reservation, purchasing, or inventory connector is bundled. For those systems, prepare drafts or analyze owner-supplied exports. Do not claim execution.
