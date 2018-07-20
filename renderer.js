const {remote} = require('electron');
const {Menu} = remote;

var visitHomepage = function()
{
    
}

const template = [
    {
        label: "도움말(&H)",
        submenu: [
            {
                label: "홈페이지 방문",
                click: function()
                {
                    visitHomepage();
                }
            }
        ]
    }
];

const menu = Menu.buildFromTemplate(template);
Menu.setApplicationMenu(menu);