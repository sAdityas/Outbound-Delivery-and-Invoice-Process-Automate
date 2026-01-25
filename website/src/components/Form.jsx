import '../style/Dispatch.css'

export const Form = ({file,setFile,loading,setLoading,setError,setGeneralError,setResults}) => {
  
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
          console.log(file)
      
          try {
            const response = await fetch('http://localhost:5050/main', {
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
            setFile(null)
          } catch (err) {
            setGeneralError(`Failed to connect to backend: ${err.message}`);
            console.error('Fetch error:', err);
          } finally {
            setLoading(false);
          }
        };

        
  return (
    
        <form onSubmit={handleRunProcess} className="app-form">
          <input
            type="file"
            accept=".csv"
            onChange={handleFileChange}
            disabled={loading}
          />
          <button
            className='btn-primary'
            type="submit"
            disabled={loading}
          >
            {loading ? 'Processing...' : 'Run SAP Automation'}
          </button>
        </form>
  )
}


export default Form; 
 
