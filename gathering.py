import time

# Mock data simulating a Facebook profile
mock_facebook_data = {
    "username": "johndoe",
    "name": "John Doe",
    "bio": "Software Developer | Open Source Enthusiast",
    "followers": 1234,
    "profile_picture": "https://github.com/nutlope.png"
}

def fetch_facebook_profile(username: str) -> dict:
    # Simulate a delay to mimic API call
    time.sleep(2)
    
    # Check if the username matches the mock data
    if username.lower() == mock_facebook_data["username"]:
        return mock_facebook_data
    else:
        raise ValueError("User not found")

def display_profile(profile: dict):
    print("\nFacebook Profile")
    print(f"Name: {profile['name']}")
    print(f"Username: @{profile['username']}")
    print(f"Bio: {profile['bio']}")
    print(f"Followers: {profile['followers']}")
    print(f"Profile Picture: {profile['profile_picture']}")

def main():
    print("Facebook Profile Lookup")
    while True:
        username = input("Enter Facebook username (or 'exit' to quit): ").strip().lower()
        
        if username == 'exit':
            print("Exiting the program.")
            break
        
        try:
            print("Fetching profile...")
            profile = fetch_facebook_profile(username)
            display_profile(profile)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
