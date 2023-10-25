import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK with credentials from "fire.json"
cred = credentials.Certificate("fire.json")
firebase_admin.initialize_app(cred)

# Define the Firestore collection and document you want to access
collection_name = "users"
document_name = "GTdgIUUc7ahLFYWExisZmLj9Kyi2"
balfield = "balanceAmount"

# Fetch data from Firestore
db = firestore.client()
doc_ref = db.collection(collection_name).document(document_name)

# Get a specific field from the document
field_data = doc_ref.get().get(balfield)

if field_data is not None:
    print(f"{balfield} from Firestore: {field_data}")
else:
    print(f"{balfield} not found in Firestore")
