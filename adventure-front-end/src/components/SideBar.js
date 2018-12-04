import React from 'react'
import { Link } from 'react-router-dom'
import { Button } from 'reactstrap';
// import './SideBar.css'


const SideBar = () => (
    <div>
        <h2>Adventure Chat</h2>

        <Link to='/api/chat'>
            <button className={"button"} pathto='/api/chat' >
                Start Chat
                </button>
        </Link>
    </div>
)

export default SideBar
