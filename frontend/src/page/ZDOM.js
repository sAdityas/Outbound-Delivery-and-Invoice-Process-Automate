
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import "../style/Dispatch.css"
import Form from '../components/Form';
import Table from '../components/Table';
import * as XLSX from 'xlsx'

export default function ZDOM() {
    const navigate = useNavigate();
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [results, setResults] = useState([]);
    const [error, setError] = useState(null);
    const [generalError, setGeneralError] = useState(null);
    const [selectedIndexes, setSelectedIndexes] = useState([])
  
  
  

     
  const handleExportToExcel = () => {
    if (selectedIndexes.length === 0) {
      alert("No rows selected to export.");
      return;
    }
  
    const selectedData = selectedIndexes.map((i) => results[i]);
    
    // Prepare data for the sheet
    const dataForExport = selectedData.map((res) => ({
      Sales_Order: res.sales_order,
      Material: res.material,
      Quantity: res.quantity,
      Invoice_Number: res.invoice_number || '-',
      Status: res.status,
      Error: res.error || '-',
    }));
  
    // Create workbook and sheet
    const workbook = XLSX.utils.book_new();
    const sheet = XLSX.utils.json_to_sheet(dataForExport);
    XLSX.utils.book_append_sheet(workbook, sheet, 'Results');
  
    // Export
    XLSX.writeFile(workbook, 'GeneratedInvoices.xlsx');
  };
    const handleNavigate = () => {
        navigate('/ZTRD');
    }
    return (
      <div className="app-container">
        <h1>Automate ZDOM Dispatch SAP Process</h1>
          <Form file={file} setFile={setFile} loading={loading} setLoading={setLoading} setError={setError} setGeneralError={setGeneralError} setResults={setResults} />
          <Table results={results} setResults={setResults} selectedIndexes={selectedIndexes} setSelectedIndexes={setSelectedIndexes} />
        {error && <div className="error-message">{error}</div>}
        {generalError && <div className="general-error">{generalError}</div>}
  
        {results.length > 0 && (
          <div className="results-section">
            <h2>Results</h2>

          </div>
        )}
        <div className='place'>
        <button
        className='btn-primary'
        onClick={handleExportToExcel}
        type='button'
        disabled={selectedIndexes.length === 0}>
          Export to Excel
        </button>
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
