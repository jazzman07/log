import firebase from "firebase/compat/app"
import "firebase/compat/auth"

const app = firebase.initializeApp({
  apiKey: "AIzaSyC9wBGB-YjueHaTj-dAi1hnfYRJPa1BwX4",
  authDomain: "jmlogin-31632.firebaseapp.com",
  projectId: "jmlogin-31632",
  storageBucket: "jmlogin-31632.appspot.com",
  messagingSenderId: "253848895496",
  appId: "1:253848895496:web:b0417532cf3abb7ec2d1bd"

})

export const auth = app.auth()
export default app

