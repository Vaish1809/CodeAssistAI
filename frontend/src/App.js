import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [inputCode, setInputCode] = useState('');
  const [output, setOutput] = useState('AI Output will appear here...');
  const [loading, setLoading] = useState(false);

  const API_URL = "http://localhost:8000";

  const handleGenerate = async () => {
    setLoading(true);
    try {
      const res = await axios.post(`${API_URL}/generate`, { prompt: inputCode, language: "python" });
      setOutput(res.data.result);
    } catch (err) {
      setOutput("Error connecting to backend: " + err.message);
    }
    setLoading(false);
  };

  const handleDebug = async () => {
    setLoading(true);
    try {
      const res = await axios.post(`${API_URL}/debug`, { code: inputCode });
      setOutput(res.data.analysis);
    } catch (err) {
      setOutput("Error connecting to backend: " + err.message);
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <header style={{marginBottom: '30px'}}>
        <h1>⚡ CodeAssist AI</h1>
        <p>Serverless Developer Productivity Tool</p>
      </header>

      <div className="editor-box">
        <div style={{flex: 1}}>
          <h3>Input / Prompt</h3>
          <textarea 
            value={inputCode}
            onChange={(e) => setInputCode(e.target.value)}
            placeholder="Enter a prompt (e.g., 'Write a binary search') or paste buggy code here..."
          />
          <div style={{marginTop: '10px'}}>
            <button onClick={handleGenerate} disabled={loading}>
              {loading ? 'Processing...' : '✨ Generate Code'}
            </button>
            <button onClick={handleDebug} disabled={loading} style={{background: '#d9534f'}}>
              {loading ? 'Processing...' : '🐞 Debug Code'}
            </button>
          </div>
        </div>

        <div style={{flex: 1}}>
          <h3>AI Response</h3>
          <div className="output">
            {output}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;