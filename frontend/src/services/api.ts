import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000/api/', // URL de Django
});

export const getCarreras = () => api.get('carreras/');
export const getMaterias = () => api.get('materias/');