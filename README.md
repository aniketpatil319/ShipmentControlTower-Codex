# Shipment Control Tower

This project is a minimal multi-tenant Django web application for managing inbound and outbound shipments. It is intended as a starting point for a SaaS platform for logistics teams working with D2C companies.

## Features

- Multi-tenancy via `Company` and custom `User` model.
- Admin-managed users (no self sign‑up).
- Dashboard showing inbound and outbound shipments filtered by the user's company.
- Basic Bulma-based UI.

## Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Apply migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
3. Run the development server:
   ```bash
   python manage.py runserver
   ```
4. Run tests:
   ```bash
   python manage.py test
   ```

Access the admin at `http://localhost:8000/admin/` to create companies, users, and shipments.
