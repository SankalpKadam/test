const {app,BrowserWindow}=require('electron');
const path=require('path');
console.log(path)
require('electron-reload')(__dirname,{
	electron:path.join(__dirname,'node_modules','.bin','.electron.cmd')
});
function createWindow() {
	const win = new BrowserWindow({
		width:1200,
		height:1200,
		frame:false
	})
	win.loadFile('index.html');
	win.maximize();
}
app.on('ready',createWindow)