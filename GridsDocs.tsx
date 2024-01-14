import "./GridsDesign.css"


const GridsDoc: React.FC = () => {
  // 生成按钮数组，可以根据需要调整按钮数量和内容
  const buttons = Array.from({ length: 5 }, (_, index) => (
    <button key={index}> 
      
      <div className="text"> FileName {index + 1}</div>
        
    </button>
  ));

  return (
    <div className="button-grid">
      {buttons}
    </div>
  );
};

export default GridsDoc;
