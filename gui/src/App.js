import logo from './logo.svg';
import './App.css';
import { useFilePicker } from 'use-file-picker';
import React, { useEffect } from 'react';

function App() {
  return <Page />
}

class Page extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      files: [],
      selectedFile: '',
    };
    this.handleChange = this.handleChange.bind(this);
    // this.deleteFile = this.deleteFile.bind(this);
  }

  componentDidMount() {
    this._isMounted = true;
  }

  componentWillUnmount() {
    this._isMounted = false;
  }

  getUploadedFiles() {
    const requestOptions = {
      method: 'GET',
      // headers: { 'Content-Type': 'text/html; charset=utf-8', },
    };
    fetch('http://localhost:5000/files', requestOptions)
      .then(response => response.json())
      .then(result => {
        this.setState({
          files: result
        });
      });
  }

  handleChange(event) {
    this.setState({selectedFile: event.target.value});
  }

  deleteFile() {
    const requestOptions = {
      method: 'DELETE',
      headers: {'Content-Type' : 'text/plain'}
    };
    console.log(this.state.selectedFile);
    fetch('http://localhost:5000/files/' + this.state.selectedFile, requestOptions)
      .then(response => console.log(response.body));
  }

  render() {
    return (
      <div>
        <FileSelector />
        <button onClick={() => {
          this.getUploadedFiles()
        }}>Get Uploaded Files </button>
        <ul>
          {this.state.files.map(file => (
            <li>{file}
            </li>
          ))}
        </ul>
        <input type="text" value={this.state.selectedFile} onChange={this.handleChange} />
        <button onClick={() => {this.deleteFile()}}>Delete File </button>
      </div>
    );
  }
};

function uploadFile(file) {
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'multipart/form-data' },
  };
  fetch('http://localhost:5000/files/' + file.name, requestOptions)
    .then(response => console.log(response.body));
}

function FileSelector() {
  const [openFileSelector, { filesContent, loading, errors, plainFiles, clear }] = useFilePicker({
    multiple: true,
    readAs: 'DataURL', // availible formats: "Text" | "BinaryString" | "ArrayBuffer" | "DataURL"
    // accept: '.ics,.pdf',
    accept: ['.json', '.pdf'],
    limitFilesConfig: { min: 1, max: 1 },
    // minFileSize: 1, // in megabytes
    // maxFileSize: 1,
    // readFilesContent: false, // ignores file content
  });

  if (errors.length) {
    return (
      <div>
        <button onClick={() => openFileSelector()}>Something went wrong, retry! </button>
        {errors[0].fileSizeTooSmall && 'File size is too small!'}
        {errors[0].fileSizeToolarge && 'File size is too large!'}
        {errors[0].readerError && 'Problem occured while reading file!'}
        {errors[0].maxLimitExceeded && 'Too many files'}
        {errors[0].minLimitNotReached && 'Not enought files'}
      </div>
    );
  }

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <button onClick={() => openFileSelector()}>Select file </button>
      <button onClick={() => clear()}>Clear</button>
      <br />
      Selected file:
      <br />
      {plainFiles.map(file => (
        <div key={file.name}>{file.name}</div>
      ))}{ }
      <button onClick={() => {
        if (plainFiles.length > 0) {
          uploadFile(plainFiles[0]);
        }
      }}>Upload File </button>
    </div>
  );
}

export default App;
