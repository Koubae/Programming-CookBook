import sqlite3
import os


def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(empId, name, photo, resumeFile):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sqlite.db')
    try:    
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO new_employee
                                  (id, name, photo, resume) VALUES (?, ?, ?, ?)"""

        empPhoto = convertToBinaryData(photo)
        resume = convertToBinaryData(resumeFile)


        # Convert data into tuple format
        data_tuple = (empId, name, empPhoto, resume)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        conn.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")

insertBLOB(1, "Smith", "smith.jpg", "smith_resume.txt")
insertBLOB(2, "David", "david.jpg", "david_resume.txt")



def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def readBlobData(empId):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sqlite.db')
    try:    
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * FROM new_employee WHERE id = ?"""
        cursor.execute(sql_fetch_blob_query, (empId,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name  = row[1]
            photo = row[2]
            resumeFile = row[3]

            print("Storing employee image and resume on disk \n")
            photoPath = "db_data\" + name + ".jpg"
            resumePath = "db_data\" + name + "_resume.txt"
            writeTofile(photo, photoPath)
            writeTofile(resumeFile, resumePath)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("sqlite connection is closed")

readBlobData(1)
readBlobData(2)