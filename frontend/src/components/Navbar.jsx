import Logo from '../components/Logo'
import LogoSVG from '../assets/istockphoto-698360006-1024x1024.jpg';

export default function Navbar(){
    return(
        <nav classNameName="navbar navbar-light bg-dark">
          <div classNameName="container-fluid">
            <a classNameName="navbar-brand" href="#">
              <Logo />
            </a>
            <a classNameName="navbar-brand" href="#">
            <img src={LogoSVG} alt="Logo" width="40" height="40" align="right" classNameName="d-inline-block align-top rounded-circle" />
            </a>
          </div>
        </nav>
    )
}