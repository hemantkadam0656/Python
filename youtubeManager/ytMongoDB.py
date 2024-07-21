from pymongo import MongoClient
from bson import ObjectId


#This is not good practice to use username and password directly into thr link instead of assigning variables from user of function.
client = MongoClient("mongodb+srv://youtubepy:hemant0656@cluster0.vakdbhi.mongodb.net/")

#client is variable but ["youtubemanager"] this is name of database ("whatever you want")

db = client["youtubemanager"]

video_collection = db['video']

# print(video_collection)

def list_of_videos():
    for video in video_collection.find():
        print(f"Id:{video['_id']} Name:{video['name']} and Duration:{video['time']}")

def add_new_video(name,time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id,new_name,new_time):
    video_collection.update_one({'_id': ObjectId(video_id)} ,
                                { "$set": {'name': new_name , 'time': new_time}}
                            )

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})
    

def main():
    while True:
        print("\n YouTube Manager APP")
        print("1.List of all videos")
        print("2.Add new video")
        print("3.Update new video")
        print("4.Delete video from List")
        print("5.exit from App")
        choice = int(input("Enter your option : "))

        match choice:
            case 1:
                list_of_videos()
            case 2:
                name = input("Enter name of video : ")
                time = input("Enter name of time : ")
                add_new_video(name,time)
            case 3:
                video_id = input("Enter video id to update :")
                new_name = input("Enter new name of video : ")
                new_time = input("Enter new time of video : ")
                update_video(video_id,new_name,new_time)
            case 4:
                video_id = input("Enter video id to update :")
                delete_video(video_id)
            case 5:
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()