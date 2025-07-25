# AY Forms App

## Running locally

### Backend setup

1. Ensure Python (version 3.13 or above) is installed on the system.
2. Create and activate a virtual environment, in the same directory where the app's source is placed.
3. Run `pip install -r app/requirements.txt` to install server-side dependencies.
4. Once the dependencies are installed, run `python app/init_demo.py` to initialize the database with demo users.
5. Run `python app/main.py` to start the backend (API) server.

### Frontend setup

1. Navigate to the `web` directory, and run `npm install` to install dependencies for the frontend.
2. Run `npm run dev` to start the frontend server.
3. The app would be accessible at `http://localhost:5173`.
