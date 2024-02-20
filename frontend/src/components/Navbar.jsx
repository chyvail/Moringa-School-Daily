import Logo from '../components/Logo'
import LogoSVG from '../assets/istockphoto-698360006-1024x1024.jpg';

export default function Navbar(){
    return(
        <nav className="navbar navbar-light bg-dark">
          <div className="container-fluid">
            <a className="navbar-brand" href="#">
              <Logo />
            </a>
            <a className="navbar-brand" href="#">
            <img src={LogoSVG} alt="Logo" width="40" height="40" align="right" className="d-inline-block align-top rounded-circle" />
            </a>
          </div>
        </nav>
    )
}