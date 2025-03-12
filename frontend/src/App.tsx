import React from 'react';
import CarrerasList from './components/CarrerasList';

const App: React.FC = () => {
    return (
        <div>
            <h1>Planificador Universitario</h1>
            <CarrerasList />
        </div>
    );
};

export default App;