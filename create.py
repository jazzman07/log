import os


class createFirebase():
    def createFirebase(ai, msi, sb, pi, ad, ak):
        f = open("log/src/firebase.js", "a")
        f.write("""import firebase from "firebase/compat/app" """)
        f.write("""import "firebase/compat/auth" """)
        f.write(""" """)
        f.write("""const app = firebase.initializeApp({ """)
        f.write(f"""      apiKey: '{ak}' """)
        f.write(f"""      authDomain: '{ad}' """)
        f.write(f"""      projectId: '{pi}' """)
        f.write(f"""      storageBucket: '{sb}' """)
        f.write(f"""      messagingSenderId: '{msi}' """)
        f.write(f"""      appId: '{ai}' """)
        f.write(""" """)
        f.write("""}) """)
        f.write(""" """)
        f.write(""" """)
        f.write("""export const auth = app.auth() """)
        f.write("""export default app """)
