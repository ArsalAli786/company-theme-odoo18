{
    "name": "Company Theme for Odoo 18",
    "version": "18.0.1.0.0",
    "summary": "Company-specific backend accent color, with an Enterprise Apps background.",
    "description": "Configure the Odoo backend primary accent color separately for each company. The included Enterprise companion addon also provides an optional company-specific Apps/Home background image.",
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
