from bson import ObjectId

def convert_mongo_document(doc):
    if not doc:
        return doc
    
    doc = dict(doc)
    for key, value in doc.items():
        if isinstance(value, ObjectId):
            doc[key] = str(value)
    return doc

def convert_mongo_list(docs):
    return [convert_mongo_document(d) for d in docs]
