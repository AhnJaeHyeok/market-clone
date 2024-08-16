import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";
import { getStorage } from "firebase/storage";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyBIZaTOw2jEMjnRw52RJJNCaqEYzhkeIRg",
  authDomain: "carrot-market-30dcd.firebaseapp.com",
  databaseURL:
    "https://carrot-market-30dcd-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "carrot-market-30dcd",
  storageBucket: "carrot-market-30dcd.appspot.com",
  messagingSenderId: "1025425189035",
  appId: "1:1025425189035:web:e0d098c306cf065feeafee",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app);
const auth = getAuth(app);
