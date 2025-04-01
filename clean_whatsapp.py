import re
import pandas as pd

# Load the WhatsApp chat data file
file_path = "C:\Users\Acer\OneDrive\Documents\VIT Query Chatbot"

# Read the file
with open(file_path, "r", encoding="utf-8") as file:
    chat_data = file.readlines()

# Regular expression to parse WhatsApp chat data
message_pattern = re.compile(r"(\d{2}/\d{2}/\d{2}), (\d{2}:\d{2} (?:AM|PM|am|pm)) - ([^:]+): (.+)")

# Store structured data
cleaned_data_v2 = []

# Extract and structure the data
for line in chat_data:
    line = line.strip()
    match = message_pattern.match(line)
    if match:
        date, time, sender, message = match.groups()
        cleaned_data_v2.append({
            "Date": date,
            "Time": time,
            "Sender": sender,
            "Message": message
        })

# Convert structured data to DataFrame
df_cleaned = pd.DataFrame(cleaned_data_v2)

# Save the cleaned data as a CSV file
csv_file_path = "cleaned_whatsapp_chat.csv"
df_cleaned.to_csv(csv_file_path, index=False)

print(f"✅ Data cleaned and saved as '{csv_file_path}' successfully!")
