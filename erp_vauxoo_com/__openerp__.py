# -*- encoding: utf-8 -*-
{
    "name": "Odoo Vauxoo ERP Instance",
    "author": "Vauxoo",
    "summary": "All the necesary modules to auto install our instance.",
    "website": "http://www.vauxoo.com",
    "category": "Vauxoo",
    "version": "2.0",
    "depends": [
        # ERP modules (here nothing with website)
        "project_followers_rule",
        "account_asset",
        "account_budget",
        "account_followup",
        "account_invoice_number",
        "account_reconcile_grouping",
        "account_smart_unreconcile",
        "analytic_contract_hr_expense",
        "hr_contract",
        "hr_expense_replenishment_tax",
        "hr_payslip_paid",
        "hr_recruitment",
        "hr_evaluation",
        "ifrs_report",
        "l10n_mx_cities",
        "l10n_mx_facturae_pac_sf",
        "auth_crypt",
        "project_issue_management",
        "hr_timesheet_reports",
        "vauxoo_sale_reports",
        # Added module of  finkok pac for signed with it invoices and payroll.
        # Task #1886
        "l10n_mx_facturae_pac_finkok",
        # This module install all about  mexican payroll.  Task #1886
        "l10n_mx_payroll_base",
        # This module install a wizard for validate XML signed in SAT  Task
        # #1886
        "l10n_mx_validate_xml_sat",
        "l10n_mx_diot_report",
        "l10n_mx_facturae_report_zebra",
        "account_financial_report",
        "procurement_jit",
        "multi_company",
        "note_pad",
        "expired_task_information",
        "forward_mail",
        "google_drive",
        "google_account",
        "payroll_amount_residual",
        "portal_project_issue",
        "portal_sale",
        "portal_stock",
        "project_conf",
        "project_btree",
        "project_issue_sheet",
        "project_task_domain",
        "purchase_analytic_plans",
        "sync_youtube",
        "warning",
        "sale_order_copy_line",
        # Portal (not website) modules
        "portal_user_story",
        # Technical tools.
        'group_xml_id',
        'hr_payroll_multicompany',
        'send_author_mail',
        'mass_editing',
    ],
    "data": [],
    "demo": [],
    "test": [
    ],
    "auto_install": False,
    "application": True,
    "installable": True,
}
