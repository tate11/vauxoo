# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    OVL : Openerp Venezuelan Localization
#    Copyleft (Cl) 2008-2021 Vauxoo, C.A. (<http://vauxoo.com>)
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{   "name" : "OpenERP Vauxoo COM",
    "version" : "1.0",
    "depends" : [
        #TODO: Clean modules list. This version 1 is copy& paste from installed modules
        #TODO: Add icon
        "crm",
        "mail",
        "account_voucher",
        "project",
        "note",
        "project_issue",
        "account_accountant",
        "sale",
        "stock",
        "purchase",
        "hr",
        "hr_timesheet",
        "hr_timesheet_sheet",
        "hr_recruitment",
        "hr_expense",
        "hr_evaluation",
        "account_asset",
        "account",
        "account_analytic_analysis",
        "account_analytic_default",
        "account_analytic_plans",
        "account_budget",
        "account_cancel",
        "account_chart",
        "account_followup",
        "account_invoice_line_currency",
        "account_invoice_number",
        "account_invoice_tax",
        "account_move_line_base_tax",
        "account_move_report",
        "account_voucher_tax",
        "admin_message",
        "analytic",
        "analytic_contract_hr_expense",
        "audittrail",
        "auth_oauth",
        "auth_oauth_signup",
        "auth_signup",
        "base",
        "base_action_rule",
        "base_calendar",
        "base_import",
        "base_setup",
        "base_status",
        "base_vat",
        "board",
        "branch_info",
        "bzr_to_task",
        "city",
        "contacts",
        "contpaq_openerp_vauxoo",
        "contract_enterprise_openerp",
        #"create_openerp_instance",#Installed by error
        "decimal_precision",
        "document",
        #"document_ftp",#No enable for testing
        "document_page",
        "document_webdav",
        "edi",
        "email_template",
        "email_template_multicompany",
        "event",
        "event_sale",
        "expired_task_information",
        "fetchmail",
        "google_base_account",
        "google_docs",
        "hr_attendance",
        "hr_contract",
        "hr_expense_analytic",
        "hr_expense_replenishment",
        "hr_expense_replenishment_tax",
        "hr_timesheet_invoice",
        "incoterm_ext",
        "knowledge",
        "l10n_mx",
        "l10n_mx_account_tax_category",
        "l10n_mx_base_vat_split",
        "l10n_mx_cities",
        "l10n_mx_company_cif",
        "l10n_mx_company_multi_address",
        "l10n_mx_facturae_pac_sf",
        "l10n_mx_facturae_vauxoo_report",
        "l10n_mx_invoice_currency_chgdft",
        "l10n_mx_notes_invoice",
        "l10n_mx_partner_address",
        "l10n_mx_res_partner_bank",
        "l10n_mx_settings_facturae",
        "l10n_mx_states",
        "lunch",
        "mass_editing",
        "mrp_jit",
        "multi_company",
        "multireport_base",
        "network",
        "note_pad",
        "pad",
        "portal",
        "portal_anonymous",
        "portal_crm",
        "portal_crm_vauxoo",
        "portal_event",
        "portal_events",
        "portal_home",
        "portal_hr_employees",
        "portal_hr_imp",
        "portal_news",
        "portal_products",
        "portal_project",
        "portal_project_imp",
        "portal_project_issue",
        "portal_public_documents",
        "portal_runbot",
        "portal_sale",
        "portal_stock",
        "process",
        "procurement",
        "product",
        "project_conf",
        "project_gtd",
        "project_issue_sheet",
        "project_long_term",
        "project_timesheet",
        "purchase_analytic_plans",
        "report_multicompany",
        "report_webkit",
        "resource",
        "risk_management",
        "sale_crm",
        "sale_multicompany_report",
        #"sale_order_report",#Temp delete because directory structure not standard. TODO: Fix directory structure.
        "sale_stock",
        "share",
        "sprint_kanban",
        "survey",
        "sync_youtube",
        "user_story",
        "vauxoo_cms",
        "vauxoo_doc",
        "warning",
        "web",
        "web_allow_custom_root",
        "web_analytics",
        "web_bootstrap3",
        "web_calendar",
        "web_captcha",
        "web_diagram",
        "web_doc",
        "web_export_view",
        "web_fancybox",
        "web_flagicons",
        "web_fontawesome",
        "web_gantt",
        "web_graph",
        "web_kanban",
        "web_many2many_attachments",
        "web_nocreatedb",
        "web_tests",
        "web_vauxoo_cust",
        "web_view_editor",
        "www_vauxoo_com"
            ],
    "author" : "Vauxoo",
    "description" : """
Install all apps needed to comply with Vauxoo instance
======================================================

This module will install for you:
  ...TODO
                    """,
    "website" : "http://www.vauxoo.com",
    "category" : "Localization/Application",
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [],
    "test" : [],
    "images" : [],
    "auto_install": False,
    "application": True,
    "installable": True,
}