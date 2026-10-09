# Hospitality Workforce OS

Hospitality Workforce OS is the reusable people-operations layer for restaurants, hotels, cafés, beach clubs, caterers, and tourist-experience operators.

BOSSA Asado i Mar is the first pilot organization. The architecture is multi-tenant from day one.

## Domain Map

```text
Organizations
├── Locations
├── Employees
├── Roles
├── Shift Scheduling
├── Attendance
├── Leave
├── Training
├── Payroll Inputs
├── Payroll Runs
├── Compliance
├── Approvals
└── Audit Logs
```

## Operating Flow

```text
Organization + Location setup
        ↓
Employee + Role assignment
        ↓
Shift planning
        ↓
Attendance and exception capture
        ↓
Leave, overtime, bonus, deduction inputs
        ↓
AI payroll validation
        ↓
Manager → Accountant → Owner approval
        ↓
External payroll software and bank processing
        ↓
Government payment confirmation
        ↓
Append-only audit close
```

## Source-of-Truth Boundaries

- **Notion:** operational workflow, approvals, readiness, training, and management views.
- **Supabase:** future production database, authentication, tenant isolation, row-level security, and API layer.
- **Approved payroll software:** official payroll calculations, payslips, declarations, and payment files.
- **Restricted document storage:** contracts, identity files, bank details, medical evidence, and official payroll documents.
- **GitHub:** schemas, prompts, skills, application code, tests, and documentation only.

## Safety Rules

1. Never commit employee names, bank details, tax numbers, identity documents, medical records, salaries, or payroll exports to a public repository.
2. AI may validate, flag, summarize, and route payroll work, but it may not release salary or government payments.
3. Payroll completion requires accountant/controller and owner authorization.
4. Payment status requires external evidence.
5. Audit logs are append-only and must not contain secrets or full sensitive payloads.

## MVP Phases

### Phase 1 — Notion foundation
Create the 13 domain databases and privacy-safe operating fields.

### Phase 2 — Relations and dashboards
Replace temporary text keys with relations, rollups, filtered views, and BOSSA dashboards.

### Phase 3 — BOSSA pilot
Load roles, locations, masked employee IDs, schedules, training modules, and one test payroll cycle.

### Phase 4 — Supabase product layer
Implement normalized tables, RLS, role-based access, APIs, audit triggers, and integration adapters.

### Phase 5 — Multi-tenant product
Add onboarding, organization configuration, location templates, payroll-provider adapters, and Hospitality OS licensing.
