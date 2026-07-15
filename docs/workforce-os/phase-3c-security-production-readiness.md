# Phase 3C — Security & Production Readiness

## Status

Conditionally ready for staging. Not ready for real payroll until manual workspace permissions, secure storage, and production controls are completed.

## Access model

| Role | Allowed | Prohibited |
|---|---|---|
| Owner | Full payroll, approvals, compliance, audit, configuration | Public sharing of restricted data |
| Accountant | Payroll inputs, payroll runs, evidence and finance approvals | Operational edits outside payroll workflow |
| General Manager | Employees, shifts, attendance, leave, training, operational approvals | Salary totals, bank details, identity and tax records |
| Department Lead | Assigned team scheduling, attendance exceptions and training | Payroll and cross-department records |
| Employee | Personal schedule, leave requests and training | Other employee records |
| AI Operator | Validation, exception detection and reporting | Approval, submission or payment release |

A filtered Notion view is not a security boundary. Production enforcement requires database/page permissions and later Supabase RLS.

## Environment separation

- `TEST`: masked and fictitious records only.
- `STAGING`: privacy-safe import validation; no bank, identity, tax or medical data.
- `PRODUCTION`: owner-approved records with least-privilege access.

Records must not move from staging to production unless validation passes, the secure record reference exists, and the owner approves the migration.

## Evidence gates

Evidence is mandatory for signed contracts, completed payroll profiles, overtime, bonuses, deductions, advances, reimbursements, payroll approvals, salary payments, government payments, compliance status and certification-based training.

A record cannot be considered complete when evidence is required and either the evidence reference is empty or `evidence_validated` is false.

## Secure HR vault

```text
Secure HR Vault/
└── ORG-001-BOSSA/
    ├── Employees/
    │   └── EMP-XXX/
    │       ├── Contract/
    │       ├── Identity/
    │       ├── Payroll-Profile/
    │       └── Compliance/
    ├── Payroll/
    │   └── YYYY-MM/
    │       ├── Payroll-Export/
    │       ├── Approval-Evidence/
    │       ├── Salary-Payment/
    │       └── Government-Payment/
    └── Audit-Exports/
```

Notion stores only a reference. Never commit personal, banking, tax, medical or salary documents to GitHub.

## Employee import template

Required privacy-safe fields:

```csv
external_key,masked_name,organization_key,location_key,department,role_key,employment_type,start_date,standard_weekly_hours,contract_status,payroll_profile_status,training_status,secure_record_ref
```

Forbidden import fields:

- bank account
- identity or passport number
- tax number
- medical details
- full salary documents
- passwords or credentials

## Go-live checklist

- [ ] Workspace owner identified
- [ ] Owner and accountant assigned
- [ ] Manager access tested
- [ ] Department-lead access tested
- [ ] Shared links disabled
- [ ] Secure HR vault created
- [ ] Retention/deletion policy approved
- [ ] Import validated in staging
- [ ] Evidence references tested
- [ ] Dual approval tested
- [ ] Audit export tested
- [ ] Backup procedure tested
- [ ] Incident owner assigned
- [ ] Official payroll software confirmed as source of truth
- [ ] Owner and accountant approve production go-live

## Production gate

```yaml
production_ready: false
staging_ready: true
manual_permissions_required: true
secure_vault_required: true
real_payroll_allowed: false
```
