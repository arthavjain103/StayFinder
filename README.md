# StayFinder

A Django-based web application for browsing, filtering, and booking hotels. Users can register, log in, search for hotels by amenities, view hotel details, and book rooms for specific dates.

---

## Tech Stack

- **Python 3.x**: Core programming language for backend logic.
- **Django**: High-level Python web framework for rapid development, ORM, authentication, and admin interface.
- **Django Unfold**: Modern, customizable admin interface for Django, providing a better user experience for administrators compared to the default Django admin. Used in this project to enhance the admin panel's usability and appearance.
- **SQLite**: Lightweight, file-based database for development and testing.
- **Bootstrap 5**: Frontend CSS framework for responsive and modern UI design.
- **HTML5 & CSS3**: Markup and styling for custom templates and layouts.
- **JavaScript**: For interactive UI elements (minimal, mostly handled by Bootstrap).
- **Pillow Library**: (If used) For image handling in Django models.

**Purpose of Each:**

- **Django**: Provides a robust backend, built-in authentication, ORM for database management, and a powerful admin panel for easy data management.
- **Django Unfold**: Replaces the default Django admin with a more modern, user-friendly, and customizable interface, making admin tasks more efficient and visually appealing.
- **SQLite**: Simple, zero-configuration database ideal for prototyping and local development.
- **Bootstrap**: Ensures the UI is mobile-friendly and visually appealing with minimal custom CSS.
- **HTML/CSS/JS**: Customizes the look and feel of the site and enables dynamic user interactions.
- **Pillow**: Handles image uploads and processing in Django models.

---

## Features

- **User Registration & Authentication**:

  - Secure sign-up, login, and logout functionality using Django's built-in authentication system.
  - Only registered users can book rooms and view their bookings.

- **Hotel Browsing & Filtering**:

  - Users can browse a list of hotels with images, descriptions, and amenities.
  - Filter hotels by price (ascending/descending), amenities (multi-select), and available dates.
  - Search hotels by name or description.

- **Hotel Detail & Gallery**:

  - View detailed information about each hotel, including a photo gallery and list of amenities.
  - See room count and starting price.

- **Room Booking**:

  - Authenticated users can book rooms for specific check-in and check-out dates.
  - The system checks for room availability and prevents overbooking.
  - Bookings are stored and associated with the user.

- **Booking Management**:

  - Users can view a list of all their booked rooms, including hotel name, booking dates, and more.
  - Search through bookings by hotel name.

- **Admin Interface**:

  - Django admin panel for managing hotels, amenities, images, and bookings.
  - Admins can add, edit, or delete hotels, amenities, and view all bookings.

- **Responsive UI**:

  - Clean, modern, and mobile-friendly interface using Bootstrap.
  - Consistent look and feel across all pages.

- **User Feedback**:
  - Success and error messages are displayed for actions like login, registration, and booking.

---

## Project Structure

```
hotel_app/
│
├── hotel/
│   ├── home/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── templates/
│   │   │   ├── base.html
│   │   │   ├── home.html
│   │   │   ├── hotel_detail.html
│   │   │   ├── booked_rooms.html
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   └── messages.html
│   │   └── ...
│   ├── hotel/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── public/
│   │   └── static/
│   │       └── hotel_images/
│   ├── db.sqlite3
│   └── manage.py
└── venv/
```

---

## Data Models

- **Amenities**: Hotel amenities (e.g., WiFi, Pool)
- **Hotel**: Main hotel entity with name, price, description, room count, and amenities (many-to-many)
- **Hotel_Image**: Images associated with each hotel
- **Hotel_Booking**: Stores bookings with user, hotel, check-in/out dates, and booking type

---

## Setup & Installation

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd hotel_app
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install django
   # (Add any other dependencies if required)
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the app**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Usage

- **Home Page**: Browse and filter hotels by price, amenities, and date.
- **Hotel Detail**: View hotel info, gallery, and book a room (login required).
- **Booked Rooms**: See your bookings.
- **Admin**: Manage hotels, amenities, images, and bookings at `/admin/`.

---

## Screenshots

### Application Screenshots

Here are screenshots of the hotel booking application in action:

![Home Page - Hotel Listings](screenshots/Screenshot%202025-07-10%20091535.png)
_Home page showing hotel listings with search and filter options_

![Hotel Detail Page](screenshots/Screenshot%202025-07-10%20091546.png)
_Hotel detail page with gallery and booking form_

![Booking Management](screenshots/Screenshot%202025-07-10%20091558.png)
_Booked rooms management page showing user's bookings_

---

## Future Enhancements

- **Payment Integration**: Add online payment (Stripe, Razorpay, PayPal) for prepaid bookings.
- **Email Notifications**: Send booking confirmations and reminders.
- **Hotel Reviews & Ratings**: Enable users to review and rate hotels.
- **Internationalization**: Support multiple languages and currencies.

---
