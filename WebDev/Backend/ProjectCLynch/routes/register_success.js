var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
  res.render('register_success');
});

module.exports = router;