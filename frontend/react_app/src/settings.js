let API_SERVER = '';

switch (process.env.NODE_ENV) {
    case 'development':
        API_SERVER = 'http://localhost:8000';
        break;
    case 'production':
        API_SERVER = process.env.REACT_APP_API_SERVER;
        break;
    default:
        API_SERVER = 'http://localhost:8000';
        break;
}

export { API_SERVER };

export const SESSION_DURATION = 5*3600*1000;