# Restaurant Ordering App Backend

This is the backend API for the Restaurant Ordering App, built with Python and FastAPI. It provides endpoints for menu management, order processing, and supports integration with the mobile frontend.

---

## Features

- RESTful API for menu items, categories, and orders
- Fast, modern codebase using FastAPI
- Cross-origin support for mobile app integration
- Simple to set up and extend

---

## Tech Stack

- **Framework:** FastAPI
- **Language:** Python 3.8+
- **Database:** PostgreSQL
- **Server:** Uvicorn

---

## API Endpoints

| Method | Endpoint              | Description                    |
|--------|-----------------------|--------------------------------|
| GET    | /menu-items           | List all menu items            |
| GET    | /menu-items/{id}      | Get a specific menu item       |
| GET    | /categories           | List all categories            |
| POST   | /orders               | Place a new order              |
| GET    | /orders/{id}          | Get order details/status       |
| POST   | /admin/menu-items     | Add new menu item (admin)      |
| PUT    | /admin/menu-items/{id}| Update menu item (admin)       |
| DELETE | /admin/menu-items/{id}| Delete menu item (admin)       |

---

## Data Models

### MenuItem

```json
{
  "id": 1,
  "name": "Margherita Pizza",
  "description": "Classic pizza with tomatoes, mozzarella, and basil.",
  "image": "https://cdn/menus/margherita.jpg",
  "price": 12.99,
  "category": "Mains",
  "available": true
}
```

### Order

```json
{
  "id": 1001,
  "items": [
    {
      "menu_item_id": 1,
      "name": "Margherita Pizza",
      "quantity": 2,
      "price": 12.99
    }
  ],
  "customer_name": "Alex",
  "customer_phone": "555-555-1234",
  "delivery_address": "123 Main St",
  "status": "pending",
  "subtotal": 25.98,
  "tax": 2.60,
  "total": 28.58,
  "created_at": "2024-05-16T20:20:00Z"
}
```