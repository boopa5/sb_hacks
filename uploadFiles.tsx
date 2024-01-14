import React, { useState, ChangeEvent } from 'react';

function FileUpload() {
  const [file, setFile] = useState<File | null>(null);

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const uploadFile = () => {
    if (file) {
      const formData = new FormData();
      formData.append('file', file);

      // Replace '/your-upload-endpoint' with your actual upload endpoint
      fetch('/your-upload-endpoint', {
        method: 'POST',
        body: formData
      })
        .then(response => response.json())
        .then(data => {
          console.log('文件上传成功', data);
        })
        .catch(error => {
          console.error('文件上传失败', error);
        });
    } else {
      alert('请选择一个文件');
    }
  };

  return (
    <div>
      <form encType="multipart/form-data">
        <input type="file" name="fileInput" onChange={handleFileChange} />
      </form>
      <button onClick={uploadFile}>上传文件</button>
    </div>
  );
}

export default FileUpload;
