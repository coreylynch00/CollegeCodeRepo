const bodyParser = require('body-parser');

var express = require('express');
var router = express.Router();

const registerRouter = express.Router();

registerRouter.use(bodyParser.json())

const dboper = require('../operations');

const url = 'mongodb://localhost:27017';
const dbname = 'project_db';

router.get('/', function(req, res, next) {
    res.render('register');
  });

registerRouter.route('/')
.all((req,res,next)=>{
    console.log(req.url);
    console.log(req.headers);
    res.statusCode=200;
    res.setHeader('Content-Type', 'text/html');
    next()
})


.post((req, res, next)=>{
    MongoClient.connect(url).then((client) => {

        console.log('Connected To Server');
        const db = client.db(dbname);
        const obj = JSON.parse(JSON.stringify(req.body));
        console.log (obj)

        dboper.insertDocument(db, obj,
        "register")
        .then((result) => {
            console.log("User details:\n", result.ops);
            res.render('register_success', {prod:obj})
        }).catch((err) => console.log(err));
        client.close;
    }).catch((err) => console.log(err));
})

.put((req, res, next)=>{
    res.statusCode=403;
    res.end('Put operation not supported :'+req.body.name+' '+req.body.description);
})

.delete((req, res, next)=>{
    res.end('Delete user')
})


module.exports = router;