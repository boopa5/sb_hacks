
import "./TopBar.css";
import Image from "/login.png";
import Image3 from "/logo.png";

function TopBar() {
  return (
    <header className="mdc-top-app-bar">
      <div className="mdc-top-app-bar__row">
        <section className="mdc-top-app-bar__section mdc-top-app-bar__section--align-start">
          <div className="myRightbutton">
            <button
            className="material-icons mdc-top-app-bar__navigation-icon mdc-icon-button"
            aria-label="About us" 
          >
          </button>
          </div>
        </section>
        <section
          className="mdc-top-app-bar__section mdc-top-app-bar__section--align-end"
          role="toolbar"
        > <div className="mybutton">
          <button
            className="material-icons mdc-top-app-bar__action-item mdc-icon-button"
            aria-label="Login"
          >
          </button>
          </div>
          <img src={Image} width="40px" height ='40px' className="Rightpic"/>
        </section>
      </div>
    </header>
  );
}

export default TopBar;
