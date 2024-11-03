import webbrowser
import datetime
import subprocess
import os
import sqlite3 



# Connect to the SQLite database
conn = sqlite3.connect('dataBase.db')
cursor = conn.cursor()
class takeCommand():
  def execute_command(self,user_command):
    # Query the database for the command
    cursor.execute("SELECT action_type, action_value FROM commands WHERE command = ?", (user_command,))
    result = cursor.fetchone()
    
    if result:
        action_type,action_value = result
        if action_type == 'url':
            webbrowser.open(action_value)
            
        elif action_type == 'file':
            # subprocess.Popen(['start', '', action_value], shell=True)  # Use 'start' to open files on Windows
            os.startfile(action_value)
        else:
            print("Unknown action type.")
    else:
        print("Command not recognized.")

   # Close the connection when done
    conn.close()


def sayTime():
   strtime=datetime.datetime.now().strftime('%H:%M:%S')
   
  