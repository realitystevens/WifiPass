import subprocess


def getProfiles():
    """List all Wi-Fi profiles on the system"""
    command = ['netsh', 'wlan', 'show', 'profiles']

    """Run the command and capture the output text and return code"""
    result = subprocess.run(command, capture_output=True, text=True)

    """
        Check if command was successful
        If the return code is not 0, then there was an error
    """
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")

        return []
    
    """Extract profile names from the command output"""
    profiles = []
    for line in result.stdout.split('\n'):
        if "All User Profile" in line:
            profiles.append(line.split(":")[1].strip())

    return profiles


def getPassword(profile_name):
    """List all Wi-Fi profile information with password"""
    command = ['netsh', 'wlan', 'show', 'profiles', profile_name, 'key=clear']
    
    """Run the command and capture the output text and return code"""
    result = subprocess.run(command, capture_output=True, text=True)

    """
        Check if command was successful
        If the return code is not 0, then there was an error
    """
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")

        return []
    
    """Extract password from the command output"""
    for line in result.stdout.split('\n'):
        if "Key Content" in line:
            return line.split(":")[1].strip()
        

    return None


def main():
    profiles = getProfiles()

    if not profiles:
        print("No Wi-Fi profile available")

        return
    
    print("Wi-Fi Profiles and Passwords:")
    for profile in profiles:
        password = getPassword(profile)
        if password:
            print(f"Profile: {profile} | Password: {password}")
        else:
            print(f"Profile: {profile} | Password: Unable to retrieve")





if __name__ == "__main__":
    main()
