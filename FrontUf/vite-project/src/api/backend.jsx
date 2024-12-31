const BASE_URL = 'http://localhost:3000/';

export const fetchBackendData = async (year, endpoint) => {
    // Construir los parámetros de consulta
    const params = new URLSearchParams({ year: year.toString() }).toString();

    // Construir la URL completa
    const url = `${BASE_URL}${endpoint}?${params}`;

    // Hacer la solicitud
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
            mode: 'cors',
        });

        if (!response.ok) {
            throw new Error(`Error ${response.status}: ${response.statusText}`);
        }

        const data = await response.json();

        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        return { success: false, message: error.message };
    }
};
