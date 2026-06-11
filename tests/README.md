# Tests

Primary validation uses the plugin-creator validator:

```powershell
C:\Users\sahid\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe C:\Users\sahid\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\sahid\OneDrive\Documents\hospitality-os-plugin
```

Expected result:

```text
Plugin validation passed
```

Manual smoke tests:

- Ask each skill's test prompt, including the v0.2 agents (Restaurant Outreach, Hotel Outreach, Catering Sales, Event Booking, Investor Deck, Social Media, Menu Costing, Inventory, Staff Training, Customer Recovery).
- Confirm the response follows that skill's output format.
- Confirm BOSSA-specific examples stay grounded in the provided facts.
