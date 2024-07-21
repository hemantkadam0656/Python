import requests

def fetch_userdata():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        user_data = data["data"]
        # print(user_data)
        for i in user_data['data']:
            # print(type(i))
            # name = i["name"]["first"]
            gender = i["gender"]
            # print(gender)
            return gender
        # gender,name = user_data["data"][0]["gender"],user_data["data"][0]["name"]["first"]
        # return gender,name
    

def main():
    try:
        gender = fetch_userdata()
        print(f"name of user , gender: {gender }")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()