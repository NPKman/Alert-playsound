
# Alert Sound System

## Description
This project is a Flask-based webhook receiver that triggers an alert sound whenever an alert is sent from Grafana. The sound is played using `pygame`.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/alert-sound-system.git
   ```
2. Navigate into the project directory:
   ```bash
   cd alert-sound-system
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - Windows: `.env\Scriptsctivate`
   - Mac/Linux: `source venv/bin/activate`
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Ensure the MP3 file (`siren-alert-96052.mp3`) is in the same directory as the script.
2. Run the Flask server:
   ```bash
   python alert_sound.py
   ```
3. Send a POST request to the `/webhook` endpoint with Grafana alert data. Example:
   ```json
   {
       "title": "Test Alert",
       "message": "This is a test message",
       "state": "alerting"
   }
   ```

## Features
- Receives alert notifications from Grafana via a webhook.
- Plays an alert sound using `pygame`.
- Logs alert details in the console.

## Dependencies
- Flask
- pygame

## Files
- `alert_sound.py`: Main script for the webhook and sound alert.
- `siren-alert-96052.mp3`: The sound file that plays on alert.

## Contributing
Feel free to fork this repository, submit issues, or create pull requests.

## License
This project is licensed under the MIT License.
