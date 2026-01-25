
import React, { useState } from 'react';
// import { useNavigate } from 'react-router-dom';  
import '../style/Dispatch.css'
import Form from '../components/Form';
import Table from '../components/Table.jsx';
import ExportButton from '../components/ExportButton';


export default function ZDOM() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState([]);
  const [error, setError] = useState(null);
  const [generalError, setGeneralError] = useState(null);
  const [selectedIndexes, setSelectedIndexes] = useState([]);
  const [signing, setSigning] = useState(false);

  const gotozdsc = () => {
    window.location.replace("/zdsc");
  };


  const signdocument = async () => {
  setLoading(true);
  setSigning(true);
  setError(null);
  setGeneralError(null);

  try {
    const response = await fetch('http://localhost:5050/zdsc', {
      method: 'POST',
    });

    const data = await response.json();

    if (!response.ok) {
      setGeneralError(data.error || 'Signing failed');
    } else {
      setResults(data.results || []);
    }
  } catch (err) {
    setGeneralError(err.message);
  } finally {
    setLoading(false);
    setSigning(false);
  }
};


  const resetAll = () => {
    setFile(null);
    setResults([]);
    setSelectedIndexes([]);
    setSigning(false);
    setError(null);
    setGeneralError(null);
  };

  return (
    <div className="app-containers">
      <h1>Automate Domestic Sale Dispatch SAP Process</h1>

      <Form
        file={file}
        setFile={setFile}
        loading={loading}
        setLoading={setLoading}
        setError={setError}
        setGeneralError={setGeneralError}
        setResults={setResults}
        signing={signing}
      />

      {error && <div className="error-message">{error}</div>}
      {generalError && <div className="general-error">{generalError}</div>}

      {results.length > 0 && (
        <>
          <Table
            results={results}
            selectedIndexes={selectedIndexes}
            setSelectedIndexes={setSelectedIndexes}
          />

          {!signing && (
            <button className="sign-button" onClick={signdocument} disabled={loading}>
              Sign Document
            </button>
          )}
        </>
      )}

      <div className="place">
        <ExportButton selectedIndexes={selectedIndexes} results={results} />

        <button className="reset-button" onClick={resetAll} disabled={signing || loading}>
          Reset
        </button>
        <button className="dsc-button" onClick={gotozdsc} disabled={signing || loading}>
          Digital Signature
        </button>
      </div>
    </div>
  );
}

 
