# Company Theme for Odoo 18

Set a company-specific primary accent color for the Odoo backend. Standard Odoo and Bootstrap primary UI follows the selected color while semantic status colors remain distinct.

## Editions

- **Community:** company-specific backend primary color.
- **Enterprise:** the same color feature, plus an optional company-specific Apps/Home background image.

The Enterprise feature is provided by the technical `company_theme_enterprise` companion addon. Keep both addon directories in the addons path. Install `company_theme`; when `web_enterprise` is available, Odoo can auto-install the companion through its declared dependencies.

Compatible with Odoo 18. The main addon license is LGPL-3; see [`company_theme/LICENSE`](company_theme/LICENSE).
