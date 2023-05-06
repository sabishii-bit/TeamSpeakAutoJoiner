import ts3
import schedule
import time

def get_credentials():
    server_ip = input("Enter your TeamSpeak server IP: ")
    server_port = int(input("Enter your TeamSpeak server port (default: 10011): ") or 10011)
    server_username = input("Enter your TeamSpeak server username: ")
    server_password = input("Enter your TeamSpeak server password: ")
    target_channel_name = input("Enter the name of the target channel: ")
    join_time = input("Enter the time to join the channel (24-hour format, e.g. 00:00-23:59): ")

    return server_ip, server_port, server_username, server_password, target_channel_name, join_time

def join_channel(server_ip, server_port, server_username, server_password, target_channel_name):
    with ts3.query.TS3Connection(server_ip, server_port) as ts_connection:
        ts_connection.login(
            client_login_name=server_username,
            client_login_password=server_password
        )

        ts_connection.use(sid=1)  # Use the first virtual server by default

        me = ts_connection.whoami()[0]  # Get information about the bot's own client
        channels = ts_connection.channellist()[0]  # Get a list of all channels

        # Find the target channel's ID
        target_channel_id = None
        for channel in channels:
            if channel["channel_name"] == target_channel_name:
                target_channel_id = channel["cid"]
                break

        # Check if the bot is already in the target channel
        if me["client_channel_id"] == target_channel_id:
            print("Already in the target channel.")
            return

        # Join the target channel
        ts_connection.clientmove(cid=target_channel_id, clid=me["client_id"])
        print(f"Joined the {target_channel_name} channel.")

# Get user input for credentials and settings
server_ip, server_port, server_username, server_password, target_channel_name, join_time = get_credentials()

# Schedule the script to run at the specified time
schedule.every().day.at(join_time).do(join_channel, server_ip, server_port, server_username, server_password, target_channel_name)

# Keep the script running and checking for scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute