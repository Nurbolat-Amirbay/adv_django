# Nutrient Counter Project

## Overview
The Nutrient Counter is a Django web application designed to help users track their food consumption and visualize nutrient intake. Users can add food items, delete them, and view their consumption data in a user-friendly interface.

## Features
- Add new food items with nutritional information (carbs, proteins, fats, and calories).
- Delete food items from the database.
- Visualize food consumption data.
- Display total nutrient counts based on user consumption.

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd nutrient_counter
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install django
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## Usage
- Navigate to the main page to view and manage food items.
- Use the provided forms to add or delete food items.
- Visualize your food consumption data through the dedicated visualization page.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.