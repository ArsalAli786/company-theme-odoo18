{
    "name": "Company Backend Theme Color",
    "version": "18.0.1.0.0",
    "summary": "Set a company-specific primary accent color for the Odoo backend.",
    "description": "Configure a primary backend accent color separately for each company.",
    "category": "Customizations",
    "author": "Arsal Ali",
    "depends": [
        "base",
        "web",
    ],
    "data": [
        "views/company_theme.xml",
        "views/res_company_views.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
