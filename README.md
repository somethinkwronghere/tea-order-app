# Web-Based Tea Ordering System

This project is a web-based version of a desktop tea/beverage ordering application. It allows users to place beverage orders through a web interface and provides an admin panel for managing orders, pricing, inventory, and other aspects of the system.

## Features

### Client Side
- User selection from a list of available computers/users
- Beverage ordering interface with categorized options
- Shopping cart functionality
- Order notes with character limits
- Total price calculation
- Frequently used orders management
- Stock status indication
- Real-time order status updates

### Admin Side
- Live order monitoring with elapsed time display
- Order completion and cancellation with reason
- Price management for all beverages
- Stock status management
- Computer/user management
- Server note management for client notifications
- Order history viewing

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Backend**: Python, Flask, Flask-SocketIO
- **Data Storage**: JSON files, Excel spreadsheet
- **Real-time Communication**: WebSockets via Socket.IO

## Project Structure

```
tea_order_web/
├── client/              # Client-side files (if needed)
├── server/              # Server-side application
│   ├── data/            # Data storage directory
│   ├── static/          # Static files
│   │   ├── css/         # CSS stylesheets
│   │   │   ├── styles.css    # Client styles
│   │   │   └── admin.css     # Admin panel styles
│   │   └── js/          # JavaScript files
│   │       ├── client.js     # Client functionality
│   │       └── admin.js      # Admin panel functionality
│   ├── templates/       # HTML templates
│   │   ├── index.html   # Client interface
│   │   └── admin.html   # Admin interface
│   ├── app.py           # Main Flask application
│   └── requirements.txt # Python dependencies
└── README.md            # Project documentation
```

## Installation and Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd tea_order_web
   ```

2. Install Python dependencies:
   ```
   cd server
   pip install -r requirements.txt
   ```

3. Run the server:
   ```
   python app.py
   ```

4. Access the application:
   - Client interface: http://localhost:5000/
   - Admin interface: http://localhost:5000/admin

## Usage

### Client Interface
1. Select your computer/user name from the list
2. Add beverages to your cart
3. Write any notes about your order (optional)
4. Send the order
5. Receive real-time updates on your order status

### Admin Interface
1. View incoming orders in real-time
2. Process orders by marking them as completed or canceled
3. Manage product prices, stock availability
4. Add/edit/remove computer names
5. Set server notes for client notifications
6. View order history

## Data Storage

- **prices.json**: Stores product prices
- **stock.json**: Stores product availability
- **computers.json**: Stores registered computer/user names
- **notes.json**: Stores server notes
- **orders.xlsx**: Stores order history in Excel format
- **frequent_orders.json**: Stores frequent orders for users

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This web-based application was adapted from an original desktop version developed with tkinter and socket communication. 