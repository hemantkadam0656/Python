import sqlite3

con = sqlite3.connect("youTubemanager.db")

cur = con.cursor()

cur.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL,
            time TEXT NOT NULL
            )
''')


def list_of_videos():
    cur.execute("SELECT * FROM videos") 
    empty_row = cur.fetchall()
    if empty_row == []:
        print(f"List is Empty {empty_row}") 
    else:
       for row in cur.fetchall():
        print(row)  

def Add_videos(name,time):
    cur.execute("INSERT INTO videos (name,time) values(?, ?)",(name,time))
    con.commit()

def update_videos(video_id,name,time):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ? ", (name,time,video_id))
    con.commit()

def delete_videos(video_id):
    cur.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()

def main():
    while True:
        print("\n YouTube Manager App | Select your choice")
        print("1.List of all Videos")
        print("2.Add video into List")
        print("3.update video into List")
        print("4.Delete video from List")
        print("5.Exit from App")
        choice = int(input("Enter your Choice: "))

        match choice:
            case 1:
                list_of_videos()
            case 2:
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                Add_videos(name,time)  
            case 3:
                video_id = int(input("Enter video id: "))
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                update_videos(video_id,name,time)
            case 4:
                video_id = int(input("Enter video id to delete: "))
                delete_videos(video_id)
            case 5:
                break
            case _:
                print("Invalid choice")

    con.close()        

if __name__ == "__main__":
    main()

