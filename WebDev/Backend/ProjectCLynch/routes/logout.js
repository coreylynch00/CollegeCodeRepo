const bodyParser = require('body-parser');

var express = require('express');
var router = express.Router();

const logoutRouter = express.Router();

logoutRouter.use(bodyParser.json())

const dboper = require('../operations');

const url = 'mongodb://localhost:27017';
const dbname = 'project_db';

router.get('/', function(req, res, next) {
    res.render('logout');
    });

logoutRouter.route('/')
.all((req,res,next)=>{
    console.log(req.url);
    console.log(req.headers);
    res.statusCode=200;
    res.setHeader('Content-Type', 'text/html');
    next()
})

module.exports = router;