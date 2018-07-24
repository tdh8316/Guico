const {app, BrowserWindow} = require('electron');
let win;

app.on('ready', () =>{
    win = new BrowserWindow(
        {
            width: 800,
            minWidth: 330,
            height: 500,
            minHeight: 450,
            show: false,
            icon: __dirname + './gui/resources/icon.ico',
            webPreferences :{
                defaultFontSize : 14
                }
        }
    );

    win.once('ready-to-show', function(){
        win.show();
    });

    // 윈도우 창에 로드 할 html 페이지
    win.loadURL(`file://${__dirname}/index.html`);
    win.webContents.openDevTools();
});