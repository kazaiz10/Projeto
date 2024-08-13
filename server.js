const express =require('express');
const bodyparser = require('body-parser');
const app1 = express();

const {app, BrowserWindow, ipcMain} = require('electron');
const path = require('path');
const ipc = ipcMain;

const {exec}= require('child_process');

function createWindow () {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    }
  })
  
  // and load the index.html of the app.
  mainWindow.loadURL('http://127.0.0.1:3000/robot')

  mainWindow.maximize();
  
  mainWindow.resizable = true
  // Open the DevTools.
  // mainWindow.webContents.openDevTools()
}

// Desliga app quando todas as janelas são fechadas
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})


app1.use(bodyparser.urlencoded({extended:true}))
app1.use(bodyparser.json());
app1.use(express.static("./"))

var robotpeerid
var maxusr=1

app1.get('/robot', (req,res) => {
    res.sendFile("./robot.html", {root:__dirname});
})
app1.get('/',  (req, res) => {
    res.sendFile("./client.html", {root:__dirname});
});

app1.post('/sendrobotpeer',  (req,res) => {
    console.log(req.body)   
    const {peerId}=req.body
    console.log(peerId)
    robotpeerid=peerId;

    res.json({
        status:"ok"
    })
})

app1.post('/sendpeerid', (req, res) => {
    const peerIdToSend = robotpeerid; // Obter o Peer ID do robo
    console.log("a enviar este peer: " + peerIdToSend)
    res.json({ peerId: peerIdToSend }); // Enviar o Peer ID para o cliente 
});

app1.post('/sendMessage', (req, res) => {
    const { control } = req.body;

    const executeCommand = (command) => {
        return new Promise((resolve, reject) => {
            exec(command, (error, stdout, stderr) => {
                if (error) {
                    console.error(`Error executing command: ${error}`);
                    reject(error);
                } else {
                    console.log(stdout);
                    resolve(stdout);
                }
            });
        });
    };

    let command;
    if (control == 87 || control == "up") {
        command = '/home/pi/Desktop/projetosemifinal1/dist/py/py s';
    } else if (control == 83 || control == "down") {
        command = '/home/pi/Desktop/projetosemifinal1/dist/py/py w';
    } else if (control == 65 || control == "left") {
        command = '/home/pi/Desktop/projetosemifinal1/dist/py/py a';
    } else if (control == 68 || control == "right") {
        command = '/home/pi/Desktop/projetosemifinal1/dist/py/py d';
    }  else if (control == 80 || control == "p") {
        command = '/home/pi/Desktop/projetosemifinal1/dist/py2/py2';
    } else {
        res.status(400).send('Invalid control command');
        return;
    }

    executeCommand(command)
        .then(() => {
            res.send('Command executed successfully');
        })
        .catch((error) => {
            res.status(500).send('Error executing command');
        });

    console.log(control);
});

app1.listen(3000, ()=>{
    console.log("Server on");

    app.whenReady().then(() => {
      createWindow()
  
      app.on('activate', function () {
        if (BrowserWindow.getAllWindows().length === 0) createWindow()
      })
    })
});