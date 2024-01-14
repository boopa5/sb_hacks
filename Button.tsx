import "./CustomizeBn.css";
import Image1 from "/arrow.png";
//import "/uploadFiles"

function Button(){
  return (
    <div className="mdc-touch-target-wrapper">
      <div className="customize">
      <button className="mdc-fab">
        <div className="mdc-fab__ripple"></div>
        <span className="mdc-fab__icon material-icons"></span>
        <img src={Image1} width="40px" height ='40px' className="pic"/>
      </button>
    </div>
    </div>
  );
}
export default Button;
