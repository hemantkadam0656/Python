import json

# Here try:except: finally method is used to handle the error while opening the file. 
# json.load() is used to load the data from py file to json file format. 


def load_data():
    try:
        with open("youtube.py",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.py', 'w') as file:
        json.dump(videos, file)

# enumerate is like a loop to arrange the items of list into the index value format. 
# it always start with "0" index so that's why start=1 is important. 

def list_of_all_videos(videos):
    for index, video in enumerate(videos, start= 1):
        print("\n") 
        print("-" * 100)       
        print(f"{index}: Name = {video['name']} ,Time = {video['time']}")
        print("-" * 100)

def add_new_video(videos):
    name = input("Enter your video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name , "time":time})
    save_data_helper(videos)

def update_new_video(videos):
    list_of_all_videos(videos)
    index = int(input("Enter index of the video : "))
    if 1<= index <= len(videos):
        name = input("Enter your video name: ")
        time = input("Enter video time: ")
        print(name,time)
        videos[index -1] = {'name': name, 'time':time }
        
    else:
        print("Invalid index selected")
    save_data_helper(videos)

def delete_video(videos):
    list_of_all_videos(videos)
    index = int(input("Enter the number of the video : "))
    if 1<= index <= len(videos):
        del videos[index-1] 
        save_data_helper(videos)
    else:
        print("Invalid index selected")
    
    list_of_all_videos(videos)    
    
def main():
    videos = load_data()
    
    while True:
        print("\n ** YouTube Manager | Choice your option **")
        print("1.List of all video.")
        print("2.Add video into the list.")
        print("3.Update video into the list.")
        print("4.Detele video from list.")
        print("5.Exit.")
        choice = int(input("Enter your Choice: "))
        print(videos)

        match choice:
            case 1:
                list_of_all_videos(videos)
            case 2:
                add_new_video(videos)
            case 3:
                update_new_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                break
            case _:
                print('Invalid Choice')
            
if __name__ == "__main__":
    main()

