-- Hospitality Workforce OS — production schema blueprint
-- Target: PostgreSQL / Supabase
-- Store sensitive identity, bank, medical, and payroll-document data in restricted systems.

create extension if not exists pgcrypto;

create table organizations (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  legal_name text,
  type text not null,
  country_code text,
  timezone text not null default 'America/Curacao',
  payroll_provider text,
  status text not null default 'setup',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table locations (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id) on delete cascade,
  name text not null,
  type text not null,
  address_text text,
  timezone text,
  status text not null default 'active',
  created_at timestamptz not null default now()
);

create table roles (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id) on delete cascade,
  name text not null,
  department text not null,
  level text not null,
  default_weekly_hours numeric(6,2),
  can_approve_overtime boolean not null default false,
  can_approve_leave boolean not null default false,
  training_requirements jsonb not null default '[]'::jsonb,
  status text not null default 'active'
);

create table employees (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id) on delete cascade,
  home_location_id uuid references locations(id),
  role_id uuid references roles(id),
  employee_code text not null,
  display_name text,
  department text,
  employment_type text not null,
  start_date date,
  end_date date,
  standard_weekly_hours numeric(6,2),
  status text not null default 'onboarding',
  payroll_profile_complete boolean not null default false,
  contract_status text not null default 'missing',
  secure_record_ref text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (organization_id, employee_code)
);

create table shifts (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id) on delete cascade,
  location_id uuid not null references locations(id),
  employee_id uuid references employees(id),
  role_id uuid references roles(id),
  starts_at timestamptz not null,
  ends_at timestamptz not null,
  shift_type text,
  status text not null default 'draft',
  manager_approved boolean not null default false,
  notes text,
  created_at timestamptz not null default now(),
  check (ends_at > starts_at)
);

create table attendance (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id) on delete cascade,
  location_id uuid not null references locations(id),
  employee_id uuid not null references employees(id),
  shift_id uuid references shifts(id),
  work_date date not null,
  clock_in timestamptz,
  clock_out timestamptz,
  regular_hours numeric(6,2) not null default 0,
  overtime_hours numeric(6,2) not null default 0,
  break_minutes integer not null default 0,
  late_minutes integer not null default 0,
  exception_type text,
  manager_approved boolean not null default false,
  payroll_month date,
  created_at timestamptz not null default now()
);

create table leave_requests (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id) on delete cascade,
  employee_id uuid not null references employees(id),
  leave_type text not null,
  starts_on date not null,
  ends_on date not null,
  units numeric(8,2),
  payroll_impact text,
  status text not null default 'draft',
  evidence_ref text,
  created_at timestamptz not null default now(),
  check (ends_on >= starts_on)
);

create table training_assignments (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id) on delete cascade,
  employee_id uuid not null references employees(id),
  role_id uuid references roles(id),
  module_name text not null,
  category text,
  assigned_on date,
  due_on date,
  completed_on date,
  expires_on date,
  score numeric(6,2),
  status text not null default 'not_started',
  evidence_ref text
);

create table payroll_inputs (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id) on delete cascade,
  employee_id uuid not null references employees(id),
  payroll_month date not null,
  input_type text not null,
  hours numeric(8,2),
  amount numeric(14,2),
  reason text,
  manager_approved boolean not null default false,
  accountant_reviewed boolean not null default false,
  evidence_ref text,
  status text not null default 'draft',
  created_at timestamptz not null default now()
);

create table payroll_runs (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id) on delete cascade,
  payroll_month date not null,
  employee_count integer not null default 0,
  gross_payroll numeric(14,2),
  net_payroll numeric(14,2),
  government_obligations numeric(14,2),
  total_funding_required numeric(14,2),
  exception_count integer not null default 0,
  ai_validation text not null default 'not_run',
  payroll_software_status text not null default 'not_started',
  accountant_approved boolean not null default false,
  owner_approved boolean not null default false,
  salary_payment_status text not null default 'not_ready',
  government_payment_status text not null default 'not_ready',
  evidence_ref text,
  status text not null default 'collecting_inputs',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (organization_id, payroll_month)
);

create table compliance_items (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id) on delete cascade,
  location_id uuid references locations(id),
  employee_id uuid references employees(id),
  category text not null,
  authority text,
  issue_date date,
  expiry_date date,
  review_date date,
  evidence_ref text,
  risk text not null default 'low',
  status text not null default 'pending',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table approvals (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id) on delete cascade,
  request_type text not null,
  record_type text not null,
  record_id uuid not null,
  requested_by uuid,
  approver_role text not null,
  approver_id uuid,
  requested_at timestamptz not null default now(),
  decided_at timestamptz,
  decision text not null default 'pending',
  decision_notes text,
  evidence_ref text
);

create table audit_logs (
  id uuid primary key default gen_random_uuid(),
  organization_id uuid not null references organizations(id) on delete cascade,
  location_id uuid references locations(id),
  actor_ref text,
  actor_role text,
  action text not null,
  entity_type text not null,
  entity_id uuid,
  before_summary jsonb,
  after_summary jsonb,
  reason text,
  evidence_ref text,
  severity text not null default 'info',
  created_at timestamptz not null default now()
);

create index idx_locations_org on locations(organization_id);
create index idx_employees_org_status on employees(organization_id, status);
create index idx_shifts_location_start on shifts(location_id, starts_at);
create index idx_attendance_employee_date on attendance(employee_id, work_date);
create index idx_payroll_inputs_org_month on payroll_inputs(organization_id, payroll_month);
create index idx_payroll_runs_org_month on payroll_runs(organization_id, payroll_month);
create index idx_compliance_expiry on compliance_items(organization_id, expiry_date);
create index idx_approvals_pending on approvals(organization_id, decision, requested_at);
create index idx_audit_org_created on audit_logs(organization_id, created_at desc);

-- Enable RLS before production and scope every table through organization membership.
