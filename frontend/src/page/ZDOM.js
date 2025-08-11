
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import "../style/Dispatch.css"
import Form from '../components/Form';
import Table from '../components/Table';
import ExportButton from '../components/ExportButton';

export default function ZDOM(dataForExport) {
    const navigate = useNavigate();
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [results, setResults] = useState([]);
    const [error, setError] = useState(null);
    const [generalError, setGeneralError] = useState(null);
    const [selectedIndexes, setSelectedIndexes] = useState([])


  
    const handleNavigate = () => {
        navigate('/ZTRD');
    }
  
    return (
      <div className="app-container">
        <h1>Automate ZDOM Dispatch SAP Process</h1>
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
            <span>Go to ZTRD</span>
        </button>
        </div>
      </div>
    );
}
