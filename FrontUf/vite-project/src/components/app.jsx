import React, { useState } from 'react';
import { fetchBackendData } from '../api/backend';
import './App.css';

function App() {
  const [year, setYear] = useState('');
  const [localYear, setLocalYear] = useState('')
  const [data, setData] = useState(null);
  const [filteredMonths, setFilteredMonths] = useState([]);
  const [isButtonEnabled, setIsButtonEnabled] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const handleYearChange = (e) => {
    const inputValue = e.target.value;
    setLocalYear(inputValue); // Actualiza el estado local del año
    setIsButtonEnabled(true); // Habilita el botón solo cuando se modifica el año
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const parsedYear = parseInt(localYear, 10); 

    if (parsedYear < 1977 || parsedYear > 2024) {
      alert('Error: El año debe estar entre 1977 y 2024.');
      return;
    }

    setYear(parsedYear);

    setIsLoading(true);

    try {
      const response = await fetchBackendData(parsedYear, 'uf');
      if (response.success) {
        setData(response.data); // Guardar los datos
        setFilteredMonths(response.data.months); // Mostrar los datos
        setIsButtonEnabled(false);
      } else {
        alert(`Error al obtener los datos: ${response.message}`);
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleFilter = async (filterType) => {
    const endpointMap = {
      'increase': 'uf/asc',
      'decrease': 'uf/desc',
      'no-change': 'uf/noavg',
    };

    const response = await fetchBackendData(year, endpointMap[filterType]);
    if (response.success) {
      setFilteredMonths(response.data.months); // Actualizar la tabla con los datos filtrados
    } else {
      alert(`Error al obtener los datos de ${filterType}: ${response.message}`);
    }
  };

  const handleClearFilters = () => {
    if (data) {
      setFilteredMonths(data.months); // Restaurar los datos originales
    }
  };

  const formatDate = (dateString) => {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('es-ES', options);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Ingresa un año</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          placeholder="Ingresa un año"
          value={localYear}
          onChange={handleYearChange}
          required
        />
        <button
          type="submit"
          style={{
            backgroundColor: isButtonEnabled ? '#007bff' : '#ccc',
            cursor: isButtonEnabled ? 'pointer' : 'not-allowed',
          }}
          disabled={!isButtonEnabled}
        >
          Enviar
        </button>
      </form>

      {data && (
        <div style={{ marginTop: '30px', textAlign: 'left', marginLeft: '20%', marginRight: '20%' }}>
          <h2>Variaciones por mes:</h2>
          <div className="buttons-container">
            <button 
              className="filter-button"
              onClick={() => handleFilter('increase')}
              disabled={isLoading}
            >
              Meses con aumento
            </button>
            <button 
              className="filter-button"
              onClick={() => handleFilter('decrease')}
              disabled={isLoading}
            >
              Meses con disminución
            </button>
            <button 
              className="filter-button"
              onClick={() => handleFilter('no-change') }
              disabled={isLoading}
            >
              Meses sin cambio
            </button>
            <button
              className="filter-button clear-filters"
              onClick={handleClearFilters}
              disabled={isLoading}
            >
              Quitar Filtros
            </button>
          </div>

          {isLoading ? (
            <div style={{ textAlign: 'center', padding: '20px' }}>
              <p>Cargando datos...</p>
            </div>
          ) : (
            <table border="1" style={{ width: '100%', borderCollapse: 'collapse' }}>
              <thead>
                <tr>
                  <th>Mes</th>
                  <th>Variación</th>
                </tr>
              </thead>
              <tbody>
                {filteredMonths.map((item, index) => (
                  <tr key={index}>
                    <td>{item.mes}</td>
                    <td>{item.variacion}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}

          <div style={{ marginTop: '20px' }}>
            <h2>Información Adicional</h2>
            <p>
              <strong>Mejor Día:</strong> {formatDate(data.best_day.fecha)} con un valor de{' '}
              {data.best_day.valor}
            </p>
            <p>
              <strong>Peor Día:</strong> {formatDate(data.worst_day.fecha)} con un valor de{' '}
              {data.worst_day.valor}
            </p>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
