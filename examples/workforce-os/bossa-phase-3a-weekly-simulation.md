# BOSSA Phase 3A — Full Masked Weekly Simulation

## Scope

This simulation validates one complete operating week for BOSSA Asado i Mar using masked records only. It does not contain real employee, identity, banking, tax, medical, or salary data.

- Organization: `ORG-001` — BOSSA Asado i Mar
- Location: `LOC-001` — BOSSA Pietermaai
- Simulation week: 2026-07-13 through 2026-07-19
- Payroll month: `2026-07`

## Masked team

| Employee key | Role | Department |
| --- | --- | --- |
| TEST-EMP-001 | General Manager | Management |
| TEST-EMP-002 | Kitchen Lead | Kitchen |
| TEST-EMP-003 | Fire Grill Cook | Fire Station |
| TEST-EMP-004 | Server | Service |
| TEST-EMP-005 | Host & Reservations | Reservations |
| TEST-EMP-006 | Cleaner | Cleaning |

## Scenario matrix

| Day | Scenario | Expected control result |
| --- | --- | --- |
| Monday | Normal service | Healthy operations |
| Tuesday | Fire cook 18 minutes late | Attendance exception |
| Tuesday | Server missing clock-out | Manager review required |
| Wednesday | Host requests Friday leave | Leave approval and coverage action |
| Thursday | Kitchen lead works 4 overtime hours | Manager approved, accountant review required |
| Friday | Weekend Fire rush and extra Fire Station hours | Labor and payroll exception review |
| Saturday | Cleaner reports sick | Absence, sick leave and replacement action |
| Sunday | Weekly close | Workforce report and payroll readiness check |

## Validation rules

1. Every shift must link to an organization, location, role and employee.
2. Every attendance record must link to an employee and organization.
3. Late arrivals and missing clocks must remain visible until reviewed.
4. Overtime cannot reach payroll approval without manager and accountant review.
5. Employees with incomplete payroll profiles block payroll readiness.
6. Expired or refresh-due training creates a warning.
7. Leave and absence records must show payroll impact.
8. Payroll cannot be marked paid without owner approval and evidence.
9. Government payment cannot be marked complete without evidence.
10. Material actions must be represented in the audit log.

## Expected final result

```yaml
simulation_status: passed_with_expected_exceptions
payroll_status: NOT_READY_FOR_PAYMENT
expected_blockers:
  - TEST-EMP-005 payroll profile incomplete
  - TEST-EMP-003 training refresh due
  - TEST-EMP-003 overtime awaiting accountant review
  - TEST-EMP-004 missing clock-out awaiting manager review
```

## Exit criteria

Phase 3A is complete when the Notion pilot can answer:

- Who is scheduled today?
- Who is late or absent?
- Which clock records are incomplete?
- Which leave requests are pending or approved?
- Which overtime inputs need approval?
- Which training or compliance records are expiring?
- Is the payroll run ready for accountant or owner approval?
- What actions occurred and who approved them?
