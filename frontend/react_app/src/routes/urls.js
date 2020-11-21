import React from "react";
import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";

import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import Signup from "../pages/SignUp";

function PrivateRoute({ isAuthenticated, children, ...rest}) {
    console.log("is authenticated??", isAuthenticated)
    return (
        <Route
            {...rest}
            render={({ location }) => 
            isAuthenticated ? (
                children
            ) : (
                <Redirect
                    to={{
                        pathname: "/login/",
                        state: { from:location }
                    }}
                />
            )
            }
        />
    )
}

function Urls(props) {
    return (
        <div>
            <BrowserRouter>
                <Switch>
                    <Route exact path="/login/"> <Login {...props} /></Route>
                    <Route exact path="/signup/"> <Signup {...props} /></Route>
                    <PrivateRoute exact path="/" isAuthenticated={props.isAuthenticated}><Dashboard {...props}/></PrivateRoute>
                </Switch>
            </BrowserRouter>
        </div>
    )
};

export default Urls;