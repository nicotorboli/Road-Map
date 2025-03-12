import React, { useEffect, useState } from 'react';
import { getCarreras } from '../services/api';

interface Carrera {
    id: number;
    nombre: string;
}

const CarrerasList: React.FC = () => {
    const [carreras, setCarreras] = useState<Carrera[]>([]);

    useEffect(() => {
        getCarreras().then(response => {
            setCarreras(response.data);
        });
    }, []);

    return (
        <ul>
            {carreras.map(carrera => (
                <li key={carrera.id}>{carrera.nombre}</li>
            ))}
        </ul>
    );
};

export default CarrerasList;