function callPythonFunction(param) {
    console.log('Calling Python function with param:', param);

    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ param }),
    };

    return fetch('/Subsystems/grpcController/call_python_function', requestOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Result from Python function:', data.result);
            return data.result;
        })
        .catch(error => {
            console.error('Error calling Python function:', error);
            throw error;
        });
}

