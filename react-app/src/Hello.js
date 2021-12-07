import React from "react";

function Hello({name, date}){
    return <h1>Hello, {name}. It's {date}.</h1>
}

Hello.defaultProps = {
    name: 'NoName',
    date: 'Today'
}

export default Hello;