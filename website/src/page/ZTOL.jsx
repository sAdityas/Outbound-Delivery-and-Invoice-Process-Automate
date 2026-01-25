
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Form from '../components/Form';
import Table from '../components/Table.jsx';
import ExportButton from '../components/ExportButton';
import "../style/Dispatch.css"

export default function ZTOL() {

    const navigate = useNavigate();
    const [loading, setLoading] = useState(false);
    const [results, setResults] = useState([]);
    const [error, setError] = useState(null);
    const [generalError, setGeneralError] = useState(null);
    const [file, setFile] = useState(null);
    const [selectedIndexes, setSelectedIndexes] = useState([])

  
    const handleNavigate = () => {
        navigate('/');
    }
  
    return (
      <div className="app-container">
        <h1>Automate Dispatch SAP Process</h1>
        <Form file={file} setFile={setFile} loading={loading} setLoading={setLoading} setError={setError} setGeneralError={setGeneralError} setResults={setResults} />
  
        {error && <div className="error-message">{error}</div>}
        {generalError && <div className="general-error">{generalError}</div>}
  
        {results.length > 0 && (
          <div className="results-section">
            <h2>Results</h2>
            <Table results={results} setResults={setResults} selectedIndexes={selectedIndexes} setSelectedIndexes={setSelectedIndexes} />
          </div>
        )}
        <div className='place'>
          <ExportButton selectedIndexes={selectedIndexes} results={results} />
        <button
        className='btn-primary'
        type='button'
        onClick={handleNavigate}> 
            <span>Go to ZDOM</span>
        </button>
        </div>
      </div>
    );
}
 
 
