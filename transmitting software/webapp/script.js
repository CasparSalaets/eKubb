const kubbList = document.getElementById('kubbList');
let kubbs = [];

function setupField(){
    for(let i = 0; i < 5; i++){
        newKubb = document.createElement('div');
        newKubb.className = "kubb";
        newKubb.setAttribute("id", "kubb" + 'L' + String(i));
        newKubb.setAttribute("staatrecht", true);
        kubbList.appendChild(newKubb);
        newKubb.style.transform = "translate(-300px, " + String(-250 + 92*(i+1)) + "px)";
    }
    for(let i = 0; i < 5; i++){
        newKubb = document.createElement('div');
        newKubb.className = "kubb";
        newKubb.setAttribute("id", "kubb" + 'R' + String(i));
        newKubb.setAttribute("staatrecht", true);
        newKubb.style.transform = "translate(300px, " + String(-250 + 92*(i+1)) + "px)";
        kubbList.appendChild(newKubb);
    }
    kubbs = kubbList.children;
}

let socket = undefined;

function connect_socket() {
    // Close any existing sockets
    disconnect_socket();

    socket = new WebSocket("ws://192.168.4.1:80/connect-websocket");

    // Connection opened
    socket.addEventListener("open", (event) => {
        statusbutton = document.getElementById('status');
        statusbutton.textContent = "Status: Connected";
        statusbutton.style.color = 'green';
    });

    socket.addEventListener("close", (event) => {
        socket = undefined;
        statusbutton = document.getElementById('status');
        statusbutton.textContent = "Status: Disconnected";
        statusbutton.style.color = 'red'
    });

    socket.addEventListener("message", (event) => {
        console.log(event.data);
        message = JSON.parse(event.data);
        if(typeof(message.name) === String){
            omvallen(message.name);
        }
    });

    socket.addEventListener("error", (event) => {
        socket = undefined;
        statusbutton = document.getElementById('status');
        statusbutton.textContent = "Status: Disconnected";
        statusbutton.style.color = 'red'
    });
}

function disconnect_socket() {
    if (socket != undefined) {
        socket.close();
    }
}

function sendCommand(command) {
    if (socket != undefined) {
        socket.send(command)
    } else {
        alert("Not connected to the PICO")
    }
}

//commands voor individuele kubbs
function omvallen(kubbId){
    document.getElementById(kubbId).setAttribute("staatrecht", false);
    document.getElementById(kubbId).style.backgroundColor = 'red';
}

function rechtzetten(kubbId){
    document.getElementById(kubbId).setAttribute("staatrecht", true);
    document.getElementById(kubbId).style.backgroundColor = 'blue';
}

//commands voor het hele veld
function get_staandeKubbs(){
    let staandeKubbs = [];
    Array.from(kubbs).forEach(element => {
        if(element.getAttribute('staatrecht') === "true"){
            staandeKubbs.push(element);
        }
    });
    return staandeKubbs;
}

function get_gevallenKubbs(){
    let staandeKubbs = [];
    Array.from(kubbs).forEach(element => {
        if(element.getAttribute('staatrecht') === "false"){
            staandeKubbs.push(element);
        }
    });
    return staandeKubbs;
}

setupField();
