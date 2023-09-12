# Warframe Riven Auction Monitor

Warframe Riven Auction Monitor is a Python application that helps Warframe players monitor and track the Riven Mod auction market. It provides tools to keep track of ongoing auctions, historical data, and make informed decisions for Riven Mod trades. By utilizing the warframe.market API, the application retrieves real-time auction information, displays metrics, and sends notifications for important events. The Warframe Riven Auction Monitor aims to enhance trading experience, save time, and improve decision-making in the Riven Mod market.

### Prerequisites

Make sure you have the following requirements installed:

- Python 3
- PyQt5
- requests

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/tvojk13/Warframe-Riven-Auction-Monitor.git
   ```

2. Install the required packages:

   ```
   pip install PyQt5 requests
   ```

### Usage

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the application:

   ```
   python main.py
   ```

3. The GUI window will appear, allowing you to set the desired weapon and maximum price.

4. Click the "Run Task" button to start monitoring the auctions.

5. If an auction is found with a buyout price at or below the specified maximum price, it will be displayed in the application window.

6. To stop monitoring, click the "Stop Task" button.

7. To close the application, click the "Close" button or use the window's close button.

### Features

- Select a weapon from the dropdown menu to monitor its Riven auctions.
- Set a maximum price to filter the auctions.
- Drag the window by clicking and dragging on any empty area of the window.
- Minimize the window by clicking the minimize button.
- The application runs on top of other windows when focused.

### Customization

You can modify the code to customize the application's behavior:

- Change the API URL in the `ThreadTask` class to monitor different types of auctions or adjust sorting options.
- Modify the GUI layout and design by editing the `GUI.ui` file and using Qt Designer.
