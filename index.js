//var http = require("http");
const express = require('express');
const app = express();
var engines = require('consolidate');
app.set('views', __dirname);
app.engine('html', engines.mustache);
app.set('view engine', 'html');
app.use(express.static(__dirname));
app.listen(3000);
app.get('/', (req, res) => {
    res.render('home.html');
})
// function onRequest(req, res) {
    
//     res.writeHead(200, {'Content-Type': 'text/html','Content-Length':data.length});
//     res.write(data);
//     res.end();
// } 
// http.createServer(onRequest).listen(8000);