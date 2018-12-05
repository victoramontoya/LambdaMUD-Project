import React from 'react'
import { Switch, Route } from 'react-router-dom'
import Adventure from './Adventure'
import Login from './Login'
import Register from './Register'

// import './Main.css'


// The Main component renders one of the three provided
// Routes (provided that one matches). Both the /roster
// and /schedule routes will match any pathname that starts
// with /roster or /schedule. The / route will only match
// when the pathname is exactly the string "/"
const Main = () => (
    <Switch>
        <Route exact path='/adv/login' component={Login} />
        <Route path='/adv/register' component={Register} />
        <Route path='/adv/adventure' component={Adventure} />



    </Switch>

)

export default Main
