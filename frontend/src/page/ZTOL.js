
import * as XLSX from 'xlsx'
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import "../style/Dispatch.css"

export default function ZTOL() {

    const navigate = useNavigate();
    const [loading, setLoading] = useState(false);
    const [results, setResults] = useState([]);
    const [error, setError] = useState(null);
    const [generalError, setGeneralError] = useState(null);
    const [file, setFile] = useState(null);
    const [selectedIndexes, setSelectedIndexes] = useState([])
  
  
  
    const handleFileChange = (e) => {
      setFile(e.target.files[0]);
    };
    
    const handleRunProcess = async (e) => {
      e.preventDefault();
      setLoading(true);
      setError(null);
      setGeneralError(null);
      setResults([]);
  
      const formData = new FormData();
      if (!file) {
        setError('Please select an Excel/CSV file.');
        setLoading(false);
        return;
      }
      formData.append('file', file);
  
      try {
        const response = await fetch('http://localhost:5050/ZTRD', {
          method: 'POST',
          body: formData,
        });
        const data = await response.json();
        if (!response.ok) {
          setGeneralError(data.error || 'An error occurred while processing.');
        } else {
          if (data.results) {
            setResults(data.results);
          } else {
            setGeneralError(data.error || 'No results returned from server.');
          }
        }
      } catch (err) {
        setGeneralError(`Failed to connect to backend: ${err.message}`);
        console.error('Fetch error:', err);
      } finally {
        setLoading(false);
      }
    };
    const handleRowClick = (index) => {
      setSelectedIndexes((prev) =>
        prev.includes(index)
          ? prev.filter((i) => i !== index) // remove if already selected
          : [...prev, index]                // add if not selected
      );
    };
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
        navigate('/');
    }
  
    return (
      <div className="app-container">
        <h1>Automate Dispatch SAP Process</h1>
        <form onSubmit={handleRunProcess} className="app-form">
          <input
            type="file"
            accept=".csv"
            onChange={handleFileChange}
          />
          <button
            className='btn-primary'
            type="submit"
            disabled={loading}
          >
            {loading ? 'Processing...' : 'Run SAP Automation'}
          </button>
        </form>
  
        {error && <div className="error-message">{error}</div>}
        {generalError && <div className="general-error">{generalError}</div>}
  
        {results.length > 0 && (
          <div className="results-section">
            <h2>Results</h2>
            <table className="results-table">
              <thead>
                <tr>
                  <th>Sales Order</th>
                  <th>Quantity</th>
                  <th>Invoice Number</th>
                  <th>Status</th>
                  <th>Error</th>
                </tr>
              </thead>
              <tbody>
                {results.map((res, idx) => (
                  <tr key={idx}
                  onClick={() => handleRowClick(idx)}
                  className={selectedIndexes.includes(idx) ? 'selected' : ''}>
                    <td>{res.sales_order}</td>
                    <td>{res.quantity}</td>
                    <td>{res.invoice_number || '-'}</td>
                    <td className={res.status === 'Success' ? 'status-success' : 'status-failure'}>
                      {res.status}
                    </td>
                    <td className="error-cell">{res.error || '-'}</td>
                  </tr>
                ))}
              </tbody>
            </table>
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
            <span>Go to ZDOM</span>
        </button>
        </div>
      </div>
    );
}
