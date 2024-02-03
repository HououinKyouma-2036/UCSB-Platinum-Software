import React, { useState, useEffect } from 'react';
import { googleLogout, useGoogleLogin } from '@react-oauth/google';
import '../Styles/App.css';
import axios from 'axios';

function LoginButton () {
    const [ user, setUser ] = useState(null);
    const [ profile, setProfile ] = useState(null);

    const login = useGoogleLogin({
        onSuccess: (codeResponse) => setUser(codeResponse),
        onError: (error) => console.log('Login Failed:', error)
    });

    useEffect(() => {
        if (user) {
            console.log(123)
            axios
                .get(`https://www.googleapis.com/oauth2/v1/userinfo?access_token=${user.access_token}`, {
                    headers: {
                        Authorization: `Bearer ${user.access_token}`,
                        Accept: 'application/json'
                    }
                })
                .then((res) => {
                    setProfile(res.data);
                })
                .catch((err) => console.log(err));
        }
        }, [ user ]
    );

    const logOut = () => {
        googleLogout();
        setProfile(null);
    };

    return (
        profile ? (
            <div>
                <img src={profile.picture} alt="user pic" />
                <p>Hi, {profile.name} 😊!</p>
                <button className='loginButton' onClick={logOut}>Log out</button>
            </div>
        ) : (
            <button className='loginButton' onClick={login}>Login</button>
        )
    );
};

export default LoginButton;
