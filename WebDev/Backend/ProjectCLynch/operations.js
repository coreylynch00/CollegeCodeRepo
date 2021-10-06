const assert = require('assert');

//INSERT TO COLLECTION
exports.insertDocument = (db, document, collection, callback)=>{
    const coll = db.collection(collection);
    return coll.insert(document);
}

//FIND FROM COLLECTION
exports.findDocuments = (db, collection, callback)=>{
    const coll = db.collection(collection);
    return coll.find({}).toArray();
}

//REMOVE FROM COLLECTION
exports.removeDocument = (db, document, collection, callback)=>{
    const coll = db.collection(collection);
    return coll.deleteOne(document);
}

//UPDATE COLLECTION
exports.updateDocument = (db, document, update, collection, callback) => {
    const coll = db.collection(collection);
    return coll.updateOne(document, { $set: update}, null);
}